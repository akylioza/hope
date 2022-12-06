from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton
)


sb_1 = KeyboardButton('/create_item') # student_button
sb_2 = KeyboardButton('/items_list')
sb_4 = KeyboardButton('/category_list')
sb_3 = KeyboardButton('/create_category')



item_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
item_keyboard.add(sb_1).insert(sb_2)
item_keyboard.add(sb_3).insert(sb_4)

