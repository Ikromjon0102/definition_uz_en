from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tarjima", callback_data='translate'),
            # InlineKeyboardButton(text="Speech in English", callback_data='speech'),
        ]
    ]
)