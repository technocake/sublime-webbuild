#!/usr/bin/env python
#coding: utf-8
import sys, re, os, string, webbrowser, subprocess

REMOTE_HOST_URI = "technocake@marte.komsys.org:/var/www/boofrecords.no/"
REMOTE_WEB_URI = "http://boof.technocake.net/"
LOCAL_DIR = "/Users/technocake/boof/web/"
try:
	pass
except Exception as e:	print (""" Usage: web-build <file> """, e);	sys.exit(1)

#Copy
print subprocess.call("rsync -vaz %s %s" % (LOCAL_DIR,  REMOTE_HOST_URI), shell=True)

print os.getcwd()
#Browse result
webbrowser.open(REMOTE_WEB_URI)
