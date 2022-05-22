import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

 

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from pro64 import xmmx

        xmmx()

elif bit == "32bit":

        from old import main_apv

        main_apv()





 
