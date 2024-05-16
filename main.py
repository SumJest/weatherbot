import asyncio
import logging
from aiogram import Bot, Dispatcher

from containers import weather_container

from handlers.messages import router as messages_router
from settings import app_settings, storage_backend

# Настраиваем логирование
logging.basicConfig(level='INFO')

# Инициализируем бота и диспетчера
bot = Bot(token=app_settings.telegram.token)
dp = Dispatcher(storage=storage_backend)


# Точка входа в приложение
async def main():
    # Включаем роутер с хэндлерами сообщений
    dp.include_routers(messages_router)

    # Чистим обновления
    await bot.delete_webhook(drop_pending_updates=True)
    # Запускаем лонг поллинг
    await dp.start_polling(bot)

# Связываем модуль для инъекции зависимостей
weather_container.wire(["handlers.messages"])

if __name__ == "__main__":
    try:
        # Запускаем асинхронную таску
        asyncio.run(main())
    except KeyboardInterrupt as ex:
        pass
