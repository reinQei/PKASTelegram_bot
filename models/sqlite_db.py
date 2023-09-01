import sqlite3 as sq


# ------ создание таблиц при запуске бота ------ #
async def db_start():
    global db, cur

    db = sq.connect('E:\PythonProjects\Base.db')
    cur = db.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS files(name TEXT PRIMARY KEY, photo TEXT, description TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS open_doors(adres TEXT PRIMARY KEY, date TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS timetable_groups(groups TEXT PRIMARY KEY, photo TEXT)')
    db.commit()


# ------ добавление имени фото в бд "files" или добавление новой строки при отсутствии объекта ------ #
async def create_file(name):
    file = cur.execute('SELECT 1 FROM files WHERE name == "{key}"'.format(key=name)).fetchone()
    if not file:
        cur.execute("INSERT INTO files VALUES(?, ?, ?)", (name, '', ''))
        db.commit()


# ------ добавление остальных фрагментов в таблицу "files" по имени ------ #
async def edit_file(state, name):
    async with state.proxy() as data:
        cur.execute('UPDATE files SET photo = "{}", description = "{}" WHERE name == "{}"'.format(
            data['photo'], data['description'], name
        ))
        db.commit()


# ------ забираем фото из "files" по "name" ------ #
async def take_file(name):
    search = cur.execute('SELECT photo FROM files WHERE name == "{file_name}"'.format(file_name=name)).fetchone()
    db.commit()
    return search[0]


# ------ считываение адреса в бд "open_doors" или добавление новой строки при отсутствии объекта ------ #
async def create_open_doors_date(adres):
    data = cur.execute('SELECT 1 FROM open_doors WHERE adres == "{key}"'.format(key=adres)).fetchone()
    if not data:
        cur.execute('INSERT INTO open_doors VALUES (?, ?)', (adres, ''))
        db.commit()


# ------ добавление остальных фрагментов в таблицу "open_doors" по адресу ------ #
async def edit_open_doors_data(state, adres):
    async with state.proxy() as data:
        cur.execute('UPDATE open_doors SET date = "{}" WHERE adres == "{}"'.format(
            data['date'], adres
        ))
        db.commit()


# ------ забираем текст из "open_doors" по "adres" ------ #
async def take_date(adres):
    search = cur.execute('SELECT date FROM open_doors WHERE adres == "{adres_date}"'.format(adres_date=adres)).fetchone()
    db.commit()
    return search[0]


# ------ считываение имени группы в бд "timetable_groups" или добавление новой строки при отсутствии объекта ------ #
async def create_timetable_groups(group):
    file = cur.execute('SELECT 1 FROM timetable_groups WHERE groups == "{key}"'.format(key=group)).fetchone()
    if not file:
        cur.execute('INSERT INTO timetable_groups VALUES (?, ?)', (group, ''))
        db.commit()


# ------ добавление остальных фрагментов в таблицу "timetable_groups" по группы ------ #
async def edit_timetable_groups(state, group):
    async with state.proxy() as data:
        cur.execute('UPDATE timetable_groups SET photo == "{}" WHERE groups == "{}"'.format(
            data['photo'], group
        ))
        db.commit()


# ------ забираем фото из "timetable_groups" по "group" ------ #
async def take_timetable_groups(group):
    search = cur.execute('SELECT photo FROM timetable_groups WHERE groups == "{group_name}"'.format(
        group_name=group
    )).fetchone()
    db.commit()
    return search[0]


