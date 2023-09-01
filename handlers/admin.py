from aiogram import types
from aiogram.dispatcher import FSMContext

from config import admins
from keyboard.inline.choice_buttons import exit_panel
from loader import dp

from handlers.states import AddFile, OpenDoors, TimeTabelGroups
from models.sqlite_db import create_file, edit_file, create_open_doors_date, edit_open_doors_data, \
    create_timetable_groups, edit_timetable_groups


@dp.message_handler(user_id=admins, commands=['help_admin'])
async def help_massage(message: types.Message):
    await message.answer("Список команд:\n \n"
                         "/start_add - панель загрузки фото\n"
                         "/help_admin - справочник команд администрации\n"
                         "/start_db_update_open_doors - обновление дат Дней откртых дверей\n"
                         "/start_add_timetables - обновление расписания постоянных занятий и звонков",
                         reply_markup=exit_panel)


# ------ адмнистративная функция обновления и добавления фото в базу данных ------ #
@dp.message_handler(user_id=admins, commands=['start_add'])
async def panel_add_start(message: types.Message):
    await message.answer('Добро пожаловать в административную панель добавления файлов')
    await message.answer('Введите название файла')
    await AddFile.name.set()


@dp.message_handler(user_id=admins, state=AddFile.name)
async def panel_add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await create_file(name=data['name'])
    await message.answer('Вы ввели имя файла')
    await message.answer('Отправьте фото(не файл)')
    await AddFile.next()


@dp.message_handler(user_id=admins, content_types=['photo'], state=AddFile.photo)
async def panel_add_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer('Введите краткое описание')
    await AddFile.next()


@dp.message_handler(user_id=admins, state=AddFile.description)
async def panel_add_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await message.answer_photo(photo=data['photo'],
                               caption=f"Имя файла: {data['name']}\n"
                                       f"Краткое описание: {data['description']}")
    await edit_file(state, name=data['name'])
    await message.answer('Файл добавлен в базу данных')
    await state.finish()


# ------ адмнистративная функция обновления дат дней открытых дверей в базу данных ------ #
@dp.message_handler(user_id=admins, commands=['start_db_update_open_doors'])
async def update_open_doors_date(message: types.Message):
    await message.answer('Добро пожаловать в административную панель обновления дат\n'
                         '<b>Дней открытых дверей</b>')
    await message.answer('Введите улицу (Набережная, Собинова):')
    await OpenDoors.adres.set()


@dp.message_handler(user_id=admins, state=OpenDoors.adres)
async def adres_add(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adres'] = message.text
    await create_open_doors_date(adres=data['adres'])
    await message.answer('Вы ввели адрес')
    await message.answer('Теперь введите даты дней открытых дверей через: ", "')
    await OpenDoors.next()


@dp.message_handler(user_id=admins, state=OpenDoors.date)
async def add_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer(f"Адрес: {data['adres']}\n"
                         f"Даты дней: {data['date']}")
    await edit_open_doors_data(state, adres=data['adres'])
    await message.answer('Информация обновлена')
    await state.finish()


# ------ адмнистративная функция обновления и добавления фото расписаний групп в базу данных ------ #
@dp.message_handler(user_id=admins, commands='start_add_timetables')
async def add_timetable_groups(message: types.Message):
    await message.answer('Добро пожаловать в административную панель обновления расписания\n'
                         '<b>Учебных занятий</b>')
    await message.answer('Ввведите отделение c номером курса\n для обновления расписания(Набережная_#_#, Собинова_#)\n'
                         'или "Звонок" - для обновления расписание звонков:')
    await TimeTabelGroups.group.set()


@dp.message_handler(user_id=admins, state=TimeTabelGroups.group)
async def add_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await create_timetable_groups(group=data['group'])
    await message.answer('Вы ввели отделение или "Звонок"')
    await message.answer('Отправьте фото(не файл)')
    await TimeTabelGroups.next()


@dp.message_handler(user_id=admins,content_types=['photo'], state=TimeTabelGroups.photo)
async def add_group_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await message.answer_photo(photo=data['photo'], caption=f"Отделение: {data['group']}")
    await edit_timetable_groups(state, group=data['group'])
    await message.answer('Информация обновлена')
    await state.finish()
