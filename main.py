#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint
import time
import telebot
from library import *
from telebot.types import Message
from telebot import types

TOKEN = '1215247311:AAH83InopzWWRuY2AttJUhlkynmevAJJlxs'
textUser = ''
descriptions = []
names = []
values = []
functions = []
mas = []

bot = telebot.TeleBot(TOKEN)

def getText(message, text): 
	global textUser
	bot.send_message(message.from_user.id, text)
	bot.register_next_step_handler(message, handler_text)
	while True:
		if textUser != '':
			return textUser

def getClick(message: Message, cort, text): #Функция выводит кнопки и получаем результат
	global textUser #
	keyboard = types.InlineKeyboardMarkup() #Создаем место куда будем кидать наши кнопки
	for i in range(len(cort)): #
			keyboard.add(types.InlineKeyboardButton(text=cort[i], callback_data=cort[i])) #кидаем наши кнопки
	bot.send_message(message.from_user.id, text=text, reply_markup=keyboard) #отпарвляем их пользователю
	while True: #
		if textUser != '': #
			for i in range(len(cort)): #
				if cort[i] == textUser: #
					textUser = '' #
					return i #возвращаем индекс нашего выбранного объекта из списка

def run_code(message, select):
	option = getClick(message, ('Дефолтные значения', 'Мои значения'), 'Режим:')
	if option == 0:
		text = f'{names[select]}({values[select]})\n'
		text += str(eval(f'{names[select]}()\n'))
	elif option == 1:
		text = getText(message, f'Введи значения, например {values[select]}') + '\n'
		text += str(eval(f'{names[select]}()\n'))
	bot.send_message(message.from_user.id, text)

def show_code(message, select):
	text = f'{descriptions[select]}\n\n'
	for i in range(0, len(functions[select])):
		option = f'Вариант {i + 1}\n'
		text += f'{option if len(functions[select]) > 1 else ""}{functions[select][i][1:]}\n'
	bot.send_message(message.from_user.id, text.replace('  ', '__').replace('\t', '____'))
	option = getClick(message, ('Запустить алгоритм', 'Назад'), 'Что дальше?')
	if option == 0:
		run_code(message, select)

def favorites(message):
	pass

def menu(message):
	option = getClick(message, ['Алгоритмы', 'Помощь'], 'Меню')
	if option == 0:
		show_code(message, getClick(message, descriptions, 'Алгоритмы'))
	elif option == 1:
		with open('help.txt', 'r') as help:
			bot.send_message(message.from_user.id, help.read())

def handler_text(message):
	global textUser 
	textUser = message.text

@bot.callback_query_handler(func=lambda call: True)
def handler_click(call):
	global textUser 
	textUser = call.data 

@bot.message_handler(commands=['start'])
def start(message: Message):
	with open('algorithms.txt', 'r') as file:
		line = file.read()
	lines = line.split('_' * 20)
	for algorithm in lines:
		algorithm = algorithm.split('-*-')
		descriptions.append(algorithm[0].replace('\n', ''))
		names.append(algorithm[1].replace('\n', ''))
		values.append(algorithm[2].replace('\n', ''))
		functions.append([algorithm[i] for i in range(3, len(algorithm))])
	mas = [['список'], [str(i) for i in range(0, len(names))], [x + '(' for x in names], ['']]
	while True:
		menu(message)

@bot.message_handler(commands=['stop'])
def stop(message):
	pass

bot.polling()
