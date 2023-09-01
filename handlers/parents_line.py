from aiogram.types import CallbackQuery

from keyboard.inline.choice_buttons import parents_panel, exit_panel, adres_panel, partners_way
import keyboard.inline.callback_data
from loader import dp
from models.sqlite_db import take_file


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="parents"))
async def answer_for_parents(call: CallbackQuery):
    await call.message.answer("<b>Всё для родителей</b>\n \n"
                              "<b>Адрес</b> - маршруты как можно добраться до колледжа,\n"
                              "<b>Общежитие</b> - краткое описание и фото из общежития,\n \n"
                              "<b>Платные услуги</b> - ссылка на сайт колледжа с файлами"
                              " для дополнительных образовательных услуг,\n"
                              "<b>Трудоустройсвто</b> - краткие рузльтаты трудоустроуства выпускников,\n \n"
                              "<b>Социальные партнёры</b> - перечень партнёров колледжа.",
                              reply_markup=parents_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="adress"))
async def adres_info(call: CallbackQuery):
    photo = await take_file(name='Автобус')

    await call.message.answer_photo(photo=photo, caption="<b>Корпус на Набережной</b>\n \n"
                                                         "Из Октябрьского района:\n"
                                                         "  Автобус - 54;\n"
                                                         "  Маршрутка - 89, 77, 75, 68, 49, 29, 13, 6, 4;\n"
                                                         "  Троллейбус - 7.\n \n"
                                                         "Из Ленинского района:\n"
                                                         "  Автобус - 54;\n"
                                                         "  Маршрутка - 77, 10, 6, 4, 2a;\n"
                                                         "  Троллейбус - 7, 6.\n \n"
                                                         "Из Первомайского района:\n"
                                                         "  Автобус - 430, 414, 70;\n"
                                                         "  Маршрутка - 89, 85, 68, 43, 39, 33, 34, 4, 2а;\n"
                                                         "  Троллейбус - 2.\n \n"
                                                         "Из Железнодорожного района:\n"
                                                         "  Автобус - 101(Зар.), 103(ГПЗ), 149(Шуист);\n"
                                                         "  Маршрутка - Все доезжающие до фантанной плащади с "
                                                         "центрального рынка;\n"
                                                         "  Тролейбус - Все доезжающие до фантанной плащади с "
                                                         "центрального рынка;",
                                    reply_markup=adres_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="adres2"))
async def adres_info_2(call: CallbackQuery):
    photo = await take_file(name='Автобус')

    await call.message.answer_photo(photo=photo, caption="<b>Корпус на Собинова</b>\n \n"
                                                         "Из Октябрьского района:\n"
                                                         "  Автобус - 82c, 70, 66, 54;\n"
                                                         "  Маршрутка - 99, 77, 68, 63, 55, 39, 33, 31, 27, 18, 16, "
                                                         "6, 4, 2а;\n"
                                                         "  Тролейбус - 9, 6;\n \n"
                                                         "Из Ленинского района:\n"
                                                         "  Автобус - 130, 82с, 54;\n"
                                                         "  Маршрутка - 99, 63, 55, 39, 33, 6, 4;\n"
                                                         "  Тролейбус - 7.\n \n"
                                                         "Из Первомайского района:\n"
                                                         "  Автобус - 430, 414, 82с, 70, 54;\n"
                                                         "  Маршрутка - 99, 89, 43, 34, 6, 4, 2а;\n"
                                                         "  Тролейбус - 7, 2.\n \n"
                                                         "Из Железнодорожного района:\n"
                                                         "  Автобус - 101(Зар.), 103(ГПЗ), 82с;\n"
                                                         "  Маршрутка - 113, 112, 111, 99(без пересадки), "
                                                         "89, 68, 6, 4(с пересадкой в центре);\n"
                                                         "  Тролейбус - 7(с пересадкой в центре).",
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="dormitory"))
async def dormitory_info(call: CallbackQuery):
    photo = await take_file(name='Общежитие')

    await call.message.answer_photo(photo=photo, caption='<b>Колледж располагает</b> двумя благоустроенными общежитиями на 590 мест'
                                                         '(по адресу ул.набережная р.Пенза 3а, ул.Собинова 7).\n \n'
                                                         '<b>Все иногородние</b> студенты, нуждающиеся в жилье, обеспечиваются местами.\n \n'
                                                         '<b>Комнаты общежития</b> по ул.Набережная р.Пенза расположены по секциям и рассчитаны '
                                                         'на проживание 2-х и 3-х человек, в общежитии по '
                                                         'Собинова коридорного типа – все комнаты трехместные.\n \n'
                                                         '<b>В общежитиях</b> созданы социально–бытовые условия для проживания и организации досуга. '
                                                         'Помещения содержатся в соответствии с установленными санитарными правилами и нормами.',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="employment"))
async def results_info(call: CallbackQuery):
    photo = await take_file(name='Выпуск_табл')

    await call.message.answer_photo(photo=photo, caption="Анализ результатов выпусков за 3 года",
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="partners"))
async def inline_list_partners(call: CallbackQuery):
    await call.message.answer("Направления в которых у колледжа есть социальные партнёры:",
                              reply_markup=partners_way)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="arcetech_part"))
async def arcitechure_partners(call: CallbackQuery):
    photo = await take_file(name='Архитектура_парт')

    await call.message.answer_photo(photo=photo, caption='<b>Социальные партнёры</b> колледжа в направлении '
                                                         '"Архитектура и строительство"\n \n'
                                                         'ООО ПКФ «Термодом»,\n'
                                                         'ООО «КНАУФ ГИПС»,\n'
                                                         'ООО «Строй-Декор»,\n'
                                                         'И другие.\n \n'
                                                         'Больше можно узнать на официальном сайте колледжа',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="park_part"))
async def parks_partners(call: CallbackQuery):
    photo = await take_file(name='Сад_парк_парт')

    await call.message.answer_photo(photo=photo, caption='<b>Социальные партнёры</b> колледжа в направлении '
                                                         '«Садово-парковое и ландшафтное строительство»\n \n'
                                                         'Садовый центр «Ладшафт»,\n'
                                                         'ООО «Мастер-Бордюр»,\n'
                                                         'И Другие.\n \n'
                                                         'Больше можно узнать на официальном сайте колледжа',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="welding_part"))
async def welding_partners(call: CallbackQuery):
    photo = await take_file(name='Сварка_парт')

    await call.message.answer_photo(photo=photo, caption='<b>Социальные партнёры</b> колледжа в направлении '
                                                         '«Сварочное производство»\n \n'
                                                         'ОАО «Пензхиммаш»,\n'
                                                         'ОАО «Пензадизельмаш»,\n'
                                                         'ООО «Инженерно-технологический центр»,\n'
                                                         'И Другие.\n \n'
                                                         'Больше можно узнать на официальном сайте колледжа',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="advert_part"))
async def advertising_partners(call: CallbackQuery):
    photo = await take_file(name='Реклама_парт')

    await call.message.answer_photo(photo=photo, caption='<b>Социальные партнёры</b> колледжа в направлении '
                                                         '«Реклама»\n \n'
                                                         'ООО «Галерея-Медиа Пенза»,\n'
                                                         'Центр наружной рекламы «Арт-мастер»,\n'
                                                         'И Другие.\n \n'
                                                         'Больше можно узнать на официальном сайте колледжа',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="inform_part"))
async def information_technology_partners(call: CallbackQuery):
    photo = await take_file(name='Информ_парт')

    await call.message.answer_photo(photo=photo, caption='<b>Социальные партнёры</b> колледжа в направлении '
                                                         '«Прикладная информатика и Web-разработка»\n \n'
                                                         'ООО «Арсенал-Сервис»,\n'
                                                         'МБУ ДО «Центр технологического обучения»,\n'
                                                         'И Другие.\n'
                                                         'Больше можно узнать на официальном сайте колледжа',
                                    reply_markup=exit_panel)
