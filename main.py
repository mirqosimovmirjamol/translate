import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from create import create_db
from insert import insert_user, select_user

logging.basicConfig(level=logging.INFO)
from app import en_uz, uz_en,uz_ru,ru_uz,ru_en,en_ru

API_TOKEN = '7376983620:AAH6os0phKY_VGcQnNZT4lQeDkaZ7eJWa6U'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

d = {'language': 'en_uz'}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # print(message.from_user.id)
    create_db()
    try:
        insert_user(message.from_user.username, message.from_user.id)
    except:
        pass
    await message.answer(f'Assalomu alekum {message.from_user.full_name}')
    if d.get('language') == 'en_uz':
        await message.answer('Bot ENG -> UZ botni UZ -> ENG xolatiga olish uchun /uz_en')
    elif d.get('language') == 'uz_en':
        await message.answer('Bot UZ -> ENG botni ENG -> UZ xolatiga olish uchun /en_uz')


@dp.message_handler(commands=['uz_en'])
async def mirjamol(message: types.Message):
    await message.answer('Bot UZ -> ENG botni ENG -> UZ xolatiga olish uchun /en_uz')
    d.update({'language': 'uz_en'})


@dp.message_handler(commands=['en_uz'])
async def doniyor(message: types.Message):
    await message.answer('Bot ENG -> UZ botni UZ -> ENG xolatiga olish uchun /uz_en')
    d.update({'language': 'en_uz'})
    
@dp.message_handler(commands=['uz_ru'])
async def a(message: types.Message):
    await message.answer('Bot UZ -> ru botni RU -> UZ xolatiga olish uchun /ru_uz')
    d.update({'language': 'uz_ru'})
    
@dp.message_handler(commands=['ru_uz'])
async def s(message: types.Message):
    await message.answer('Bot ru -> uz botni UZ -> ru xolatiga olish uchun /uz_ru')
    d.update({'language': 'ru_uz'})

@dp.message_handler(commands=['ru_en'])
async def e(message: types.Message):
    await message.answer('Bot ru -> en botni en-> ru xolatiga olish uchun /en_ru  ')
    d.update({'language': 'ru_en'})
    
@dp.message_handler(commands=['en_ru'])
async def s(message: types.Message):
    await message.answer('Bot en -> ru botni en-> ru xolatiga olish uchun /ru_en')
    d.update({'language': 'ru_en'})


@dp.message_handler(text='admin')
async def admin(message: types.Message):
    if message.from_user.id == 1038185913:
        for i in select_user():
            await bot.send_message(i, 'Qovunlarga habar ketdi!')
    else:
        await message.answer("Siz qovunsiz!")


@dp.message_handler()
async def muhammadyusuf(message: types.Message):
    if d.get('language') == 'uz_en':
        await message.answer(uz_en(message.text))
    elif d.get('language') == 'en_uz':
        await message.answer(en_uz(message.text))
        
    elif d.get('language') == 'en_ru':
        await message.answer(en_ru(message.text))
    elif d.get('language') == 'ru_en':
        await message.answer(ru_en(message.text))
    elif d.get('language') == 'ru_uz':
        await message.answer(ru_uz(message.text))
    elif d.get('language') == 'uz_ru':
        await message.answer(uz_ru(message.text))
    


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)