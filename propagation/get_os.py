import nmap
nm = nmap.PortScanner()
def get_os_(ip):
    nm.scan(ip,arguments='-O')
    try:
        return nm[ip]['osmatch'][0]['osclass'][0]['vendor']
    except:
        return None
