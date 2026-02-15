import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import questions

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(questions.router)

async def main():
    print("Бот запущений і готовий до роботи!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())