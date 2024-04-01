from aiogram import types, Dispatcher, Router, F
from aiogram.filters import Command

from app.keyboards.user_keyboards import *
from app.utils.text import text_data

router = Router()


@router.message(Command('start', 'catalog'))
async def commands_handler(message: types.Message) -> None:
    await message.answer(text_data['catalog'], reply_markup=main_keyboard())


@router.callback_query(F.data.startswith("main_"))
async def main_callback_handler(callback: types.CallbackQuery) -> None:
    subject = callback.data.split('_')[1]
    await callback.message.edit_text(text_data['main'],
                                     reply_markup=training_class_keyboard(subject))


@router.callback_query(F.data.startswith("training_class_"))
async def training_class_callback_handler(callback: types.CallbackQuery) -> None:
    elements = callback.data.split('_')
    training_class, part, subject = elements[2], elements[3], elements[4]
    await callback.message.edit_text(text_data['output_elements'],
                                     reply_markup=make_keyboard_topic(training_class, part, subject))


@router.callback_query(F.data.startswith("back_"))
async def back_callback_handler(callback: types.CallbackQuery) -> None:
    callback_data = [i for i in callback.data.split('_')]
    reverse = '_'.join(callback_data[1:-1])
    subject = callback_data[-1]

    if reverse == 'main':
        await callback.message.edit_text(text_data['catalog'], reply_markup=main_keyboard())
    elif reverse == 'training_class':
        await callback.message.edit_text(text_data['main'],
                                         reply_markup=training_class_keyboard(subject))


def register_user_handlers(dp: Dispatcher) -> None:
    dp.include_router(router)
