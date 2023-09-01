from aiogram.types import CallbackQuery

import keyboard.inline.callback_data
from loader import dp
from keyboard.inline.choice_buttons import obitur_panel, exit_panel, ways_panel_page_1, ways_panel_page_2
from models.sqlite_db import take_file


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="abitur"))
async def answer_for_abiturients(call: CallbackQuery):
    await call.message.answer("<b>Перечень основных документов для поступления</b> \n"
                              "\n"
                              "Oригинал или ксерокопию документов:\n"
                              "- Удостоверение личность и гражданство\n"
                              "- Документ государственного образца об образовании\n"
                              "\n"
                              "- 4 фотографии(размер 3:4).\n \n"
                              "Баллы для поступления не ставяться заранее перед новым набором студентов. "
                              "Существуют быллы только за <b>прошлый год</b>",
                              reply_markup=obitur_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="contacts"))
async def contacts_info(call: CallbackQuery):
    await call.message.answer("<b>Контакты\n</b>Адреса и телефоны:\n \n"
                              "<b>ул. Набережная реки Пенза 3а</b>\n"
                              "     <b>-</b> Администрация: 8(8412)52-18-58,\n"
                              "     <b>-</b> Приемная комиссия: 89085303808\n \n"
                              "<b>ул. Собинова 7</b>\n"
                              "     <b>-</b> Администрация: 8(8412)43-44-86,\n"
                              "     <b>-</b> Приемная комиссия: 8(8412)43-44-94",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="exams"))
async def exams_for_abiturients(call: CallbackQuery):
    photo = await take_file(name='Экз_рисунок')

    await call.message.answer_photo(photo=photo,
                                    caption="Для поступления в ГАПОУ ПО ПКАС на специальности:\n"
                                            "\n"
                                            "- Архитектура\n"
                                            "- Реклама\n"
                                            "- Садово-парковое и ландшафтное строительство\n"
                                            "\n"
                                            "Необходимо пройти вступительное испытание по рисунку(пример работы на А3).",
                                    reply_markup=exit_panel
                                    )


# -------- первая стрница с направления подготовки студентов -------- #
@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="competencies"))
async def ways_competencies(call: CallbackQuery):
    await call.message.answer("<b>Направления подготовки</b>\nПеречень всех направлений обучения ГАПОУ ПО ПКАС\n \nстраница 1", reply_markup=ways_panel_page_1)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="architechture"))
async def architechture_info(call: CallbackQuery):
    await call.message.answer("<b>Архитектура \nCрок обучения</b>:\n"
                              "на базе 9 классов\n \n3 года 10 месяцев,\n"
                              "4 года 10 месяцев(углубленная поготовка).\n \n<b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Проектирование конструкций,\n<b>-</b> Расчёт конструкций,\n"
                              "<b>-</b> Разработка планов зданий,\n<b>-</b> Разработка планов фасадов,\n"
                              "<b>-</b> Рзаработка внутренних пространств.",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="build_and_use_house"))
async def build_and_use_house_info(call: CallbackQuery):
    await call.message.answer("<b>Строительство и эксплуатация зданий и сооружений \n"
                              "Cрок обучения</b>:"
                              "\nна базе 9 классов\n \n2 года 10 месяцев,\n3 года 10 месяцев,\n4 года 10 месяцев.\n \n"
                              "<b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Участие в проектировании гражданских и промышленных зданий,\n"
                              "<b>-</b> Разрабатка архитектурно-строительных чертежей "
                              "с помощью информационных технологий,\n"
                              "<b>-</b> Контролировать качество выполняемых работ.", reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="build_and_use_roads"))
async def build_and_use_roads_info(call: CallbackQuery):
    await call.message.answer("<b>Строительство и эксплуатация автомобильных дорого\nСрок обучения</b>:\n"
                              "на базе 9 классов\n \n"
                              "3 года 10 месяцев\n \n<b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Проектирование и реконструкция дорожных полотен, транспортных сооружений,\n"
                              "<b>-</b> Разработка новых методов работы с такими сооружениями,\n"
                              "<b>-</b> Организация и управление работой команды или подразделения, "
                              "соблюдение сроков выполнения обязательств перед заказчиками.",
                              reply_markup=exit_panel)


@dp.callback_query_handler(
    keyboard.inline.callback_data.callback_panel.filter(item_name="build_and_use_apartments"))
async def build_and_use_apartments_info(call: CallbackQuery):
    await call.message.answer("<b>Управление, эксплуатация и обслуживание многоквартирного дома\nСрок обучения</b>:\n"
                              "на базе 9 класса\n \n "
                              "3 года 10 месяцев\n \n<b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Управление многоквартирным домом,\n"
                              "<b>-</b> Обеспечивать и проводить работы по эксплуатации, "
                              "обслуживанию и ремонту общего имущества многоквартирного дома,\n"
                              "<b>-</b> Обеспечивать и проводить работы по санитарному содержанию, "
                              "безопасному проживанию и благоустройству общего имущества многоквартирного дома.",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="technician_coder"))
async def technician_coder_info(call: CallbackQuery):
    await call.message.answer("<b>Прикладная информатика(по отрослям)\nСрок обучения</b>:\nна базе 9 класса\n \n"
                              "3 года 10 месяцев\n \n<b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Создание стилевых образцов web-документов,\n"
                              "<b>-</b> Написание программной части и кода страницы,\n"
                              "<b>-</b> Создание интерактивных web-приложений,\n"
                              "<b>-</b> Создание и работа с приложениями для статической обработки.",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="inform_system_and_codding"))
async def inform_system_and_codding_info(call: CallbackQuery):
    await call.message.answer("<b>Информационные системы и программирование\nСрок обучения</b>:\nна базе 9 класса\n \n"
                              "3 года 10 месяцев\n \n<b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Анализ, проектирование и разработка сайтов для сети Интернет,\n"
                              "<b>-</b> Проектирование и разработка цифровых мультипликаций, изображений, "
                              "презентаций, игр, звуковых и видеоклипов и Интернет-приложений,\n"
                              "<b>-</b> Поддержка связи с сетевыми специалистами "
                              "по таким связанным с Интернет вопросами.",
                              reply_markup=exit_panel)


# -------- вторая стрница с направления подготовки студентов -------- #
@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="next_page_1"))
async def ways_competencies_page_2(call: CallbackQuery):
    await call.message.answer("<b>Направления подготовки</b>\nПеречень всех направлений обучения ГАПОУ ПО ПКАС\n \nстраница 2", reply_markup=ways_panel_page_2)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="weld"))
async def weld_info(call: CallbackQuery):
    await call.message.answer("<b>Сварочное производство\nСрок обучения</b>:\nна базе 9 класса\n \n"
                              "3 года 10 месяцев\n \n<b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> На основе предоставляемой документации правильно и "
                              "последовательно описывать технологию изготовления продукции\n"
                              "<b>-</b> Подобр режимов сварки,\n"
                              "<b>-</b> Подобрка оборудование, приспособления и оснастку.",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="park_build"))
async def park_build_info(call: CallbackQuery):
    await call.message.answer("<b>Садово-парковое и ландшафтное строительство\n"
                              "Срок обучения</b>:\nна базе 9 класса\n \n"
                              "3 года 10 месяцев\n \n<b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Производственно-технологическая - "
                              "ведение строительно-монтажных работ по проектам,\n"
                              "<b>-</b> Организационно-управленческая - планирование "
                              "и организация работы коллектива исполнителей, "
                              "выбор оптимальных решений, осуществление контроля качества работ,\n"
                              "<b>-</b> Эксплуатационная - контроль параметров эксплуатационной пригодности, "
                              "диагностика и организация ремонта конструкций.",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="advert"))
async def advertisings_info(call: CallbackQuery):
    await call.message.answer("<b>Реклама\n Срок обучения</b>:\nна базе 9 класса\n \n"
                              "3 года 10 месяцев\n \n <b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Разработка и создание дизайна рекламной продукции,\n"
                              "<b>-</b> Производство рекламной (аудио- и видео-визуальной) продукции,\n"
                              "<b>-</b> Организация и управление процессом изготовления рекламного продукта,\n"
                              "<b>-</b> Реализация комплексных рекламных проектов.",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="gr_dsgn"))
async def gr_designer_info(call: CallbackQuery):
    await call.message.answer("<b>Графисечкий\n Срок обучения</b>:\nна базе 9 класса\n \n"
                              "3 года 10 месяцев\n \n <b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Разработка полиграфии,\n"
                              "<b>-</b> Разработка интреактивного дизайна(сайты, интерфейсы),\n"
                              "<b>-</b> Разработка фирменого стиля компании,\n"
                              "<b>-</b> Разработка визуальных решений упоков продуктов.",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="master_finisher_build"))
async def master_finisher_build_info(call: CallbackQuery):
    await call.message.answer("<b>Мастер отделочных строительных и декоративных работ\nСрок обучения</b>:\nна базе 9 класса\n \n"
                              "2 года 10 месяцев\n \n<b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Подготовка (выравнивание) поверхностей и выполнение "
                              "работ по оштукатуриванию (штукатур),\n"
                              "<b>-</b> Приготовление растворов, разметка поверхностей под оштукатуривание и "
                              "облицовку плиткой и другими материалами (облицовщик),\n"
                              "<b>-</b> Выполнение окраски, оклейки, художественной отделки, "
                              "ремонт наружных и внутренних поверхностей здания (маляр).",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="JKH_system"))
async def jkh_system_info(call: CallbackQuery):
    await call.message.answer("<b>Мастер по ремонту и обслуживанию инженерных систем ЖКХ\nСрок обучения</b>:\nна базе 9 класса\n \n"
                              "2 года 10 месяцев\n \n <b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Ремонт конструкций в зданиях, оборудование и осветительные сети,\n"
                              "<b>-</b> Оснащение жизнеобеспечивающих систем зданий, конструкций и "
                              "сооружений из всевозможных материалов,\n"
                              "<b>-</b> Измерение параметров различных систем зданий,\n"
                              "<b>-</b> Эксплуатации инженерных сетей.",
                              reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="welder"))
async def welder_info(call: CallbackQuery):
    await call.message.answer("<b>Сварщик (ручной и частично механизированной сварки)\nСрок обучения</b>:\nна базе 9 класса\n \n"
                              "2 года 10 месяцев\n \n <b>Основные виды деятельности</b>:\n \n"
                              "<b>-</b> Обслуживания электросварочной техники,\n"
                              "<b>-</b> Сваривка элементов металлоконструкций, трубопроводы, детали машин и механизмов с помощью сварочного аппарата,\n"
                              "<b>-</b> Сборка заготовок (узлы) конструкций, "
                              "осуществляет их транспортировку в пределах рабочего места.",
                              reply_markup=exit_panel)