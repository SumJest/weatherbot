from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from db import User

# Мидлварь для создания пользователя в бд и передачи его в хэндлер
class UserMessageMiddleware(BaseMiddleware):
    def __init__(self, user_model: User = User):
        self.user_model = user_model

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        chat_id = event.from_user.id
        user, created = self.user_model.get_or_create(chat_id=chat_id)
        data["user"] = user
        data["is_new"] = created
        return await handler(event, data)
