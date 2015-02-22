#from gevent import socket
from gevent import monkey; monkey.patch_ssl()
import httplib
import urllib

class pushover(object):
    def __init__(self, app_token, user_key):
        self.app_token = app_token
        self.user_key = user_key

    def send(self, msg, priority=0):
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                urllib.urlencode({
                    'token': self.app_token,
                    'user': self.user_key,
                    'message': msg,
                    'priority': priority
                    }),
                { 'Content-type':
                        'application/x-www-form-urlencoded' })
