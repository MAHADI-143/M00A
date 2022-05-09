import os, platform
import time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations 🥰 Your Device Support Tools\033[1;37m")
    time.sleep(3.5) 
    from mahadi3 import Main
    Main()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Bro Your Mobile Not Support This Tools😡")
