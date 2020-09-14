import nmap
portscan = nmap.PortScanner()
def check_open_port(ip):
	portscan.scan(ip,'22')
	if(portscan[ip].state() == 'up'):
		return True
	else:
		return False

