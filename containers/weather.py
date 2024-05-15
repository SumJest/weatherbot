from dependency_injector import containers, providers
from pyowm.weatherapi25.weather_manager import WeatherManager
from settings import app_settings, weather_config


class WeatherManagerContainer(containers.DeclarativeContainer):
    manager: WeatherManager = providers.Singleton(WeatherManager,
                                                  API_key=app_settings.owm.token,
                                                  config=weather_config)