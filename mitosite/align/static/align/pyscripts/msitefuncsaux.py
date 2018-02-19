import os
import sys
import subprocess

from mitositefuncs import *

dirpath=mkkeydir()                  # Create directory and get path to said directory
os.chdir(dirpath)                   # set directory to given path to new directory
os.environ['KEYDIR'] = dirpath      # set environment variable to be new directory
os.system("echo $KEYDIR")			# echo path to command line
os.system("source /project/home17/whb17/public_html/django-framework/mitosite/align/static/align/shscripts/time.sh")	# run bash script. Full path given so accessable from any directory.