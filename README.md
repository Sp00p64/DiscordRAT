# DiscordRAT
Discord Remote Administration Tool fully written in Python3.

This is a RAT controlled over Discord with over 20 post exploitation modules.

## **Disclaimer:**

This tool is for educational use only, the author will not be held responsible for any misuse of this tool.\
This is my first project on github as such it is far from perfect,I will listen to any criticism as long as it is constructive.


## **Setup Guide:**
You will first need to register a bot with the Discord developper portal and then add the bot to the server that you want (make sure bot as administrator privileges).
Once the bot is created copy the token of your bot and paste it at line 18.

Install requirements :
```
pip3 install -r requirements.txt
```
Then if steps above were succesful after launching the python file, or executable , it will create a new channel and post a message on the server with a generated uuid.\
Now your bot should be available to use ! 

**Requirements:**\
Python3,Windows(x64)

**Compiling to exe (optional):**\
If you want to compile the bot to exe you can use PyInstaller.\
Inside the directory of the bot execute 
```
PyInstaller --onefile --noconsole DiscordRAT.py
```
Or 
``` 
python3 -m PyInstaller --onefile --noconsole "DiscordRAT.py"
```
If an error occured during compiling try to import the discord module 
```
PyInstaller --onefile --noconsole --hidden-import=discord DiscordRAT.py
```

## **Modules**
```
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
```
## **Advice:**
If you have problems with the installation of win32api or other modules , try installing it in a python virtual environment.\
Please avoid opening issues about module related errors as it is related to your python install and not a problem inherent of DiscordRAT.\
If you encounter "AttributeError: module 'enum' has no attribute 'IntFlag'" while compiling to Pyinstaller please do :
```
pip uninstall enum34
```
