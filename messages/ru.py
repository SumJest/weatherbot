hello_message = """
Здравствуй, добро пожаловать в бота. 
Для начала настройте свой город с помощью команды /city
"""

enter_city_message = """
Отправьте мне город, в котором хотите смотреть погоду
"""

enter_city_exist_message = """
Ваш текущий город: {city}.

Отправьте мне новый город, в котором хотите смотреть погоду
"""

city_set_message = """
Ваш новый город: {city}.

Теперь вы сможете смотреть погоду в этом городе.
"""

city_not_found = """
Город {city} не найден.

Проверьте правильность введенного города.
"""

city_not_set = """
Вы ещё не установили город. 

Сделайте это, используя команду /city
"""

city_weather_message = """
Вот погода в городе {city}:

Ветер: {wind_speed} м/c {wind_direction}
Влажность: {humidity}%
Температура: {temperature_celsius} °C
Облачность: {clouds}%
Время: {time}
"""


weather_button = "Погода"