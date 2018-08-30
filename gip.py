#!/bin/bash/python

from subprocess import Popen, PIPE

def getip():
	gip = Popen(['hostname','-I'], stdout=PIPE, stderr=PIPE)
	stdout, stderr = gip.communicate()
	
	if len(stdout) == 13:
		print '[+] Your IP: ' + stdout [:12]	
	
	elif len(stdout)==15:  
		print '[+] Your IP: ' + stdout [:14]	

	else:
		print '[+] Your IP: ' + stdout [:13]
	return ''


