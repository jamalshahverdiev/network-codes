#!/usr/bin/python

import paramiko

ssh = paramiko.SSHClient()
#ssh.get_host_keys().add('172.16.100.100', 'ssh-rsa', key)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.16.100.100', port=22, username='jamal', password='freebsd', look_for_keys=False, allow_agent=False)

def shipintbr():
        stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
        output = stdout.readlines()
        print('\n'.join(output))
	print('\n')
	ssh.close()

ssh1 = paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh1.connect('172.16.100.100', port=22, username='jamal', password='freebsd', look_for_keys=False, allow_agent=False)
def shintfa():
	stdin, stdout, stderr = ssh1.exec_command('sh int fa 0/0')
	out = stdout.readlines()
	print('\n'.join(out))
	ssh.close()

shipintbr()
shintfa()
