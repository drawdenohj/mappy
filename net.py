#!/bin/bash/python

from subprocess import Popen, PIPE

def net():
	n = Popen(['hostname','-I'], stdout=PIPE, stderr=PIPE)
	stdout, stderr = n.communicate()	
	stdout = stdout[:10] + '1/24' + stdout[12:]
	print '[+] Network Range: ' + stdout[:14] 
	return '' 
	

