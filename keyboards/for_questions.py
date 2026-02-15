from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_yes_no_kb():
    buttons = [
        [KeyboardButton(text="так, хочу замовити"), KeyboardButton(text="ні, просто дивлюсь")]
    ]
    Keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return Keyboard


def add_vacancia():
    buttons = [
        [KeyboardButton(text="Надіслати вакансію"), KeyboardButton(text="")]
    ]
    Keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return Keyboard