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

#Example config file:
# filename: config-wb.py  !important

class config:
    REMOTE_HOST_URI = "technocake@marte.komsys.org:/srv/webmap/"
    REMOTE_WEB_URI = "http://webmap.technocake.net/lol"
    LOCAL_DIR = "/Users/technocake/django/webmap/"