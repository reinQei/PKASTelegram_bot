from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboard.inline.callback_data import callback_panel

# ------ кнопки главного меню ------ #
main_menu = InlineKeyboardMarkup(

    inline_keyboard=[
    
        [
            InlineKeyboardButton(text="Абитуриентам", callback_data=callback_panel.new(item_name="abitur")),
            InlineKeyboardButton(text="Родителям", callback_data="list:parents")
        ],
        [
            InlineKeyboardButton(text="Новости", url="https://t.me/pkaspenza"),
            InlineKeyboardButton(text="Студентам", callback_data="list:for_student")
        ],
        [
            InlineKeyboardButton(text="День открытых дверей", callback_data="list:more")
        ]

    ]

)


# ------ панель кнопок в разделе для абитуриентов ------ #
obitur_panel = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Экзамены", callback_data=callback_panel.new(item_name="exams")),
            InlineKeyboardButton(text="Направления", callback_data="list:competencies")
        ],
        [
            InlineKeyboardButton(text="Консультация по рисунку", url='https://pkas58.ru/article/consultpic')
        ],
        [
            InlineKeyboardButton(text="Контакты", callback_data="list:contacts")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)


# ------ 1 страница с пенлями кнопок в пункте направления подготовки ------ #
ways_panel_page_1 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Управление многоквартирным\nдомом", callback_data="list:build_and_use_apartments")
        ],
        [
            InlineKeyboardButton(text="Строительство зданий", callback_data="list:build_and_use_house")
        ],
        [
            InlineKeyboardButton(text="Строительсво дорог", callback_data="list:build_and_use_roads")
        ],
        [
            InlineKeyboardButton(text="Архитектура", callback_data="list:architechture")
        ],
        [
            InlineKeyboardButton(text="Прикладная инф.", callback_data="list:technician_coder"),
            InlineKeyboardButton(text="Информ. системы", callback_data="list:inform_system_and_codding")
        ],
        [

        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del'),
            InlineKeyboardButton(text="Вперёд", callback_data="list:next_page_1")
        ]

    ]

)


# ------ 2 страница с пенлями кнопок в пункте направления подготовки ------ #
ways_panel_page_2 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Сварочное производство", callback_data="list:weld")
        ],
        [
            InlineKeyboardButton(text="Парковое строительство", callback_data="list:park_build")
        ],
        [
            InlineKeyboardButton(text="Мастер-отделочник", callback_data="list:master_finisher_build"),
            InlineKeyboardButton(text="Ремонт ЖКХ систем", callback_data="list:JKH_system")
        ],
        [
            InlineKeyboardButton(text="Реклама", callback_data="list:advert"),
            InlineKeyboardButton(text="Сварщик", callback_data="list:welder")
        ],
        [
            InlineKeyboardButton(text="Графический дизайнер", callback_data="list:gr_dsgn")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]
    ]

)


# ------ панель с кнопкой с удалением нынешнего сообщения ------ #
exit_panel = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)

# ------ панель с кнопками в главном меню пункта родителей ------ #
parents_panel = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Адрес", callback_data="list:adress"),
            InlineKeyboardButton(text="Общежитие", callback_data="list:dormitory")
        ],
        [
            InlineKeyboardButton(text="Плат. услуги", url="https://pkas58.ru/article/dogovor"),
            InlineKeyboardButton(text="Трудоустройство", callback_data="list:employment")
        ],
        [
            InlineKeyboardButton(text="Партнёры", callback_data="list:partners")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="list:back_del")
        ]

    ]

)

adres_panel = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del'),
            InlineKeyboardButton(text="Вперёд", callback_data="list:adres2")
        ]

    ]

)

partners_way = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Архитектура", callback_data='list:arcetech_part'),
            InlineKeyboardButton(text="Садово-парк.", callback_data='list:park_part')
        ],
        [
            InlineKeyboardButton(text="Сварочное дело", callback_data='list:welding_part'),
            InlineKeyboardButton(text="Реклама", callback_data='list:advert_part')
        ],
        [
            InlineKeyboardButton(text="Информатика", callback_data='list:inform_part')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]
)

student_ways = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text='Набережная', callback_data='list:ttnaberejnaya'),
            InlineKeyboardButton(text='Собинова', callback_data='list:ttsobinova')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)


naberejnaya_timetable_courses = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text='1 Курс', callback_data='list:first_nn_timetable'),
            InlineKeyboardButton(text='2 Курс', callback_data='list:second_nn_timetable')
        ],
        [
            InlineKeyboardButton(text='3 Курс', callback_data='list:third_nn_timetable'),
            InlineKeyboardButton(text='4 Курс', callback_data='list:fourth_nn_timetable')
        ],
        [
            InlineKeyboardButton(text='5 Курс', callback_data='list:fifth_nn_timetable')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]
)

naberejnaya_timetable_first_courses_page2 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Далее", callback_data='list:ttfnnpage2')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)

naberejnaya_timetable_first_courses_page3 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Далее", callback_data='list:ttfnnpage3')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)

naberejnaya_timetable_second_courses_page2 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Далее", callback_data='list:ttsnnpage2')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)

naberejnaya_timetable_second_courses_page3 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Далее", callback_data='list:ttsnnpage3')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)


naberejnaya_timetable_third_courses_page2 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Далее", callback_data='list:tttnnpage2')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)

naberejnaya_timetable_third_courses_page3 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Далее", callback_data='list:tttnnpage3')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)

naberejnaya_timetable_fourth_courses_page2 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Далее", callback_data='list:ttfonnpage2')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)

naberejnaya_timetable_fourth_courses_page3 = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text="Далее", callback_data='list:ttfonnpage3')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]

)

sobinova_timetable_courses = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(text='1 Курс', callback_data='list:first_sn_timetable'),
            InlineKeyboardButton(text='2 Курс', callback_data='list:second_sn_timetable')
        ],
        [
            InlineKeyboardButton(text='3 Курс', callback_data='list:third_sn_timetable'),
            InlineKeyboardButton(text='4 Курс', callback_data='list:fourth_sn_timetable')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='list:back_del')
        ]

    ]
)
