from aiogram import types
from aiogram.types import File

from loader import dp, bot
from keyboard.inline.choice_buttons import main_menu, exit_panel
from models.sqlite_db import take_file


# --------- Приветственное сообщение при старте ----------- #
@dp.message_handler(commands=['start'])
async def welcome_massage(message: types.Message):

    photo = await take_file(name='Главная')

    await bot.send_photo(chat_id=message.chat.id, photo=photo,
                               caption='<b>Привет</b>!\n'
                                       f'Я бот-помощник Пензенского колледжа архитектуры и строительста\n \n'
                                       f'Выберите из следующих пунктов или введите команду /help',
                         reply_markup=main_menu)


# --------- Сообщение на команду /help --------- #
@dp.message_handler(commands=['help'])
async def help_massage(message: types.Message):
    await message.answer("Список команд:\n \n"
                         "/start - Приветствие\n"
                         "/help - Справка\n"
                         "/help_admin - Cправка для администрации",
                         reply_markup=exit_panel)



