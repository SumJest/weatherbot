import asyncio
import logging

from aiogram import Bot, Dispatcher

from containers import weather_container

from handlers.messages import router as commands_router
from settings import app_settings, storage_backend

logging.basicConfig(level='INFO')

bot = Bot(token=app_settings.telegram.token)
dp = Dispatcher(storage=storage_backend)


#
# @inject
# def get_weather(city: str,
#                 weather_manager: WeatherManager = Provide[WeatherManagerContainer.manager]):
#     weather = weather_manager.weather_at_place(city).weather
#
#     print(weather.wind()['speed'])
#     print(weather.humidity)
#     print(weather.temperature('celsius')['temp'])
#     print(weather.clouds)

async def main():
    dp.include_routers(commands_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


weather_container.wire(["handlers.messages"])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ex:
        pass



# print(get_weather('Челябинск'))
