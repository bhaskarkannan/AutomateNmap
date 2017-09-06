import os
from termcolor import colored, cprint

class scan:
	def __init__(self):
		print ""
		print " *************************"
		print "     List of Scans   "
		print "*************************** "
		print ""
	def scanc(self):
		list = '''
[1] Intense Scan

[2] Heartbleed Scan

[3] SSH Scan

[4] SQL Injection

[5] SSL Enum Ciphers

[6] SMB Enum

			'''
		print list

	#def ser(self):
		
		list = ['','INTENSE SCAN','HEARTBLEED SCAN','SSH SCAN','SQL INJECTION','SSL ENUM CIPHERS','SMB ENUM']
		string = str(raw_input("Search keyword: ")).upper()
#print string
		for s in list:
    			if string in str(s):
        #print 'Yes'
        #print list.index(s)
        			index = list.index(s)
        #print "[",list[index],"]","=>",list.index(s)
       
        			print "PRESS","[",list.index(s),"]","<===========",list[index] 
		


