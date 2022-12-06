from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN
import keyb as kb
import raspisanie

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.greet_kb)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!", reply_markup=kb.greet_kb)

@dp.message_handler()
async def cur_message(message: types.Message):
    mess = message.text
    if mess.lower() == 'расписание сегодня':
        await message.answer("Расписание уроков", reply_markup=kb.cur_kb)
    elif mess in raspisanie.classes:
        now = datetime.now()
        r = raspisanie.rasp[mess][datetime.weekday(now)]
        await message.answer(r, reply_markup=kb.back_kb)
    elif mess.lower() == 'расписание на неделю':
        await message.answer("Расписание на неделю", reply_markup=kb.rasp_kb)
    elif mess in raspisanie.classes_:
        global class_num
        class_num = mess.strip('_')
        await message.answer('День недели', reply_markup=kb.week_kb)
    elif mess in raspisanie.days:
        ind = raspisanie.days.index(mess)
        print(ind)
        r = raspisanie.rasp[class_num][ind]
        await message.answer(r, reply_markup=kb.week_kb)
    elif mess.lower() == 'назад':
        await message.answer("Главное меню", reply_markup=kb.greet_kb)


if __name__ == '__main__':
    executor.start_polling(dp)