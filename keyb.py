from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton


back_button = KeyboardButton('Назад')
back_kb =ReplyKeyboardMarkup(resize_keyboard=True).add(back_button)

button_hi = KeyboardButton('Новости')
button_cur = KeyboardButton('Расписание сегодня')
button_week = KeyboardButton('Расписание на неделю')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(button_hi, button_cur, button_week)

button_10A = KeyboardButton('10А')
button_10B = KeyboardButton('10Б')
button_10V = KeyboardButton('10В')
button_10G = KeyboardButton('10Г')

cur_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4).add(button_10A, button_10B, button_10V, button_10G, back_button)

button_10A_ = KeyboardButton('_10А_')
button_10B_ = KeyboardButton('_10Б_')
button_10V_ = KeyboardButton('_10В_')
button_10G_ = KeyboardButton('_10Г_')

rasp_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4).add(button_10A_, button_10B_, button_10V_, button_10G_, back_button)

days = ['пн', 'вт',' ср', 'чт', 'пт']

week_buttons = [KeyboardButton(x) for x in days]
week_kb =ReplyKeyboardMarkup(resize_keyboard=True, row_width=5).add(*week_buttons, back_button)

