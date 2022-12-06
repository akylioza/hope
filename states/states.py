from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class ItemFSMAdmin(StatesGroup):
    name = State()
    photo = State()
    price = State()
    category = State()
 

class CategoryFSMAdmin(StatesGroup):
    name = State()


class CommentsFSMAdmin(StatesGroup):
    grade = State()
    text = State()
    