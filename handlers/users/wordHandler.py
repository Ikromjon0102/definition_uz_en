from googletrans import Translator
import logging
from aiogram import types

from keyboards.inline.tarjimaKey import key
from utils.wordlookup import getdef
from loader import dp

translator = Translator()

@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 1:
        if lang == 'en':
            dest = 'uz'
            await message.answer(translator.translate(message.text, dest).text)
        else:
            await message.answer(translator.translate(message.text, dest='en').text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text
        lookup = getdef(word_id)
        if lookup:
            if lookup.get('audiouk'):# and lookup.get('audious'):
                await message.reply_voice(lookup['audiouk'], "United Kingdom version")
                # await message.reply_voice(lookup['audious'], "United Stated version")
            await message.answer(f"Word: <b>{word_id.title()}</b>\nDefinitions:\n"
                                 f"{lookup['definitions']}",reply_markup=key)
        else:
            await message.reply("Bunday so'z topilmadi")

@dp.callback_query_handler(text="translate")
async def tarjima(call: types.CallbackQuery):
    msg = call.message.text
    # logging.info(msg)
    # await call.message.delete()
    await call.message.answer(translator.translate(call.message.text,dest='uz').text)
    await call.answer(cache_time=60)


