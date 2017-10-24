#coding:utf-8
from tornado.web import RequestHandler, asynchronous


class Client1(RequestHandler):

    @asynchronous
    def get(self, *args, **kwargs):
        items = {'name': 'Client1'}
        self.render('client.html', title='Ola', items=items)
