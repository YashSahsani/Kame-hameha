import nmap
nm = nmap.PortScanner()
def get_os_(ip):
	print(nm.scan(ip,arguments='-O'))
	print(nm.command_line())
	return nm[ip]['osmatch'][0]['osclass'][0]['vendor']

