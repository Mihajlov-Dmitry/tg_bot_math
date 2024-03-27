from aiogram import types, Dispatcher, Router, F
from aiogram.filters import Command

from app.keyboards.user_keyboards import *
from app.utils import text

router = Router()


@router.message(Command('start'))
async def command_start_handler(message: types.Message) -> None:
    await message.answer(text['command_start'])


def register_user_handlers(dp: Dispatcher) -> None:
    dp.include_router(router)
