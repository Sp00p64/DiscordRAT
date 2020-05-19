# DiscordRAT
Discord Remote Administration Tool fully written in Python3.

This is a RAT controlled over Discord with over 20 post exploitation modules.

## **Disclaimer:**

This tool is for educational use only, the author will not be held responsible for any misuse of this tool.\
This is my first project on github as such this project is far from perfect , I will listen to any criticism as long as it is constructive.


## **Setup Guide:**
You will first need to register a bot with the Discord developper portal and then add the bot to the server that you want.
Once the bot is created copy the token of your bot and paste it at line 18 if you use the WithCV or line 17 if you choose the WithoutCV .\
Now on go on discord , go to the settings , go to appearance , scroll to the bottom , and activate "Developer Mode",now go to the server where your bot added right click on the channel where you want the bot to post , click copy ID and finally , paste the channel  ID (not server ID) in the parenthesis in line 97 if you use the NoCV or line 67 if you use the WithCV.\
Install requirements ("pip3 install -r requirements.txt")\
Then if steps above were succesful after launching the python file, or executable , it will post a message on the server with a generated uuid , all that is left to do is posting "!interact " with the given uuid.\
Now your bot should be available to use ! 

**Requirements:**\
Python3,Windows

**Compiling to exe (optional):**\
If you want to compile the bot to exe you can use PyInstaller.\
Inside the directory of the bot execute "PyInstaller --onefile --noconsole DiscordRAT.py" or "python3 -m PyInstaller --onefile --noconsole DiscordRAT(NoCV).py (or DiscordRAT.py)"\
If an error occured during compiling try to import the discord module "PyInstaller --onefile --noconsole --hidden-import=discord DiscordRAT.py"

**Advice:**\
If you have problems with the installation of win32api or other modules , try installing it in a python virtual environment.\
There are two python files one has opencv and webcam related modules the other does not, this has been done because open-cv adds multiple dozens of megabytes to the compiled .exe file.
