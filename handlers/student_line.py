import keyboard.inline.callback_data
from loader import dp

from aiogram.types import CallbackQuery

from keyboard.inline.callback_data import callback_panel
from keyboard.inline.choice_buttons import exit_panel, student_ways, naberejnaya_timetable_courses, \
    sobinova_timetable_courses, naberejnaya_timetable_first_courses_page2, naberejnaya_timetable_first_courses_page3, \
    naberejnaya_timetable_second_courses_page2, naberejnaya_timetable_second_courses_page3, \
    naberejnaya_timetable_third_courses_page3, naberejnaya_timetable_third_courses_page2, \
    naberejnaya_timetable_fourth_courses_page3, naberejnaya_timetable_fourth_courses_page2

from models.sqlite_db import take_timetable_groups, take_file


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="for_student"))
async def studen_main_panel(call: CallbackQuery):
    photo = await take_timetable_groups(group='Звонок')

    await call.message.answer_photo(photo=photo, caption='Расписание звонков\n \n'
                                                         '<b>Набережная</b> - расписание занятий\n'
                                                         'в отделение на ул. Набережная\n'
                                                         '<b>Собинова</b> - расписание занятий\n'
                                                         'в отделение на ул. Собинова',
                                    reply_markup=student_ways)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="ttnaberejnaya"))
async def timetable_naberejnaya(call: CallbackQuery):
    photo = await take_file(name='Расписание')

    await call.message.answer_photo(photo=photo, caption='Расписание занятий студентов на Набережной\n\n'
                                                         'Выберите курс: ',
                                    reply_markup=naberejnaya_timetable_courses)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="first_nn_timetable"))
async def take_first_course_naberejnaya_page1(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_1_1')

    await call.message.answer_photo(photo=photo, caption='Расписание первых курсов',
                                    reply_markup=naberejnaya_timetable_first_courses_page2)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="ttfnnpage2"))
async def take_first_course_naberejnaya_page2(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_1_2')

    await call.message.answer_photo(photo=photo, caption='Расписание первых курсов',
                                    reply_markup=naberejnaya_timetable_first_courses_page3)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="ttfnnpage3"))
async def take_first_course_naberejnaya_page3(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_1_3')

    await call.message.answer_photo(photo=photo, caption='Расписание первых курсов',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="second_nn_timetable"))
async def take_second_course_naberejnaya_page1(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_2_1')

    await call.message.answer_photo(photo=photo, caption='Расписание вторых курсов',
                                    reply_markup=naberejnaya_timetable_second_courses_page2)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="ttsnnpage2"))
async def take_second_course_naberejnaya_page2(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_2_2')

    await call.message.answer_photo(photo=photo, caption='Расписание вторых курсов',
                                    reply_markup=naberejnaya_timetable_second_courses_page3)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="ttsnnpage3"))
async def take_second_course_naberejnaya_page3(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_2_3')

    await call.message.answer_photo(photo=photo, caption='Расписание вторых курсов',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="third_nn_timetable"))
async def take_third_course_naberejnaya_page1(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_3_1')

    await call.message.answer_photo(photo=photo, caption='Расписание третих курсов',
                                    reply_markup=naberejnaya_timetable_third_courses_page2)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="tttnnpage2"))
async def take_third_course_naberejnaya_page2(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_3_2')

    await call.message.answer_photo(photo=photo, caption='Расписание третих курсов',
                                    reply_markup=naberejnaya_timetable_third_courses_page3)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="tttnnpage3"))
async def take_third_course_naberejnaya_page3(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_3_3')

    await call.message.answer_photo(photo=photo, caption='Расписание третих курсов',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="fourth_nn_timetable"))
async def take_fourth_course_naberejnaya_page1(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_4_1')

    await call.message.answer_photo(photo=photo, caption='Расписание четвёртых курсов',
                                    reply_markup=naberejnaya_timetable_fourth_courses_page2)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="ttfonnpage2"))
async def take_fourth_course_naberejnaya_page2(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_4_2')

    await call.message.answer_photo(photo=photo, caption='Расписание четвёртых курсов',
                                    reply_markup=naberejnaya_timetable_fourth_courses_page3)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="ttfonnpage3"))
async def take_fourth_course_naberejnaya_page3(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_4_3')

    await call.message.answer_photo(photo=photo, caption='Расписание четвёртых курсов',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="fifth_nn_timetable"))
async def take_fifth_course_naberejnaya(call: CallbackQuery):
    photo = await take_timetable_groups(group='Набережная_5')

    await call.message.answer_photo(photo=photo, caption='Расписание пятых курсов',
                                    reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="ttsobinova"))
async def timetable_naberejnaya(call: CallbackQuery):
    photo = await take_file(name='Расписание')

    await call.message.answer_photo(photo=photo, caption='Расписание занятий студентов на Собинова\n\n'
                                                         'Выберите курс: ',
                                    reply_markup=sobinova_timetable_courses)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="first_sn_timetable"))
async def take_first_course_sobinova(call: CallbackQuery):
    photo = await take_timetable_groups(group='Собинова_1')
    await call.message.answer_photo(photo=photo, caption='Расписание первых курсов', reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="second_sn_timetable"))
async def take_second_course_sobinova(call: CallbackQuery):
    photo = await take_timetable_groups(group='Собинова_2')
    await call.message.answer_photo(photo=photo, caption='Расписание вторых курсов', reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="third_sn_timetable"))
async def take_third_course_sobinova(call: CallbackQuery):
    photo = await take_timetable_groups(group='Собинова_3')
    await call.message.answer_photo(photo=photo, caption='Расписание третих курсов', reply_markup=exit_panel)


@dp.callback_query_handler(keyboard.inline.callback_data.callback_panel.filter(item_name="fourth_sn_timetable"))
async def take_fourth_course_sobinova(call: CallbackQuery):
    photo = await take_timetable_groups(group='Собинова_4')
    await call.message.answer_photo(photo=photo, caption='Расписание четвёртых курсов', reply_markup=exit_panel)
