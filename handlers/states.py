from aiogram.dispatcher.filters.state import StatesGroup, State


class AddFile(StatesGroup):
    name = State()
    photo = State()
    description = State()


class OpenDoors(StatesGroup):
    adres = State()
    date = State()


class TimeTabelGroups(StatesGroup):
    group = State()
    photo = State()



