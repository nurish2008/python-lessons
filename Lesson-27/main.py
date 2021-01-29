# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:49:40 2021

@author: Lesson-27
"""
from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "1607692892:AAG7EI2ux0NM5PJC_o1kzXKGbJ9WUZfHt3Q"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalamu Aleikom, Xush kelipsiz!!!"
    javob += "\nMatn kiriting: "
    bot.reply_to(message,javob )
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin (msg)
    bot.reply_to(message, javob(msg))
     
    
bot.polling()
    
    
   
            
# matn = input("Matn kiriting: ")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
