#!/usr/bin/python

import paramiko
import cmd
import time
import sys

def main(argv):
        if len(sys.argv) == 0:
                sys.stderr.write('Please enter router IP as first and TFTP server IP as second arqument.\n')
                sys.exit
        else:
		arg1 = raw_input('Xahish olunur Router IP unvanini daxil edesiniz: ')
		print(arg1)
		arg2 = raw_input('Xahish olunur TFTP serverin IP unvanini daxil edesiniz: ')
		print(arg2)
if __name__ == '__main__':
        sys.exit(main(sys.argv))

