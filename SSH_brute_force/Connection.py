import sys
from threading import Thread
try:
    from paramiko import SSHClient
    from paramiko import AutoAddPolicy
    from paramiko import util
except ImportError:
    print('Missing Paramiko Dependency.')
    sys.exit(0)

class Connection(Thread):
    def __init__(self, username, password, targetIp, portNumber, timeoutTime):
        super(Connection, self).__init__()
        self.username = username
        self.password = password
        self.targetIp = targetIp
        self.portNumber = portNumber
        self.timeoutTime = timeoutTime
        self.status = ""
    def run(self):
        util.log_to_file("main_paramiko_log.txt", level = "INFO")
        sshConnection = SSHClient()
        sshConnection.set_missing_host_key_policy(AutoAddPolicy())
        try:
            sshConnection.connect(self.targetIp, port=int(self.portNumber),
                                  username=self.username, password=self.password,
                                  timeout=int(self.timeoutTime), allow_agent=False, look_for_keys=False)

            self.status = 'Succeeded'
            sshConnection.close()
        except:
            self.status = 'Failed'