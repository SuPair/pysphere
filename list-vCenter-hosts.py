#_*_coding:utf-8_*_
__author__ = 'jidong'

from pysphere import VIServer
import ssl

vCenterIP = "192.168.10.100"                   
username = "administrator@vsphere.local"
password = "password"

#######################################
# Disable SSL verification in Python  #
#######################################
def DisableSSL():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
#######################################

def main():
    DisableSSL()
    server = VIServer()
    server.connect(vCenterIP,username,password)
    hostslist = server.get_hosts().values()
    # print hostslist

    f = open("hosts.txt","w")
    sep = "\n"
    f.write(sep.join(hostslist))
    f.close()

    #Disconnecting from the server
    server.disconnect()

if __name__ == '__main__':
    main()
