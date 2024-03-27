from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Кнопка 1', callback_data='ikb_1')]
    ])


