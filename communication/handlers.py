#coding:utf-8
from aiohttp import ClientSession
import asyncio
import socket
import time
from tornado.websocket import WebSocketHandler
from learning import SAUDACAO, NAME

API_KEY = 'UqEkshJuXYjAYNklXJ'

class MainHandler(WebSocketHandler):

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        msg = "Mensagem recebida {}".format(message)
        print(msg)
        names = 'olá ola ola  boa noite Ola Olá oi tudo bem bom dia bom a tarde boa noite'
        if message in SAUDACAO:
            msgs = [
                u'Ola eu sou o bot smart! Tentaria adivinhar seu sexo dado o nome. Vamos brincar?',
                'Me diga seu nome'
            ]
            for msg in msgs:
                self.write_message(
                    msg
                )
                time.sleep(2)
        else:
            loop = asyncio.get_event_loop()
            future = asyncio.ensure_future(self.api_request(loop, message))
            result = loop.run_until_complete(future)
            result = result[0][0]
            print(result)
            msgs = self.message_fallback(result.get('accuracy'), result.get('gender'))
            for msg in msgs:
                self.write_message(msg)
                time.sleep(2)

    def on_close(self):
        print("WebSocket closed")

    def message_fallback(self, accuracy, gender):
        msg = 'essa foi {} você é {}'
        msg2 = 'Deixa eu pensar...'
        msg4 = 'mas acredito que você sejá {}'
        msg3 = ' Não tenho certeza, essa foi difícil pra mim, mas acredito que você seja: {}'
        if accuracy > 70 and gender is not 'unknown':
            if gender == 'female':
                return (msg2, msg.format('fácil', 'mulher'))
            return (msg2, msg.format('fácil', 'homem'))
        if (accuracy >=30 and accuracy <=70) and gender is not 'unknown':
            if gender == 'female':
                return (msg2, msg4.format('mulher'))
            return (msg2, msg4.format('homem'))
        else:
            if gender == 'female':
                return (msg2, msg3.format('mulher'))
            return (msg2, msg3.format('homem'))

    async def api_request(self, loop, nome):

        tasks = []

        async with ClientSession() as session:
            task = asyncio.ensure_future(
                        self.get_from_api(
                            session, nome
                        )
                    )
            tasks.append(task)
            return await asyncio.gather(*tasks)

    async def get_from_api(self, session, nome):
        url = 'https://gender-api.com/get?key={}&name={}&country_id=br'
        result = []
        nome = nome.strip().replace(' ','&')
        for name in [nome]:
            url = url.format(API_KEY, name)
            print(url)
            async with session.get(url) as response:
                result.append(await response.json())
        return result
