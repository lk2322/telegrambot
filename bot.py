import database
import msg
import telebot
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('API_KEY')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['names'])
def info(message):
    print(message.text)
    try:
        usr_id = message.reply_to_message.from_user.id
    except AttributeError:
        bot.send_message(
            message.chat.id, 'Нужно ответить на сообщение для получение информации')
    else:
        history(message)
        names = database.give_names(usr_id)
        mesg = msg.names(names)
        bot.send_message(message.chat.id, mesg)


@bot.message_handler(func=lambda m: True)
def history(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if last_name is None:
        last_name = ''
    username = message.from_user.username
    usr_id = message.from_user.id
    database.add_name(usr_id, first_name, last_name, username)


bot.polling()
