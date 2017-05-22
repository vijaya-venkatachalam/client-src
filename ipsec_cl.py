import vici
import sys
import subprocess
import hashlib

'''
routines for enabling and disabling the modems. 
id = modem id in dbus notation (eg. Modem/0)
retruns none
'''

print ("child-sa = %s", sys.argv[1])
machid=subprocess.check_output(["dmidecode","-s","system-uuid"])
contid = machid.decode()
cname=contid.rstrip()
print("local id = %s",cname)
if (sys.argv[1] == "server2"):
    rem_ip = "78.33.59.117"
    updown_scr = "/root/vv/l2updown.sh"
else:
    rem_ip = "78.33.59.116"
    updown_scr = "/root/vv/l2updown2.sh"
print("remote ip = %s, updown script = %s",rem_ip,updown_scr)
    
s = vici.Session()
server_cfg = { sys.argv[1] : { 'version' : '2', 'local_addrs' : [sys.argv[2]] , 'remote_addrs' : [rem_ip], 'encap' : 'yes', 'mobike' : 'no', 'local' : { 'auth' : 'psk' , 'id' : cname} ,  'remote' : { 'auth' : 'psk' , 'id' : sys.argv[1]} , 'children' : { sys.argv[1] : {'mode' : 'TRANSPORT', 'updown' : updown_scr} }}}
secr = { 'type' : 'ike', 'data' : 'v+NkxY9LLZvwj4qCC2o/gGrWDF2d21jL'}
s.load_conn(server_cfg)
s.load_shared(secr)
list(s.initiate({'child' : sys.argv[1]}))
    

