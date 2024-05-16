from aiogram.fsm.state import StatesGroup, State


# Набор состояний указания города
class SetCityState(StatesGroup):
    ENTERING_CITY = State()
