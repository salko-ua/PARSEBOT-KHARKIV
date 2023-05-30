from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text

from handlers.parser import get_data


# ===========================start============================
async def start(message: types.Message):
    await message.answer(
        f"Вітаю {message.from_user.full_name}! 👏\nЦей бот призначений для швидкого парсингу\nі створення постів у telegram з olx\nПриємного користування 😁"
    )


# ===========================Посилання============================
async def main(message: types.Message):
    try:
        await get_data(message)
    except:
        await message.answer(
            "Виникла помилка ❌\nСторінку не було запарсено",
            reply_markup=types.ReplyKeyboardRemove(),
        )


# ===========================Всі повідомлення============================
async def all_message(message: types.Message):
    await message.answer(
        "🔴 Вибачте, але мені потрібне тільке\nпосилання на сторінку olx.ua з нерухомістю.\nтакого типу https://www.olx.ua/....",
        disable_web_page_preview=True,
    )


# ===========================реєстратор============================
def register_handler_main(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(
        main, Text(ignore_case=True, startswith="https://www.olx.ua/")
    )
    dp.register_message_handler(all_message)
