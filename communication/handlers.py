#coding:utf-8
import socket
from tornado.websocket import WebSocketHandler

class MainHandler(WebSocketHandler):

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        msg = "Mensagem recebida {}".format(message)
        print(msg)
        if message in ['olá','ola', 'Ola', 'Olá']:
            self.write_message(
                u"Ola eu sou o bot smart! Como posso ajuda-lo"
            )
        else:
            self.write_message(
                u"Não consegui entender o que você escreve: " + message
            )

    def on_close(self):
        print("WebSocket closed")
