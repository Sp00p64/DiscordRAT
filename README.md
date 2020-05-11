# DiscordRAT
Discord Remote Administration Tool fully written in Python3.

This is a RAT controlled over Discord with 20 post exploitation modules.

## **DISCLAIMER:**

/!\ This tool is for educational use only.The author will not be held responsible for any misuse of this tool.

## **Setup Guide:**
You will first need to register a bot with the Discord developper portal and then add the bot to the server that you want.
Once the bot is created copy the token of your bot and paste it at line 11.\
Now on go on discord , go to the settings , go to appearance , scroll to the bottom , and activate "Developer Mode",now go to the server where your bot added right click on the channel where you want the bot to post , click copy ID and finally , paste the ID in the parenthesis in line 99.\
Install requirements ("pip3 install -r requirements.txt")\
Now your bot should be available to use ! 

**Requirements:**\
Python3,Windows

**Compiling to exe (optional):**\
If you want to compile the bot to exe you can use PyInstaller.\
Inside the directory of the bot execute "PyInstaller --onefile --noconsole DiscordRAT.py" or "python3 -m PyInstaller --onefile --noconsole DiscordRAT.py"\
If an error occured during compiling try to import the discord module "PyInstaller --onefile --noconsole --hidden-import=discord DiscordRAT.py"

