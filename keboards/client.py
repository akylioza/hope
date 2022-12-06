from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton
)


b1 = KeyboardButton('/address')
b2 = KeyboardButton('/items')
b3 = KeyboardButton('/comment')



client_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

client_keyboard.add(b1).insert(b2)
client_keyboard.add(b3)
