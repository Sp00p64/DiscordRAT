# DiscordRAT
Discord Remote Administration Tool fully written in Python3

This is a RAT controlled over Discord with 20 post exploitation modules.

Requirements:\
Python3,Windows

Setup Guide:\
You will first need to register a bot with the Discord developper portal and then add the bot to the server that you want
Once the bot is created copy the token of your bot and paste it at line 11
Install PyInstaller (optional) "pip install PyInstaller"   
Install discord python module ("pip install discord")\
Now your bot should be available to use ! 

Compiling to exe (optional):\
If you want to compile the bot to exe you can use PyInstaller.\
Inside the directory of the bot execute "PyInstaller --onefile --noconsole nameofthebot.py" or "python3 -m PyInstaller --onefile --noconsole nameofthebot.py"\
If compiling failed try to import the discord module "PyInstaller --onefile --noconsole --hidden-import=discord nameofthebot.py"

