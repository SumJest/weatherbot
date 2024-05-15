from aiogram.fsm.storage.memory import MemoryStorage
from pydantic import Field
from pydantic_settings import BaseSettings
from pyowm.commons.databoxes import SubscriptionType
from pyowm.commons.enums import SubscriptionTypeEnum


class OWMSettings(BaseSettings, env_prefix='owm_'):
    token: str = Field()


class TelegramSettings(BaseSettings, env_prefix='telegram_'):
    token: str = Field()


class Settings(BaseSettings):
    owm: OWMSettings = OWMSettings()
    telegram: TelegramSettings = TelegramSettings()


app_settings = Settings()
weather_config = {'subscription_type': SubscriptionTypeEnum.FREE,
                  'language': 'ru',
                  'connection': {'use_ssl': True,
                                 'verify_ssl_certs': True,
                                 'use_proxy': False,
                                 'timeout_secs': 5,
                                 'max_retries': None}
                  }

storage_backend = MemoryStorage()
