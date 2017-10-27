#coding:utf-8
import tornado.ioloop
import tornado.web
import asyncio
import socket
import msgpack

def socket_com():
    size = 512
    host = ''
    port = 9898
    #  family = Internet, type = stream socket means TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #  we have a socket, we need to bind to an IP address and port
    #  to have a place to listen on
    sock.bind((host, port))
    sock.listen(5)
    #  we can store information about the other end
    #  once we accept the connection attempt
    c, addr = sock.accept()
    data = c.recv(size)
    if data:
        f = open("storage.dat", '+w')
        print("connection from: ", addr[0])
        execution = msgpack.unpackb(data)
        for func in execution:
            func = func.decode('utf-8')
            rs = eval(func)
            f.write(addr[0])
            f.write(":")
            msg = msgpack.packb(rs)
            c.send(msg)
            f.write(str(rs))
            f.write("\n")
            c.settimeout(2)
        f.close()
    sock.close()


def execute_test():
    fallback = {'execute': True, 'user': 'teste'}
    print(fallback)
    return fallback

def send_sms():
    fallback =  {
        'sending': True,
        'kind': 'sms',
        'msg': 'Os testes passaram com sucesso'
    }
    print(fallback)
    return fallback

def send_email():
    fallback = {
        'send': True,
        'kind': 'email',
        'msg': 'Os testes foram executados normalmente'
    }
    print(fallback)
    return fallback


def main():
    from urls import routers
    from settings import template_path
    # socket = socket_com()
    app = routers()
    app.settings = dict(zip(['template_path'], [template_path]))
    app.listen(8888)
    print(app)
    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
