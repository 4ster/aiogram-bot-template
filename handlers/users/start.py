from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsPrivate
from loader import dp


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    args = message.get_args()
    await message.answer(f"Ты находишься в личной переписке/nТы нажал на старт и передал {args}")
