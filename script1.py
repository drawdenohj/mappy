#!/bin/bash/python
import sys
import signal
import subprocess
import gip
import extip
import net
import mapi


def inputNumber(message):
	while True:
		try:
			interger = int(raw_input(message))
		except ValueError:
			print('This is not a valid option, Duh! ')
			continue
		else:
			return interger
			break


def clear():
	subprocess.call(['clear'])


def main():
	while True:
		try:			
			clear()
			print '[+] Choose an Option: '
			print ''
			print '[1] Internal IP'
			print '[2] External IP'
			print '[3] View your network range'
			print '[4] Nmapping...'
			print '[5] Exit'

			x = inputNumber('Choose! ')
			if x == 1:
				clear()		
				gip.getip()
				print ''
				print '[0] To Go Back'
				print '[1] To Exit'
				a = inputNumber('Choose! ')
				if a == 0:
					clear()			
					main()
				else:
					sys.exit(0)
			if x == 2:
				clear()
				extip.exip()
				print ''
				print '[0] To Go Back'
				print '[1] To Exit'
				a = inputNumber('Choose! ')
				if a == 0:
					clear()			
					main()
				else:
					sys.exit(0)
			if x == 3:
				clear()
				net.net()
				print ''
				print '[0] To Go Back'
				print '[1] To Exit'
				a = inputNumber('Choose! ')
				if a == 0:
					clear()			
					main()
				else:
					sys.exit(0)()
			if x == 4:
				clear()
				mapi.nmapi()
				print ''
				print '[0] To Go Back'
				print '[1] To Exit'
				a = inputNumber('Choose! ')
				if a == 0:
					clear()			
					main()
				else:
					sys.exit(0)
			if x == 5:
				clear()
				sys.exit(0)	

		except KeyboardInterrupt:
			print 'Bye!'
			sys.exit()


main()
	

