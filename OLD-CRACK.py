import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

 

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from old64 import fuck

        fuck()

 

elif bit == "32bit":

        from fuck0 import fuck

        fuck()





 
