# -- coding: utf-8 --
import tornado.web

from handlers import MainHandler
from client_1 import Client1
from client_2 import Client2
from settings import static_path

def routers():
    return tornado.web.Application([
        (r'/$', MainHandler),
        (r'/client1/$', Client1),
        (r'/client2/$', Client2),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path})
    ])
