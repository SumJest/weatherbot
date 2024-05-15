from aiogram.fsm.state import StatesGroup, State


class SetCityState(StatesGroup):
    ENTERING_CITY = State()
