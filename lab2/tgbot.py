import telebot
import emoji
from telebot import types

bot = telebot.TeleBot('6618497519:AAEHGb3mQGpvfj8EBLBIUy62_EFU49i2bME')
def emojing(line):
    return str(emoji.emojize(line))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, emojing("Привет! :waving_hand: "))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() in ('привет', 'привет!', emojing("Привет! :waving_hand: ")):
        bot.send_message(message.from_user.id, emojing("Привет! :waving_hand: ")) 

bot.polling(none_stop=True, interval=0)
