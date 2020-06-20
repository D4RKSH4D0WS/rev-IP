#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
C0 = "\033[0;36m"
C1 = "\033[1;36m"
G0 = "\033[0;32m"
G1 = "\033[1;32m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"

import requests
import os
import sys


try:
	os.system('clear')
	print '''%s
    ____            ________
   / __ \___ _   __/  _/ __ \\
  / /_/ / _ \ | / // // /_/ /   %s|| Coded by D4RKSH4D0WS%s
 / _, _/  __/ |/ // // ____/    %s|| Mass Reverse IP%s
/_/ |_|\___/|___/___/_/
'''%(C1,W0,C1,W0,C1)
	fl=sys.argv[1]
	op=open(fl).read().splitlines()
	file=raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mSave results : ')
	if file == '':
		exit('%s[%s!%s] %sYou stupid'%(W1,R1,W1,W0))
	print
	for x in op:
		site=requests.get('http://api.hackertarget.com/reverseiplookup/?q='+x).text
		if 'API count exceeded' in site:
			exit('%s[%s!%s] %sChange your IP'%(W1,R1,W1,W0))
		print '%s[%s*%s] %sReversing %s ...'%(W1,R1,W1,W0,x)
		print '%s[%s*%s] %s%s domains found for %s'%(W1,R1,W1,W0,len(site.split('\n')),x)
		open(file,"a+").write(site+"\n")
	print
	print '%s[%s>%s] %sDone, saved in %s'%(W1,G1,W1,W0,file)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 rev.py ip.txt'%(W1,R1,W1,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))

