# 7891535798:AAGUtwq5OScPeG6pPP0j3IVx4EQDCA9SvC8 - bot ID
# !pip install pyTelegramBotAPI - скачивание API бота в Google Colab
# <tg-spoiler> - скрывает сообщения, но используется parse_mode='html'

import telebot

from telebot import types

isTest = False
version = 'v0.1.2 - создание парсера с Habr'

token = '7891535798:AAGUtwq5OScPeG6pPP0j3IVx4EQDCA9SvC8'

parsingBot = telebot.TeleBot(token)

@parsingBot.message_handler(commands=['start'])
def startBot(message):
    nameUser = message.from_user.first_name

    mess = f"Привет, {nameUser}!\n\nОткуда нужно получить новости!"
    if (isTest == True):
        mess += f"{version}"

    markup = types.InlineKeyboardMarkup()
    setNewsButton = types.InlineKeyboardButton("Получить новости", callback_data= "set_news")
    setHabrNewsButton = types.InlineKeyboardButton("Hadr", callback_data= "set_habr_news")
    markup.add(setNewsButton, setHabrNewsButton)
    parsingBot.send_message(message.chat.id, mess, parse_mode= "Markdown", reply_markup=markup)

@parsingBot.callback_query_handler(func=lambda call: True)
def messageBot(callback):
    if callback.data == "set_news":
        mess = "Функция в работе"
        parsingBot.send_message(callback.message.chat.id, mess, parse_mode="Markdown", reply_markup=None)
    
    if callback.data == "set_habr_news":
            mess = "Сделаем скоро"
            parsingBot.send_message(callback.message.chat.id, mess, parse_mode="Markdown", reply_markup = None)

parsingBot.infinity_polling()