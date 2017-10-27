#coding: utf-8

def execute_test():
    fallback =  {
        'execute': True,
        'user:' 'teste'
    }
    print(fallback)
    return fallback

def send_sms():
    fallback =  {
        'sending': True,
        'msg': 'Os testes passaram com sucesso'
    }
    print(fallback)
    return fallback

def send_email():
    fallback = {
        'sending': True,
        'msg': 'Os testes passaram com sucesso'
    }
    print(fallback)
    return fallback
