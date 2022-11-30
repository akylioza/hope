from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

storage = MemoryStorage()


bot = Bot(token="5689191366:AAGx4OfPLBCOvYeWlnSLuVPU_FQlzMEG2LU")
disp = Dispatcher(bot, storage=storage)
