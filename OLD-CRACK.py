import os, sys, time
from time import sleep
try:
    __import__('uidd64').main_apv()
except Exception as e:
    exit(str(e))
 
