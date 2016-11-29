# -*- coding: utf-8 -*-

import urllib
import requests
from flask import render_template, redirect, url_for, request

from tebot import app, bot
from config import TOKEN, API_URL


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    code = request.form.get('code')
    if not code:
        raise Exception("required code")

    response = requests.get(API_URL + TOKEN + '/getUpdates')

    if response.status_code != 200:
        raise Exception("Something went wrong!!")

    response_data = response.json()
    if not response_data['ok']:
        raise Exception('Result is false!')

    for item in response_data['result']:
        if item['message']['text'] == code:
            url = API_URL + TOKEN + "/sendMessage?"
            data = {
                'chat_id': item['message']['from']['id'],
                'text': 'Your id = %s\nYour first_name = %s\nYour username = %s' %
                        (item['message']['from']['id'],
                         item['message']['from']['first_name'].encode('utf-8'),
                         item['message']['from']['username'].encode('utf-8'))
            }
            response = requests.get(url + urllib.urlencode(data))
            if response.status_code != 200:
                raise Exception("Message don't send")
            break

    return render_template('index.html')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Wow! Hi. Can i help you?\nThere are available commands:"
                          "\n/id - Your id\n/username - Your username"
                          "\n/first_name - Your first name\n/last_name - Your last name")


@bot.message_handler(commands=['help'])
def send_help(message):
    print message
    bot.reply_to(message, "There are available commands:"
                          "\n/id - Your id\n/username - Your username"
                          "\n/first_name - Your first name\n/last_name - Your last name")


@bot.message_handler(commands=['id'])
def send_help(message):
    bot.reply_to(message, '%s' % message.from_user.id)


@bot.message_handler(commands=['username'])
def send_help(message):
    bot.reply_to(message, '%s' % message.from_user.username)


@bot.message_handler(commands=['first_name'])
def send_help(message):
    bot.reply_to(message, '%s' % message.from_user.first_name)


@bot.message_handler(commands=['last_name'])
def send_help(message):
    bot.reply_to(message, '%s' % message.from_user.last_name)
