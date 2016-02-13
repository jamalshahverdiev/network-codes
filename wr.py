#!/bin/env python

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
	arg5 = raw_input('Cixisini faylda saxlamaq istediyiniz cisco emrini daxil edin: ')
        buff = ''
        resp = ''
        ssh = paramiko.SSHClient()
        #ssh.get_host_keys().add('172.16.100.100', 'ssh-rsa', key)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(arg1, username=arg2, password=arg3, look_for_keys=False, allow_agent=False)
       
	chan = ssh.invoke_shell()
        chan.send('en\n')
        time.sleep(1)
        resp = chan.recv(9999)
        print resp

        chan.send('terminal length 0\n')
        time.sleep(1)

	chan.send(arg5+'\n')
	time.sleep(3)
	resp = chan.recv(9999)
	wrout = open(arg1+'.command.txt', 'w')
	wrout.writelines(resp)

	print('\n')
	ssh.close()

while True:
        print("Secimleriniz: ")
        print("1. Router-deki istenilen emri fayl sistemde yadda saxlmaq ucun, 1 reqemi daxil edib Enter sixin.")
        print("2. Scriptden cixmaq ucun, 2 reqemi daxil edib Enter sixin.")
        ent = input('Xahish olunur seciminizi daxil edib Enter sixin: ')
        if ent == 1:
                tftpcon()
        else:
                break
