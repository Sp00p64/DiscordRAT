# DiscordRAT
Discord Remote Administration Tool fully written in Python3.

This is a RAT controlled over Discord with over 20 post exploitation modules.

## **Disclaimer:**

This tool is for educational use only, the author will not be held responsible for any misuse of this tool.\
This is my first project on github as such it is far from perfect,I will listen to any criticism as long as it is constructive.


## **Setup Guide:**
You will first need to register a bot with the Discord developper portal and then add the bot to the server that you want (make sure bot as administrator privileges).
Once the bot is created copy the token of your bot and paste it at line 18.\

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
**Advice:**\
If you have problems with the installation of win32api or other modules , try installing it in a python virtual environment.\
Please avoid opening issues about module related errors as it is related to your python install and not a problem inherent of DiscordRAT.\
If you encounter "AttributeError: module 'enum' has no attribute 'IntFlag'" while compiling to Pyinstaller please do :
```
pip uninstall enum34
```
