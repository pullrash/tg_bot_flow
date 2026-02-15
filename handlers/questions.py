from aiogram import Router, types
from aiogram.filters import Command
from keyboards.for_questions import get_yes_no_kb, add_vacancia


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привіт {message.from_user.full_name}! Бажаєш записатися на послугу?",
        reply_markup=get_yes_no_kb()
    )

@router.message(lambda message: message.text == "так, хочу замовити")
async def proces_yes(message: types.Message):
    await message.answer("чудово тоді напишіть своє їм'я:",reply_markup=add_vacancia())
    