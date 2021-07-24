import telebot
import my_infos

token = my_infos.token
class Method():
    """Tentanto criar o método do meu jeito"""
    def __init__(self):
        self.token= my_infos.token
        self.apitelegram = f"https://api.telegram.org/bot{self.token}"
        self.headers = {'content-type': 'application/json', 'Cache-Control': 'no-cache'}
        @staticmethod
