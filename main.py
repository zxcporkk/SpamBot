from time import sleep

import telebot
import sqlite3
from dbConnector import*
from telebot import types

bot = telebot.TeleBot("")#your token

@bot.message_handler(commands=['start'])
def get_spam(message):
    db = SpamDB('base')
    spam = db.get_spam()

    while True:
        for cs in spam:
            bot.reply_to(message, cs)
            print(cs)
            sleep(0.2)

    db.close()


bot.polling()
