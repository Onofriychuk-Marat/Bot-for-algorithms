# -*- coding: utf-8 -*-
# !/usr/bin/env python3.7
import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from library import *
import telebot
from telebot.types import Message

descriptions = []
names = []
values = []
functions = []
mas = []

try:
    token_for_vk = 'ff7d0303d573f8dfe0a3b9eb38e6fb98f9597af9904b42d5f55546f81d705daa81ef2895090a32c6b1e51'
    vk = vk_api.VkApi(token=token_for_vk)
    vk._auth_token()
    vk.get_api()
    long_poll = VkBotLongPoll(vk, 194049127)

    TOKEN = '1215247311:AAH83InopzWWRuY2AttJUhlkynmevAJJlxs'
    bot = telebot.TeleBot(TOKEN)
except Exception:
    print('Error')


def send_message(id_user, message_send, type_send):
    if type_send == 'vk':
        vk.method("messages.send",
                  {"peer_id": id_user, "message": message_send, "random_id": 0})
    elif type_send == 'world':
        print(message_send)


def brain(param):  # dict(peer_id, from_id, text, type)
    command = [show_list, show_code, run_code, info]
    for i in range(0, len(mas)):
        for k in mas[i]:
            if k in param['text'].lower() or k == param['text'].lower():
                command[i](param)
                return


def connect(type):
    try:
        if type == 'telegram':
            for event in long_poll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    param = dict(peer_id=event.object.peer_id, from_id=event.object.from_id, text=event.object.text,
                                 type='vk')
                    brain(param)
        elif type == 'world':
            text = input('>>> ')
            param = dict(peer_id=0, from_id=0, text=text, type='world')
            brain(param)
    except Exception as error:
        send_message(param['from_id'], error, param['type'])


@bot.message_handler(func=lambda message: True)
def connect_telegram(message: Message):
    bot.send_message()


def show_list(param):
    message = 'Алгоритмы:\n'
    for i in range(0, len(descriptions)):
        message += f'    {i + 1}) {descriptions[i]}\n'
    message = message[:-1]
    send_message(param['peer_id'], message, param['type'])


def show_code(param):
    select = int(param['text']) - 1
    message = f'{descriptions[select]}\n\n'
    for i in range(0, len(functions[select])):
        option = f'Вариант {i + 1}\n'
        message += f'{option if len(functions[select]) > 1 else ""}{functions[select][i][1:]}\n'
    send_message(param['peer_id'], message[:-1].replace('  ', '__').replace('\t', '____'), param['type'])


def run_code(param):
    for i in range(0, len(names)):
        if names[i] + '(' in param['text']:
            code = i
            value = param['text'].split(names[i] + '(')[1].split(')')[0].replace(' ', '')
    if len(value) == 0:
        message = f'{names[code]}({values[code]})\n'
        message += str(eval(f'{names[code]}()\n'))
    else:
        message = f'{param["text"]}\n'
        message += str(eval(message))
    send_message(param['peer_id'], message, param['type'])


def info(param):
    message = 'Команды:\n' \
              '1) Список\n' \
              '2) Алгоритм 1(Пример запуска алгоритма из списка)\n' \
              '3) gcd(100, 30)/gcd()(Пример вызова алгоритма Евклида)'
    send_message(param['peer_id'], message, param['type'])


def start(type):
    if type == 'telegram':
        bot.polling()
    else:
        while True:
            connect(type)


def init():
    global mas
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


init()
start('world')
