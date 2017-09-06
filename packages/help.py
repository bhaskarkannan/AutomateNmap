import os
from termcolor import colored, cprint

class Autohelp:

	def __init__(self):
		print "******************* "
		print "    Help    "
		print "******************* "
	def help(self):
		helpc = '''

help	-> List all options to help	 


scans	-> List all options to scan


about	-> Detail about the Developer and tool


clear	-> To clear the text


quit	-> Quit
			'''
		print helpc
