# 1. Импорт библиотек
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message  # ловим все обновления этого типа
from aiogram.filters.command import (
    Command,
)  # обрабатываем команды /start, /help и другие


# 2. Инициализация объектов
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


# 3. Обработка команды start
@dp.message(Command(commands=["start"]))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = (
        f"Привет, {user_name}! \n"
        f"Отправь мне ФИО на кириллице, и я переведу его в латиницу."
    )
    logging.info(f"{user_name} {user_id} запустил бота")
    await bot.send_message(chat_id=user_id, text=text)


TRANSLIT_RULES = {
    "А": "A",
    "а": "a",
    "Б": "B",
    "б": "b",
    "В": "V",
    "в": "v",
    "Г": "G",
    "г": "g",
    "Д": "D",
    "д": "d",
    "Е": "E",
    "е": "e",
    "Ё": "E",
    "ё": "e",
    "Ж": "Zh",
    "ж": "zh",
    "З": "Z",
    "з": "z",
    "И": "I",
    "и": "i",
    "Й": "I",
    "й": "i",
    "К": "K",
    "к": "k",
    "Л": "L",
    "л": "l",
    "М": "M",
    "м": "m",
    "Н": "N",
    "н": "n",
    "О": "O",
    "о": "o",
    "П": "P",
    "п": "p",
    "Р": "R",
    "р": "r",
    "С": "S",
    "с": "s",
    "Т": "T",
    "т": "t",
    "У": "U",
    "у": "u",
    "Ф": "F",
    "ф": "f",
    "Х": "Kh",
    "х": "kh",
    "Ц": "Ts",
    "ц": "ts",
    "Ч": "Ch",
    "ч": "ch",
    "Ш": "Sh",
    "ш": "sh",
    "Щ": "Shch",
    "щ": "shch",
    "Ы": "Y",
    "ы": "y",
    "Э": "E",
    "э": "e",
    "Ю": "Iu",
    "ю": "iu",
    "Я": "Ia",
    "я": "ia",
    "Ь": "",
    "ь": "",
    "Ъ": "",
    "ъ": "",
}


# 4. Обработка всех сообщений
@dp.message()
async def send_FIO(message: Message):
    text = message.text.strip()
    if not text:
        await message.answer("Ошибка: пустое сообщение.")
        return

    words = text.split()
    result_words = []

    for word in words:
        normalized_word = word[0].upper() + word[1:].lower()

        translit_chars = []
        for ch in normalized_word:
            if "А" <= ch <= "я" or ch in "Ёё":
                translit_chars.append(TRANSLIT_RULES.get(ch, ch))
            else:
                translit_chars.append(ch)
        result_words.append("".join(translit_chars))

    final = " ".join(result_words)
    await message.answer(final)


# 5. Запуск процесса пуллинга
import asyncio


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
