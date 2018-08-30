#!/bin/bash/python
import subprocess
from subprocess import Popen, PIPE

def nmapi():
	
	gip = Popen(['hostname','-I'], stdout=PIPE, stderr=PIPE)
	stdout, stderr = gip.communicate()
	
	if len(stdout) == 13:
		print '[+] Your IP: ' + stdout [:12]	
	
	elif len(stdout) == 15:  
		print '[+] Your IP: ' + stdout [:14]	

	else:
		print '[+] Your IP: ' + stdout [:13]

	stdout = stdout[:10] + '1/24' + stdout[12:]
	print '[+] Network Range: ' + stdout[:14] 
	
	net = stdout[:14]
	print '[+] Nmapping to: ' + net[:14]
	subprocess.call(['nmap', net])		
	return ''

