from aiogram.utils.keyboard import ReplyKeyboardBuilder
from messages.ru import weather_button


def get_weather_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text=weather_button)
    return keyboard_builder.as_markup(resize_keyboard=True)
