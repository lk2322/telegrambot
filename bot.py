import sqlite3
import telebot
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('API_KEY')
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda m: True)
def history(message):
    bot.reply_to(message, message.from_user.id)
    bot.reply_to(message, message.from_user.first_name)


bot.polling()