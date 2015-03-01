import gevent
from gevent import monkey; monkey.patch_ssl()
import httplib
import urllib

class SparkFun(object):
    def __init__(self, server, publickey, privatekey, fields):
        self.server = server
        sellf.publickey = publickey
        self.privatekey = privatekey
        self.fields = fields
        self.dorun = True

    def run(self):
        while self.dorun == True:
            gevent.sleep(10)

