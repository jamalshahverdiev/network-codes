import paramiko
import cmd
import time
import sys

ssh = paramiko.SSHClient()
#ssh.get_host_keys().add('172.16.100.100', 'ssh-rsa', key)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.16.100.100', username='jamal', password='freebsd', look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh.exec_command('copy tftp: disk0:')

stdin.write('172.16.100.20')
stdin.write('\n')
stdin.flush()
stdin.write('sshexeconrouter.py')
stdin.write('\n')
stdin.flush()
stdin.write('sshexeconrouter.py')
stdin.write('\n')

output = stdout.readlines()
print('\n'.join(output))
ssh.close()

