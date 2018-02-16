import os
import sys
import string
import random

#def runshell():
	#os.system("sh alntest.sh")

def keygen(size = 10, chars = string.ascii_lowercase + string.digits): #Generates 10-digit random key
    id = ''.join(random.choice(chars) for x in range(size))
    return id

def getkey():
	key = keygen()
	return key

key = getkey() #To hold on to single key for other functions


def mkkeydir():
	dirpath = "/project/home17/whb17/public_html/django-framework/mitosite/align/media/uploads/" + key
	os.mkdir(dirpath)
	os.chdir(dirpath)                   # set directory to given path to new directory
	os.environ['KEYDIR'] = dirpath      # set environment variable to be new directory
	os.system("echo $KEYDIR")			# echo path to command line
	os.system("source /project/home17/whb17/public_html/django-framework/mitosite/align/static/align/shscripts/time.sh")	
	# ^ run bash script. Full path given so accessable from any directory.
	return dirpath