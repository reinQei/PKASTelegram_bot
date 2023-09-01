from aiogram.types import CallbackQuery

from keyboard.inline.callback_data import callback_panel
from keyboard.inline.choice_buttons import exit_panel
from loader import dp
from models.sqlite_db import take_date


@dp.callback_query_handler(callback_panel.filter(item_name="back_del"))
async def back_del(call: CallbackQuery):
    await call.message.delete()


@dp.callback_query_handler(callback_panel.filter(item_name="more"))
async def more_info(call: CallbackQuery):
    sobinova = await take_date(adres='Собинова')
    naberejnaya = await take_date(adres='Набережная')

    await call.message.answer(f'<b>День открытых дверей</b>\n \n'
                              f'Дни открытых дверей в Пензенском колледже архитектуры '
                              f'и строительства позволяют познакомиться с нашими специальностями '
                              f'и профессиями, правилами приема в учебное заведение, а также условиями обучения '
                              f'и организацией досуга в колледже\n \n'
                              f'<b>В программе мероприятия:</b>\n \n'
                              f'презентация специальностей,\n'
                              f'экскурсия по колледжу и учебным кабинетам и мастерским.\n \n'
                              f'Дни открытых дверей по адресу: г.Пенза, ул.Собинова, 7:\n'
                              f'{sobinova}\n \n'
                              f'Дни открытых дверей по адресу: г.Пенза, ул.Набережная р.Пензы, 3А:\n'
                              f'{naberejnaya}',
                              reply_markup=exit_panel)
