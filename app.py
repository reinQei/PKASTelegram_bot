from aiogram import executor
from handlers import dp
from loader import bot
from models.sqlite_db import db_start


async def on_startup(dp):
    print('Bot started')
    await db_start()


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
