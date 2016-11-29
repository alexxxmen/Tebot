# -*- coding: utf-8 -*-

import telebot
import requests
import threading
from flask import Flask

from config import TOKEN

requests.packages.urllib3.disable_warnings()

app = Flask(__name__)

bot = telebot.TeleBot(TOKEN)


def polling():
    bot.polling(none_stop=False, interval=2)


t1_stop = threading.Event()
t1 = threading.Thread(target=polling)
t1.start()


import views