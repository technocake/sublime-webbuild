#!/usr/bin/env python
#coding: utf-8
import sys, re, os, string, webbrowser, subprocess
###
###
###        Web-build
###        Current version rsyncs a given folder localy with a given folder
###        On a remote host:  (LOCAL_DIR -->  REMOTE_HOST_URI).
###
###        It does not care for the file being given to it on build.
###
###        When the sync is done, it opens a webbrowser to a given target url:
###        (REMOTE_WEB_URI).
###
###        @Author:    Technocake http://technocake.net
############################################################################


config = 'undefined'


def find_config():
    """ Searches for a config.wb.py file in the given sublimeproject directory """
    #Adding the project dir to path
    global config

    sys.path.append(sys.argv[1])
    print ("Building : %s" % sys.argv[1] )
    config = __import__('config-wb', fromlist=[]).config()


def build():
    """ Builds the webproject """
    global config


    ############################################################
    # Copy to remote host (Rsync)
    # 
    if not 'NO_SYNC' in dir(config):
        print subprocess.call( 
            "rsync -vaz --exclude %s %s %s " % ('*.pyc', config.LOCAL_DIR,  config.REMOTE_HOST_URI, ), 
            shell=True 
        ) 
    else:
        print "Not syncing config.NO_SYNC flag is set"


    ############################################################
    # Browse result
    # 
    webbrowser.open(config.REMOTE_WEB_URI)



if __name__ == '__main__':
    find_config()
    build()
