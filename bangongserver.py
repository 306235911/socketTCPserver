from SocketServer import (TCPServer as TCP , StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST , PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:' , self.client_address
        while True:
            line = self.rfile.readline()
            if line:
                self.wfile.write('[%s] %s' % (ctime(), line))
            data = raw_input('> ')
            if data:
                self.wfile.write(data)

            
tcpServ = TCP(ADDR , MyRequestHandler, bind_and_activate=True)
print 'waiting for connention...'
tcpServ.serve_forever()