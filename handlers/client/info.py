from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardRemove

from keboards.client import client_keyboard

from states.states import CommentsFSMAdmin

from aiogram.dispatcher import FSMContext

from db import sqlite_db

from bot import bot


async def start_command(message: Message):
    await message.answer('Choose your next option', reply_markup=client_keyboard)


async def get_address(message: Message):
    await message.answer('Ибраимова 103')


async def get_itemss_list(message: Message):
    for obj in sqlite_db.cursor.execute('SELECT * FROM item').fetchall():
            await bot.send_photo(message.from_user.id, obj[2], f"name: {obj[1]}\n category: {obj[4]}\n price: {obj[3]}")



async def leave_comment(message: Message):
    await CommentsFSMAdmin.grade.set()
    await message.answer('Send grade(from one to five)')


async def add_grade(message: Message, state: FSMContext):
    if int(message.text) > 5:
        async with state.proxy() as data:
            data['grade'] = 5
    elif int(message.text) < 5:
        async with state.proxy() as data:
            data['grade'] = 0
    elif int(message.text) == 5:
        async with state.proxy() as data:
            data['grade'] = 5
    await CommentsFSMAdmin.next()
    await message.answer('write text for your comment')



async def comment_text(message: Message, state: FSMContext):    
    async with state.proxy() as data:
        data['text'] = message.text
    await sqlite_db.sql_add_command(state, 'comments')
    await state.finish()
    await message.answer('Готово')




def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(get_address, commands=['address'])
    dp.register_message_handler(get_itemss_list, commands=['items'])
    dp.register_message_handler(leave_comment, commands=['comment'])
    dp.register_message_handler(add_grade, state=CommentsFSMAdmin.grade)
    dp.register_message_handler(comment_text, state=CommentsFSMAdmin.text)