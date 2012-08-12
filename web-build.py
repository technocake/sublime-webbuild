#!/usr/bin/env python
#coding: utf-8
import sys, re, os, string, webbrowser, subprocess

###		Web-build
###		Current version rsyncs a given folder localy with a given folder
###		On a remote host:  (LOCAL_DIR -->  REMOTE_HOST_URI).
###				
###		It does not care for the file being given to it on build.
###
###		When the sync is done, it opens a webbrowser to a given target url:
###		(REMOTE_WEB_URI).
###
############################################################################

REMOTE_HOST_URI = "technocake@marte.komsys.org:/var/www/boofrecords.no/"
REMOTE_WEB_URI = "http://boof.technocake.net/"
LOCAL_DIR = "/Users/technocake/boof/web/"

#Empty Skeleton, don't mind this block.
try:
	pass
except Exception as e:	print (""" Usage: web-build <file> """, e);	sys.exit(1)


#Copy to remote host (Rsync)
print subprocess.call("rsync -vaz %s %s" % (LOCAL_DIR,  REMOTE_HOST_URI), shell=True)

#Browse result
webbrowser.open(REMOTE_WEB_URI)
