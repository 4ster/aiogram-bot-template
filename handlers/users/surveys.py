from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Survey


@dp.message_handler(Command("survey"))
async def enter_survey(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1:\n\n"
                         "Вы часто занимаетесь бессмысленными делами?\n")

    await Survey.Q1.set()  # присваиваем пользователю состояние ответа на первый вопрос

    # await Survey.Q1.first() # еще можно так присвоить первое состояние

    @dp.message_handler(state=Survey.Q1)  # присваиваем обработчик, любое сообщение будет ответом на этот вопрос
    async def answer_q1(message: types.Message, state: FSMContext):
        answer = message.text
        await state.update_data(answer1=answer)  # вариант 1 сохранения состояния в машине

        # await state.update_data( # вариант 2 сохранения состояния в машине
        #     {
        #         "answer1": answer
        #     }
        # )

        # # вариант 3 сохранения состояния в машине - асинхронный генератор - сохраняет состояние при выходе из генератора
        # # сразу изменяет данные в стейте, не нужно делать await state.get_data, потом set_data ...
        # async with state.proxy() as data:
        #     data["answer1"] = answer

        await message.answer("Вопрос №2:\n\n"
                             "Ваша память ухудшилась?\n")
        # передаем пользователя в следущее состояние по списку
        await Survey.next()  # вариант 1
        # await Survey.Q2.set() # вариант 2
