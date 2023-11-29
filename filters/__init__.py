# from aiogram import Dispatcher
# from .is_admin import AdminFilter
from loader import dp
from filters.private_chat import IsPrivate


if __name__ == "filters":
    # dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)
