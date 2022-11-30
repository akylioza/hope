from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton
)


b1 = KeyboardButton('/address')
b2 = KeyboardButton('/category_list')



client_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

client_keyboard.add(b1).insert(b2)
