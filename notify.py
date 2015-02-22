import httplib
import urllib

class pushover(object):
    def __init__(self, app_token, user_key):
        self.app_token = app_token
        self.user_key = user_key

    def send(msg):
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                urllib.urlencode({
                    'token': self.app_token,
                    'user': self.user_key,
                    'message': msg,
                    }),
                { 'Content-type':
                        'application/x-www-form-urlencoded' })