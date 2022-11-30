from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from states.states import ItemFSMAdmin

from keboards.admin  import item_keyboard

from bot import bot
from bot import disp

from db import sqlite_db

ID = None


async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(
        message.from_user.id, "choose action: ", reply_markup=item_keyboard
    )
    await message.delete()


async def create_item(message: types.Message):
    if message.from_user.id == ID:
        await ItemFSMAdmin.name.set()
        await message.answer('Send its name')
    await message.answer('You are not an admin')


async def set_item_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:    
        async with state.proxy() as data:
            data['name'] = message.text
        await ItemFSMAdmin.next()
        await message.answer('пришлите фото')


async def set_item_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await ItemFSMAdmin.next()
        await message.answer('Выберите цену')


async def set_item_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text
        await ItemFSMAdmin.next()
        await message.answer('Выберите категорию')


async def set_item_category(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:        
        async with state.proxy() as data:
            data['category'] = message.text

        await sqlite_db.sql_add_command(state, 'item')
        await state.finish()
        await message.answer('Готово')


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if message.from_user.id == ID:
        if current_state is None:
            return
        await state.finish()
        await message.answer("canceled")


async def get_items_list(message: types.Message):
    for obj in sqlite_db.cursor.execute('SELECT * FROM item').fetchall():
        await bot.send_photo(ID, obj[1], f"name: {obj[0]}\n category: {obj[3]}\n price:{obj[2]}")


async def get_item_by_categorie(message: types.Message):
    if message.text in ['/phone', '/appliance', '/gadget']:
        query = f"SELECT * FROM student WHERE course = '{message.text[1:].capitalize()}'"
    else:
        await message.answer('wrong data')
        return

    for obj in sqlite_db.cursor.execute(query).fetchall():
        await bot.send_photo(ID, obj[1], f"name: {obj[0]}\nprice: {obj[2]}\ncategory: {obj[3]}")
    await bot.send_message(
        message.from_user.id, "choose action: ", reply_markup=item_keyboard)



def register_item_handler(disp: Dispatcher):
    disp.register_message_handler(create_item, commands=['create_item'], state=None)
    disp.register_message_handler(cancel_handler, state="*", commands=['cancel'])
    disp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    disp.register_message_handler(set_item_name, state=ItemFSMAdmin.name)
    disp.register_message_handler(set_item_photo, content_types=['photo'], state=ItemFSMAdmin.photo)
    disp.register_message_handler(set_item_price, state=ItemFSMAdmin.price)
    disp.register_message_handler(set_item_category, state=ItemFSMAdmin.category)
    disp.register_message_handler(get_items_list, commands=['items_list'])
    disp.register_message_handler(make_changes_command, commands=['admin'])
    disp.register_message_handler(get_item_by_categorie, commands=['/phone', '/appliance', '/gadget'])
