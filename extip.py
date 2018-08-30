#!/bin/bash/python
import subprocess

def exip():
	subprocess.call(['curl','ifconfig.me'])
	return ''


