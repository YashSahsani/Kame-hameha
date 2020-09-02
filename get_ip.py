import grequests
import threading
class Test(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def exception(self, request, exception):
        print ("Problem: {}: {}".format(request.url, exception))

    def tasync(self):
        results = grequests.map((grequests.get(u) for u in self.urls), exception_handler=self.exception, size=5)
        print (results)
    def run(self):
        response = os.popen("ping -n 1")
for i in range(50):
	Test(i,"Thread-"+str(i),i).start()