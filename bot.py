import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command

API_TOKEN = "8595486566:AAEyXAoB8xFV5SOXcdWZ_rqHUMHeGm-KkUs"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Я твій перший бот!😉")

# /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Ось що я вмію:\n"
        "/start - привітання\n"
        "/help - довідка\n"
        "/about - про мене\n"
        "/menu - меню"
    )

# /about
@dp.message(Command("about"))
async def about_command(message: Message):
    await message.answer("Я створений на Python з бібліотекою Aiogram")

# /menu
@dp.message(Command("menu"))
async def show_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Привіт 👋"), KeyboardButton(text="Як справи? 😊")],
            [KeyboardButton(text="Анекдот 🤣")]
        ],
        resize_keyboard=True
    )
    await message.answer("Вибери опцію:", reply_markup=keyboard)

# КНОПКИ (окремі хендлери — це головний фікс)
@dp.message(F.text == "Привіт 👋")
async def hi_handler(message: Message):
    await message.answer("Привіт-привіт! 👋")

@dp.message(F.text == "Як справи? 😊")
async def how_are_you_handler(message: Message):
    await message.answer("Усе чудово! А в тебе?")

@dp.message(F.text == "Анекдот 🤣")
async def joke_handler(message: Message):
    await message.answer("Як називається кіт-програміст? — JavaMeow!")

# Якщо щось інше написали
@dp.message()
async def fallback(message: Message):
    await message.answer("Натисни одну з кнопок 😺")

# Запуск
async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
# КНОПКИ
@dp.message(F.text == "Привіт 👋")
async def hi_handler(message: Message):
    await message.answer("Привіт-привіт! 👋")

# Відповідь на фразу "як справи"
@dp.message(F.text.lower().contains("як справи?"))
async def hi_text_handler(message: Message):
    await message.answer("Дякую, нормально 😊")