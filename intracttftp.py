import paramiko
import cmd
import time
import sys


buff = ''
resp = ''

ssh = paramiko.SSHClient()
#ssh.get_host_keys().add('172.16.100.100', 'ssh-rsa', key)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.16.100.100', username='jamal', password='freebsd', look_for_keys=False, allow_agent=False)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
chan = ssh.invoke_shell()

##### first we enable!
chan.send('en\n')
time.sleep(1)
resp = chan.recv(9999)
print resp

##### enablepassword!
#chan.send('freebsd\n')
#time.sleep(1)
#resp = chan.recv(9999)
#print resp

##### get into config mode
chan.send('copy tftp: disk0:\n')
time.sleep(1)
resp = chan.recv(9999)
print resp

##### turn off paging
#chan.send('terminal pager 0\n')
#time.sleep(1)
#resp = chan.recv(9999)
##### print resp

##### Display how many users are connected to the IPSEC vpn
chan.send('172.16.100.20\n')
time.sleep(1)
resp = chan.recv(9999)
print resp

chan.send('sshexeconrouter.py\n')
time.sleep(1)
resp = chan.recv(9999)
print resp

chan.send('sshexeconrouter.py\n')
time.sleep(1)
resp = chan.recv(9999)
print resp

ssh.close()

