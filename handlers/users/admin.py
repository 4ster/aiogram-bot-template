from aiogram import types
from environs import Env

from filters import IsPrivate
from loader import dp

# FIXME: перенести отсюда
env = Env()
env.read_env()
admins = env.list("ADMINS")
print(admins)


@dp.message_handler(IsPrivate(), user_id=883513159, text="secret", state=None, content_types=types.ContentTypes.TEXT)
async def admin_chat_secret(message: types.Message):
    await message.answer(f"Ты находишься в административной части")
