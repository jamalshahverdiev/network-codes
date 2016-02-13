#!/usr/bin/python

import paramiko
import cmd
import time
import sys

def tftpcon():
	print('\n')
	print('Script Router(IP, istifadeci adi, shifre) melumatlarini ve TFTP serverin IP unvaninin daxil edilmesini teleb edir.')
	arg1 = raw_input('Xahish olunur Router IP unvanini daxil edesiniz: ')
	arg2 = raw_input('Xahish olunur Router istifadeci adini daxil edesiniz: ')
	arg3 = raw_input('Xahish olunur Router shifresini daxil edesiniz: ')
	arg4 = raw_input('Xahish olunur TFTP serverin IP unvanini daxil edesiniz: ')
	buff = ''
	resp = ''
	ssh = paramiko.SSHClient()
	#ssh.get_host_keys().add('172.16.100.100', 'ssh-rsa', key)
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(arg1, username=arg2, password=arg3, look_for_keys=False, allow_agent=False)
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	chan = ssh.invoke_shell()
	chan.send('en\n')
	time.sleep(1)
	resp = chan.recv(9999)
	print resp
	chan.send('copy tftp: disk0:\n')
	time.sleep(1)
	resp = chan.recv(9999)
	print resp
	chan.send(arg4+'\n')
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
	print('\n')
	ssh.close()

while True:
	print("Secimleriniz: ")
	print("1. TFTP serverden Router-e fayl kocurmek ucun, 1 reqemi daxil edib Enter sixin.")
	print("2. Scriptden cixmaq ucun, 2 reqemi daxil edib Enter sixin.")
        ent = input('Xahish olunur seciminizi daxil edib Enter sixin: ')
	if ent == 1:
		tftpcon()
	else:
		break
