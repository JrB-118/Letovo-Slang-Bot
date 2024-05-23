# Начальные настройки

import telebot
from telebot import types

token = '7107994763:AAG-5R8KKtUYOp1QgLYkcZqsLjufKddrywE'
bot = telebot.TeleBot(token)
filename = "feedback.txt"
fh = None

learningwords = {

    "*Аналитика*": "(или ЛК - Личный Кабинет) - онлайн-сервис, личный кабинет учащегося, который включает в себя дневник, расписание уроков, отчет по успеваемости и многое другое. Несмотря на то, что Аналитика - общее название личных кабинетов для учителей , часто это слово используется как синоним к Личному Кабинету для учеников.\nСсылка: student.letovo.ru.",
    "*Канвас, Canvas*": "- онлайн-сервис, в котором располагается основная часть учебного материала, а также многие задания к урокам.\nСсылка: canvas.letovo.ru.",
    "*Форматив, formative assestment*": "(от англ. formative - формирующий) - вид экзамена, за который выставляется оценка, существующая для отслеживания успеваемости учащегося и решения вопросов в случае спорной оценки на summative и не влияющая напрямую на годовой балл. Часто под этим словом подразумевается оценка за этот/эти formative.",
    "*Самматив, summative assestment*": "(от англ. summative - суммирующий) - вид экзамена, который является решающим в и напрямую влияет на годовой балл. Сроки этих экзаменов заранее объявлены. Часто под этим словом подразумевается оценка за этот/эти summative.",
    "*Критерии*": "(ABCD, ашка, бэшка, цэшка, дэшка) - четыре критерия, по каждому из которых выставляется summative-оценка. Каждый отвечает за определенный навык учащегося в конкретном предмете. В summative assestment всегда указаны критерии, влияющие на типы заданий в экзамене. Например, A по алгебре “Знание и понимание” проверяет теоретические знания ученика, а D по биологии “Наука в контексте глобальных вопросов” - умение широко мыслить.",
    "*DP, дипи*": "(от англ. Development Programme) - вид обучения для 10-11 классов, который подготавливает учеников к поступлению в зарубежные ВУЗы. Чтобы попасть в программу DP, необходимо пройти отбор.",
    "*РФ-трек, РФ*": "- стандартный вид обучения для 10-11 классов, который подготавливает учеников к поступлению в российские ВУЗы. Чтобы попасть в данную программу, нет необходимости сдавать дополнительные экзамены.",
    "*Профиль*": "- комбинация предметов для углубленного изучения в 8 классе. Примеры: биохим (биология и химия), соцэк (социально-гуманитарные науки и экономика).",
    "*ИУП*": "(аббр. от Индивидуальный Учебный План) - учебный план, включающий в себя профиль и уровни изучения предметов: по некоторым из них (к примеру иностранным языкам) выделяют группы по уровню знаний.",
    "*ПП*": "- персональный проект, обязателен для выполнения в 9 классе.",
    "*ИВР*": "(аббр. Индивидуальная Выпускная Работа) - проект, обязателен для выполнения в 10 классе.",
    "*Сёрвис*": "(от англ. service - социальная помощь) - социальный проект, обязателен для выполнения 8 классе.",
    "*Диплом Летово*": "- совокупность требований, выполнение которых дает серьезные привилегии, а также помогает при поступлении в ВУЗ. За выполнение поощряемого действия выдаются баллы: золотые, серебряные или бронзовые. Накопив 100 баллов каждого вида, можно получить диплом с отличием.",
    "*Харкнесс*": "- формат дискуссии на уроке, в котором фиксируется взаимодействие участников.",
    "*Граспс*": "(от англ. GRASPS - Goal Role Audience Situation Product Standarts (Цель Роль Аудитория Ситуация Продукт Стандарты)) - формат summative, в котором заданы критерии GRASPS.",
    "*Кас*": "(от англ. CAS - Creativity Activity Service) - список требований для участников программы DP, который разделяется на три критерия: Creativity - креативность, Activity - активность и Service - социальная ответственность."

}

schoollifewords = {

    "*Поддержка*": "- помощь по предмету, которую организовывают учителя по расписанию. На ней можно запросить дополнительные задания, объяснение темы или переписать экзамен.",
    "*Наставник*": "- учитель или сотрудник школы, помогающий своим ученикам-подопечным во всевозможных вопросах. К каждому наставнику распределено некоторое количество учеников.",
    "*Супервайзер*": "- руководитель ученического проекта, аналог наставника в вопросах проектов.",
    "*Горизонтальный наставник, горностай*": "- ученик, помогающий новым ученикам освоиться. Аналогичен обычному наставнику-учителю.",
    "*Внеакадем*": "- кружки, клубы по интересам и занятия, проводимые после уроков. Ученик может выбирать из более чем 100 вариантов!",
    "*Пицца пермишн*": "(от англ. pizza permission - разрешение на пиццу) - разрешение заказать в школу пиццу и съесть. Ученикам ограниченное количество таких разрешений.",
    "*Команды (Komandas)*": "- 5 групп (Орлы, Леопарды, Волки, Тигры, Медведи), соревнующиеся в различных спортивных и интеллектуальных состязаниях. Каждый ученик принадлежит к команде. Аналогия - факультеты в школе Хогвартс в серии книг “Гарри Поттер”.",
    "*Сонник*": "- самый поздний прием пищи в столовой. Как следует из названия, его можно получить перед сном.",
    "*Локер*": "- личный шкафчик ученика, находящийся в здании школы. В начале года ученик может выбрать себе до трёх локеров.",
    "*Ассамблея*": "- еженедельное мероприятие, собрание для учеников, на котором обсуждаются новости, нововведения и прочее. Посещение обязательно. Проводится по понедельникам.",

}

boardingwords = {

    "*Бординг*": "(от англ. boarding - пансион) - система проживания внутри школы. Учеников, проживающих в бординге называют бордерами (boarders).",
    "*Дом*": "- здание, предназначенное для проживания учеников. Здания разделяются на мужские и женские, где живут только юноши или только девушки соответственно. Каждый дом имеет свой номер.",
    "*Хаб*": "- здание, предназначенное для проживания учеников старших классов, а также для административных целей.",
    "*Пансион*": "- под этим словом подразумевается вид нахождения в школе: дневной пансион, недельный пансион и полный пансион.",
    "*Дневной*": "- пансион, при котором ученик не проживает в школе, приезжая и уезжая из школы каждый день.",
    "*Недельный*": "- пансион, при котором ученик проживает в школе только в учебные дни и возвращается домой на выходные.",
    "*Полный*": "- пансион, при котором ученик проживает в школе все время, возвращаясь домой только на каникулы.",
    "*Кёрфью*": "(от англ. curfew - комендантский час) - время, в которое проживающие в бординге обязаны находиться в домах.",
    "*Саспеншн*": "(от англ. suspension - отстранение) - форма наказания в бординге, при которой ученик на некоторое время лишается права проживать в бординге.",
    "*Детеншн*": "(от англ. detention - задержание) - форма наказания в бординге, при которой ученик должен либо написать письменную объяснительную, либо выполнять домашнее задание под надзором хаусмастера в течение часа.",
    "*Преп, преп-рум*": "(от англ. preparation room - комната для подготовки) - общая комната для учебы в Домах. У каждого ученика в ней есть свой личный письменный стол.",
    "*Коммон, коммон-рум*": "(от англ. common room - общая комната) - комната в бординге, предназначенная для отдыха. В ней обычно есть телевизор, настольные игры и прочее.",
    "*Дорм*": "(от англ. dorm - общежитие) - комната для проживания бордеров. ",
    "*Амбассадор дома*": "- член школьного самоуправления, который решает вопросы, связанные с бордингом его дома.",
    "*Хаусмастер*": "(от англ. housemaster - заведующий домом) - должность в бординге. В обязанности входят: поддержание порядка и дисциплины, решение некоторых административных вопросов и т.д.",
    "*Экзит*": "(от англ. exeat - разрешение на отлучку) - разрешение на выход для бордеров. Заявку на него нужно заранее оформлять каждый раз, когда необходимо покинуть школу. Экзит должен быть подтвержден заведующим домом и родителем."
}

all = {**learningwords, **schoollifewords, **boardingwords}

# Приветствие
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я помогу тебе разобраться с локальным языком школы "Летово"')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dictionary = types.KeyboardButton("📕Словарь")
    test = types.KeyboardButton("📋Тест на знание слов")
    findword = types.KeyboardButton("🔎Найти слово")
    errorreport = types.KeyboardButton("❗️Сообщить об ошибке")
    markup.add(dictionary)
    markup.add(test)
    markup.add(findword)
    markup.add(errorreport)
    bot.send_message(message.chat.id, 'Выбери то, что тебе нужно:', reply_markup = markup)
    bot.register_next_step_handler("", next)

# Основное меню
@bot.message_handler(commands=['next'])
def next(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dictionary = types.KeyboardButton("📕Словарь")
    findword = types.KeyboardButton("🔎Найти слово")
    errorreport = types.KeyboardButton("❗️Сообщить об ошибке")
    markup.add(dictionary)
    markup.add(findword)
    markup.add(errorreport)
    bot.send_message(message.chat.id, 'Выбери то, что тебе нужно:', reply_markup = markup)

# @bot.message_handler(commands=['clear'])
# def clear_chat(message):
#     chat_id = message.chat.id
#     message_id = message.message_id
#
#     # Получаем список всех сообщений в чате
#     messages = bot.fetch_all(chat_id)
#
#     # Удаляем каждое сообщение
#     for m in messages:
#         bot.delete_message(chat_id, m.message_id)
#
#     # Удаляем сообщение, которое отправил пользователь
#     bot.delete_message(chat_id, message_id)

# Помощь по боту

# Помощь
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Привет! Этот бот сделан для того, чтобы новые ученики могли освоиться с '
                                      'сленгом школы "Летово". Создан учеником 7 класса Докунихиным Ярославом.')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFmYNmTbd9YLh_Df3fKckLkX8iCVCWcgACARcAAvGv8EgRQ0rD_1-wbjUE')

# Основное меню 2
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "📕Словарь":
        bot.send_message(message.chat.id, "Если вы нашли ошибку/неточность, сообщите в главном меню.")
        keyboard = types.InlineKeyboardMarkup()
        learning = types.InlineKeyboardButton(text="📘Учебное", callback_data="dictlearning")
        schoollife = types.InlineKeyboardButton(text="🏫Жизнь школы", callback_data="dictschoollife")
        boarding = types.InlineKeyboardButton(text="🏠Пансион", callback_data="dictboarding")
        allwords = types.InlineKeyboardButton(text="Все", callback_data="dictall")
        exitbuttton = types.InlineKeyboardButton(text="⬅️Назад", callback_data="back")
        keyboard.add(learning)
        keyboard.add(schoollife)
        keyboard.add(boarding)
        keyboard.add(allwords)
        keyboard.add(exitbuttton)
        bot.send_message(message.chat.id, "Выбери необходимый раздел словаря:",
                         reply_markup=keyboard)
    elif message.text == "🔎Найти слово":
        bot.send_message(message.chat.id, "Если вы нашли ошибку/неточность, сообщите в главном меню.")
        keyboard = types.InlineKeyboardMarkup()
        learning = types.InlineKeyboardButton(text="📘Учебное", callback_data="findlearning")
        schoollife = types.InlineKeyboardButton(text="🏫Жизнь школы", callback_data="findschoollife")
        boarding = types.InlineKeyboardButton(text="🏠Пансион", callback_data="findboarding")
        exitbuttton = types.InlineKeyboardButton(text="⬅️Назад", callback_data="back")
        keyboard.add(learning)
        keyboard.add(schoollife)
        keyboard.add(boarding)
        keyboard.add(exitbuttton)
        bot.send_message(message.chat.id, "Выбери необходимый раздел:",
                         reply_markup=keyboard)
    elif message.text == "❗️Сообщить об ошибке":
        fb = bot.send_message(message.chat.id, "Отправьте нам сообщение об ошибке в одном предложении:")
        bot.register_next_step_handler(fb, feedback)

# Собираем данные
@bot.message_handler(commands=['feedback'])
def feedback(message):

    text = message.text
    global fh
    fh = None
    try:
        fh = open(filename, "w", encoding="utf-8")
        with open(filename, encoding="utf-8") as fh:
            data = fh.read()
    finally:
        if fh:
            fh.close()
    try:
        fh = open(filename, "w", encoding="utf-8")
        print(data + " ", file=fh)
        print(text + " ", file=fh)
    finally:
        if fh:
            fh.close()
    keyboard = types.InlineKeyboardMarkup()
    exitbuttton = types.InlineKeyboardButton(text="⬅️Назад", callback_data="back")
    keyboard.add(exitbuttton)
    bot.send_message(message.chat.id, "Спасибо за ваш отзыв!", reply_markup = keyboard)


# Реакция на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "dictlearning":
            mes_text = ''
            for key, value in learningwords.items():
                mes_text += key + " " + value + "\n\n"
            bot.send_message(call.message.chat.id, mes_text, parse_mode="Markdown")
        if call.data == "dictschoollife":
            mes_text = ''
            for key, value in schoollifewords.items():
                mes_text += key + " " + value + "\n\n"
            bot.send_message(call.message.chat.id, mes_text, parse_mode="Markdown")
        if call.data == "dictboarding":
            mes_text = ''
            for key, value in boardingwords.items():
                mes_text += key + " " + value + "\n\n"
            bot.send_message(call.message.chat.id, mes_text, parse_mode="Markdown")
        if call.data == "dictall":
            mes_text = ''
            for key, value in learningwords.items():
                mes_text += key + " " + value + "\n\n"
            bot.send_message(call.message.chat.id, mes_text, parse_mode="Markdown")
            mes_text = ''
            for key, value in schoollifewords.items():
                mes_text += key + " " + value + "\n\n"
            bot.send_message(call.message.chat.id, mes_text, parse_mode="Markdown")
            mes_text = ''
            for key, value in boardingwords.items():
                mes_text += key + " " + value + "\n\n"
            bot.send_message(call.message.chat.id, mes_text, parse_mode="Markdown")
        if call.data == "findlearning":
            keyboard = types.InlineKeyboardMarkup()
            for key, value in learningwords.items():
                neededtext = str(key)
                key = types.InlineKeyboardButton(text=neededtext[1: (len(neededtext) - 1)], callback_data=neededtext)
                keyboard.add(key)
            exitbuttton = types.InlineKeyboardButton(text="⬅️Назад", callback_data="back")
            keyboard.add(exitbuttton)
            bot.send_message(call.message.chat.id, "Выбери нужное слово:",
                             reply_markup=keyboard)
        if call.data == "findschoollife":
            keyboard = types.InlineKeyboardMarkup()
            for key, value in schoollifewords.items():
                neededtext = str(key)
                key = types.InlineKeyboardButton(text=neededtext[1: (len(neededtext) - 1)], callback_data=neededtext)
                keyboard.add(key)
            exitbuttton = types.InlineKeyboardButton(text="⬅️Назад", callback_data="back")
            keyboard.add(exitbuttton)
            bot.send_message(call.message.chat.id, "Выбери нужное слово:",
                             reply_markup=keyboard)
        if call.data == "findboarding":
            keyboard = types.InlineKeyboardMarkup()
            for key, value in boardingwords.items():
                neededtext = str(key)
                key = types.InlineKeyboardButton(text=neededtext[1: (len(neededtext) - 1)], callback_data=neededtext)
                keyboard.add(key)
            exitbuttton = types.InlineKeyboardButton(text="⬅️Назад", callback_data="back")
            keyboard.add(exitbuttton)
            bot.send_message(call.message.chat.id, "Выбери нужное слово:",
                             reply_markup=keyboard)
        if call.data == "back":
            bot.register_next_step_handler("", next(call.message))
        for key, value in all.items():
            if call.data == str(key):
                bot.send_message(call.message.chat.id, text=str(key + " " + all.get(key)), parse_mode="Markdown")



bot.infinity_polling()
