from db import sqlite_db

from aiogram import executor

from bot import disp
from handlers.client import info
from handlers.admin import commands


async def on_startup(_):
    print('Bot has started')
    sqlite_db.sql_start()



info.register_client_handler(disp)
commands.register_item_handler(disp)


if "__main__" == __name__:
    executor.start_polling(disp, skip_updates=True, on_startup=on_startup)
