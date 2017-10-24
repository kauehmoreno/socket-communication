#coding:utf-8
import tornado.ioloop
import tornado.web
import asyncio

def main():
    from urls import routers
    from settings import template_path

    app = routers()
    app.settings = dict(zip(['template_path'], [template_path]))
    app.listen(8888)
    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
