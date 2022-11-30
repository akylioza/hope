from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardRemove

from keboards.client import client_keyboard

from bot import bot


async def start_command(message: Message):
    await message.answer('Choose your next option', reply_markup=client_keyboard)


async def get_address(message: Message):
    await message.answer('Ибраимова 103')


async def get_category_list(message: Message):
    await message.answer('1.бытовая техника /appliance\n 2.телефоны /phone\n 3.гаджеты /gadjet')



def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(get_address, commands=['address'])
    dp.register_message_handler(get_category_list, commands=['category_list'])