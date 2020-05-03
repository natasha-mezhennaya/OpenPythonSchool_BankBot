#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:37:09 2020

@author: natasha
"""

from telebot import types

def main_menu(bot, chat_id):
    main_menu_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    
    currency_button = types.KeyboardButton('Курсы валют')
    payments_button = types.KeyboardButton('Платежи')
    my_cards_button = types.KeyboardButton('Мои карты')
    new_card_button = types.KeyboardButton('Новая карта')    
    
    main_menu_buttons.add(currency_button, payments_button, my_cards_button, new_card_button)
    bot.send_message(chat_id, 'Выберите операцию', reply_markup=main_menu_buttons)


def payment_menu(bot, chat_id):
    payment_menu_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    mobile_payment = types.KeyboardButton('Мобильный телефон')
    internet_payment = types.KeyboardButton('Домашний интернет')
    main_menu_button = types.KeyboardButton('Главное меню')

    payment_menu_buttons.add(mobile_payment, internet_payment, main_menu_button)
    bot.send_message(chat_id, 'Выберите платеж', reply_markup=payment_menu_buttons)