#coding:utf-8
from tornado.web import RequestHandler, asynchronous


class Client2(RequestHandler):

    @asynchronous
    def get(self, *args, **kwargs):
        items = {'name': 'Client2'}
        self.render('client2.html', title='Ola', items=items)
