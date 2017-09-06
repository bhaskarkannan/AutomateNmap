
import socket
import sys,os
import time
import ipaddress
from termcolor import colored, cprint
from pyfiglet import figlet_format
from packages import help
from packages import scans
from packages import aboutme
os.system('clear')
time.sleep(1) 
cprint(figlet_format('Auto Nmap', font='starwars'), 'yellow', 'on_blue', attrs=['bold'])

name = colored('''	Developed by:BhaskarKANNAN  Twitter: @Bhaskarkanan''', 'yellow', attrs=['blink'])
version = colored('''		Version 1''', 'yellow', attrs=['blink'])
print version


inst = colored('''	 Type 'help' to play with the tool ''', 'yellow', attrs=['blink'])

quit = colored("Quitting ... :( ", 'red', attrs=['bold'])

print " "
print name
print " "
print inst


class fresh:
	def __init__(self):
		print " "
	def Start(self):
		if option == "1":
			scanner1 = os.system("sudo nmap -T4 -A -v -oN /home/.autonmap-logs/basic/intense --script ip-geolocation-geoplugin.nse "+str(targetaddr))
			print scanner1
			print colored ('Scan Has Been Completed , scan logs saved in /home/.autonmap-logs/ [+]' , 'green' , attrs=['bold'])


		#elif option == "2":
		 #   	scanner2 = os.system("sudo nmap -sS -O -oN /home/.nmapii-logs/basic/port_os" +str   	#(targetaddr))
	#	    	print scanner2
	#	    	print colored ('[+] Scan Has Been Completed , scan logs saved in /home/.nmapii-logs/ [+]' , 'green' , attrs=['bold'])
		#elif option == "3":
		 #   	scanner3 = os.system("sudo nmap -sS -sC" + str(targetaddr))
		  #  	print scanner3
		   # 	print colored ("Scan Has Been Completed", 'yellow' , attrs=['bold'])



		elif option == "2":
		    	scanner2 = os.system("sudo nmap -p 443 -oN /home/.autonmap-logs/SSL/heartbleed --script ssl-heartbleed.nse,ip-geolocation-geoplugin.nse "+str(targetaddr))
			print scanner2
			print colored ('Scan Has Been Completed , scan logs saved in /home/.autonmap-logs/ [+]' , 'green' , attrs=['bold'])
		elif option == '3':	
			scanner3 = os.system('sudo nmap -T4 -sS -Pn -O -oN /home/.autonmap-logs/SSH/ssh --script ssh-hostkey.nse,ssh2-enum-algos.nse,dns-brute.nse,ip-geolocation-geoplugin.nse -p 22 '+str(targetaddr))
			print scanner3
			print colored ('Scan Has Been Completed , scan logs saved in /home/.autonmap-logs/ [+]' , 'green' , attrs=['bold'])
		elif option == "4":
		    	scanner4 = os.system("sudo nmap -p 80 -sV -oN /home/.autonmap-logs/SQLInjection/sqlinject --script=http-sql-injection ,ip-geolocation-geoplugin.nse "+str(targetaddr))
			print scanner4
			print colored ('Scan Has Been Completed , scan logs saved in /home/.autonmap-logs/ [+]' , 'green' , attrs=['bold'])
		elif option == "5":
		    	scanner5 = os.system("sudo nmap -p 443 -sV -oN /home/.autonmap-logs/SSL/ssl --script ssl-enum-ciphers,ip-geolocation-geoplugin.nse "+str(targetaddr))
			print scanner5
			print colored ('Scan Has Been Completed , scan logs saved in /home/.autonmap-logs/ [+]' , 'green' , attrs=['bold'])
		elif option == "6":
		    	scanner6 = os.system("sudo nmap -sU -sS -p U:137,T:139 -oN /home/.autonmap-logs/SMB/smb --script smb-enum-shares.nse,ip-geolocation-geoplugin.nse "+str(targetaddr))
			print scanner6
			print colored ('Scan Has Been Completed , scan logs saved in /home/.autonmap-logs/ [+]' , 'green' , attrs=['bold'])

 
if __name__ == "__main__":
	options=[str(i) for i in range(7)]
	options.append('help')
	options.append('scans')
	options.append('about')
	options.append('clear')
	options.append('quit')
	options.append('search')	

	while  1:
		print ""
		option=raw_input('Enter the option > ') 
		print ""
		if option in options:
				
			if option=="help":
				x=help.Autohelp()
				x.help()
			elif option == "scans":
				x=scans.scan()
				x.scanc()
			elif option == "about":
				x=aboutme.abtme()
				x.myself()
			elif option == "quit":
				os.system('clear')
				#print banner
				print quit
				time.sleep(3)
				os.system('clear') 
				sys.exit(0)
			elif option == "clear":
				os.system('clear')
				#print banner
				print name
				print ""
				print inst
				print " "
		
			else:		
				print ""
				targetaddr = str(raw_input('Target Address >'))
				
			
				ip = ipaddress.ip_address(unicode(targetaddr))
				print colored ("Target addresss is Valid.", 'green', attrs=['bold'])	
				
				#targetport = str(raw_input('Target port >'))	
				print ""
				print "[+] Option => '%s'"%option
				print ""
				print "[+] Target => '%s'"%targetaddr
				print ""
				#print "[+] Prot => '%s' "%targetport
				#print ""	
				print colored ("[+] Your Scan will start in few seconds [+]" , 'yellow' , attrs=['bold'])

				time.sleep(2)
				fresh().Start()
		
		else : 
				print ""
				print colored ("[-] OOOOOPPPPPSSSSSS, '%s' is incorrect. Please check the spell or type  'help'" , 'red' , attrs=['bold'])%option
				print ""
				continue 	
		
	print ""
	targetaddr = str(raw_input('Target Address >'))
	print ""
	print "[+] Option => '%s'"%option
	print ""
	print "[+] Target => '%s'"%targetaddr
	print ""
	print "[+] Scan will start in few seconds [+]"

	time.sleep(2)
	fresh().Start()
	option=""




