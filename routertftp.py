#!/usr/bin/python

import paramiko
import os
import time
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.16.100.100', port=22, username='jamal', password='freebsd', look_for_keys=False, allow_agent=False)

channel = ssh.invoke_shell()

channel_data = str()
host = str()
srcfile = str()

while True:
	if channel.recv_ready():
		channel_data += channel.recv(9999)
	else:
		continue
	
	if channel_data.endswith('R1>'):
		channel.send('en\n')
		time.sleep(1)
	elif channel_data.endswith('R1#'):
		channel.send('copy tftp: disk0:\n')
	elif channel_data.endswith('remote host []? '):
		host = raw_input('\n\n\tEnter the TFTP host IP: ')
		channel.send(host+'\n')
	elif channel_data.endswith('Source filename []? '):
		srcfile = raw_input('\n\n\tEnter the source file: ')
		channel.send(srcfile+'\n')
	elif channel_data.endswith('Destination filename []? '.format(srcfile)):
		channel.send('\n')
	elif '(Timed out)' in channel_data:
		print('\nError: Connection to TFTP Server {} timed out'.format(host))
		channel_data = ''
		channel.send('\n')
