import gevent
from gevent import monkey; monkey.patch_ssl()
import httplib
import urllib
import time

class SparkFun(object):
    def __init__(self, server, publickey, privatekey, fields):
        self.server = server
        self.publickey = publickey
        self.privatekey = privatekey
        self.dorun = True
        self.fields = fields

    def updatezone(self, zone, state):
        self.fields[zone]['state'] = state

    def publish(self):
        #d = {}
        #for datum,field in zip(self.data, self.fields):
        #    d[field] = datum

        #print d
        data = {}
        for datum in self.fields.values():
            data[datum['field']] = datum.get('state', '')

        params = urllib.urlencode(data)
        print 'params:', params
        headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Connection': 'close',
                'Content-Length': len(params),
                'Phant-Private-Key': self.privatekey
                }

        c = httplib.HTTPSConnection(self.server)
        c.request('POST', '/input/' + self.publickey + '.txt', params, headers)
        r = c.getresponse()
        print r.status, r.reason

    def set(self, field, data):
        self.data[field] = data

