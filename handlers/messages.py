import logging

from aiogram import Router, F
from aiogram.filters import Command, CommandObject, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from dependency_injector.wiring import Provide, inject
from pyowm.commons.exceptions import NotFoundError
from pyowm.weatherapi25.weather_manager import WeatherManager

from containers import WeatherManagerContainer
from db import User
from keyboards.weather_keyboard import get_weather_keyboard
from middlewares import UserMessageMiddleware

from messages.ru import *
from services.types import SetCityState

from datetime import datetime

router = Router()
router.message.middleware(UserMessageMiddleware())


@router.message(Command("start"))
async def start_command_message(message: Message, command: CommandObject, user: User):
    await message.answer(hello_message, reply_markup=get_weather_keyboard())


@router.message(StateFilter(None), Command("city"))
async def city_command_message(message: Message, user: User, state: FSMContext):
    city = user.city
    if city is None:
        await message.answer(enter_city_message)
    else:
        await message.answer(enter_city_exist_message.format(city=city))
    await state.set_state(SetCityState.ENTERING_CITY)


@router.message(StateFilter(SetCityState.ENTERING_CITY))
@inject
async def city_message(message: Message, user: User, state: FSMContext,
                       weather_manager: WeatherManager = Provide[WeatherManagerContainer.manager]):
    city_raw = message.text
    try:
        test_weather = weather_manager.weather_at_place(city_raw)
    except NotFoundError as exc:
        logging.warning(f"User's city {city_raw} not found.")
        await message.answer(city_not_found.format(city=city_raw))
        return

    city = test_weather.location.name

    user.city = city
    user.save()

    await state.clear()

    await message.answer(city_set_message.format(city=city))


@router.message(F.text.lower() == weather_button.lower())
@inject
async def weather_message(message: Message, user: User,
                          weather_manager: WeatherManager = Provide[WeatherManagerContainer.manager]):
    if user.city is None:
        await message.answer(city_not_set)
        return

    weather = weather_manager.weather_at_place(user.city).weather
    winds_directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "CЗ"]

    wind = weather.wind()
    time = datetime.fromtimestamp(datetime.today().timestamp() + weather.utc_offset).strftime("%H:%M:%S")
    weather_data = {
        'city': user.city,
        'wind_speed': wind['speed'],
        'wind_direction': winds_directions[int(((wind['deg'] + 22.5) // 45) % 8)],
        'humidity': weather.humidity,
        'temperature_celsius': round(weather.temperature('celsius')['temp']),
        'clouds': weather.clouds,
        'time': time
    }

    await message.answer(city_weather_message.format(**weather_data))
