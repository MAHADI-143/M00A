import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from cold64 import mahadi
 
        mahadi()
 
 
 
elif bit == "32bit":
 
        from old32 import bye
 
 
        bye()
 
 
