import telebot
import config
import dbworker
token = '5004963884:AAE_Y20DIdIxjkIrlkMzBy8FbSPEfHbrWlc'
bot = telebot.TeleBot(config.token)
available_sign = ["козерог", "водолей", "рыбы", "овен", "телец", "близнецы", "рак", "лев", "дева", "весы", "скорпион", "стрелец"]
cars =['форд', 'хёндай', 'шкода', 'жигули', 'волга', 'нет машины']
bot = telebot.TeleBot(token)



@bot.message_handler(commands=["cancel"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Пока, если что переходи в /menu")
    dbworker.set_state(message.chat.id, config.States. S_START.value)


@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Опять все по новой...\n представляйся ещё раз")
    dbworker.set_state(message.chat.id, config.States.STATE_FIRST_NUM.value)

# Начало диалога
@bot.message_handler(commands=['begin'])
def cmd_start(message):
    bot.send_message(message.chat.id, "смело! но если захочешь выйти из этого режима - /cancel поможет\nначать заполнять заново - /reset\nкак к тебе обращаться?")
    dbworker.set_state(message.chat.id, config.States.STATE_FIRST_NUM.value)

# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.STATE_FIRST_NUM.value)
def user_entering_name(message):
    if not message.text.isalpha():
        bot.send_message(message.chat.id, "Не похоже что это имя, вводи буквы")
        return
    else:
        bot.send_message(message.chat.id, "Твой знак зодиака...")
        dbworker.set_state(message.chat.id, config.States.STATE_SECOND_NUM.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.STATE_SECOND_NUM.value)
def user_entering_sign(message):
    # А вот тут сделаем проверку
    if message.text.lower() not in available_sign:
        bot.send_message(message.chat.id, "Такого знака не бывает, выбери существующий!")
        return
    else:
        if message.text.lower() == 'овен' or message.text.lower() =='лев' or message.text.lower() =='рыбы':
            bot.send_message(message.chat.id, "идеальный знак)!")
        if message.text.lower() == 'рак' or message.text.lower() == 'водолей' or message.text.lower() == 'весы':
            bot.send_message(message.chat.id, "ну норм...")
        if message.text.lower() == 'козерог':
            bot.send_message(message.chat.id, "не одобряю")

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        for model in cars:
            keyboard.add(model)
        bot.send_message(message.chat.id, "Выбери машину", reply_markup=keyboard)
        dbworker.set_state(message.chat.id, config.States.STATE_THIRD_NUM.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.STATE_THIRD_NUM.value)
def user_model(message):
    if message.text.lower() not in cars:
        bot.send_message(message.chat.id, "Да нет такого, давай по новой")
        return
    else:
        bot.send_message(message.chat.id, "Ну ладно")
        dbworker.set_state(message.chat.id, config.States.S_START.value)
        bot.send_message(message.chat.id, "Это конец теста")
        if message.text.lower() == 'нет машины':
            bot.send_message(message.chat.id, "что ж иди копи на машину))")
        else:
            bot.send_message(message.chat.id, "воу да ты реально крут в /menu")


@bot.message_handler(commands=['start'])
def stt_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    buttons = ["/menu"]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'Привет, молодёжь! Ну или как у вас принято говорить - привет-медвед, молодёжь!', reply_markup=keyboard)

@bot.message_handler(commands=['menu'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    buttons = ["анекдот", "пока", "/test", "/begin"]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, ' Хочешь попрощаться - нажми "пока"\nХочешь интерактива - нажми "/test"\nХочешь пройти тест на крутость - нажми "/begin"\nНу и анекдот, думаю, понятно) ', reply_markup=keyboard)


@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='форд', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='хёндай', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='жигули', callback_data=3))
    bot.send_message(message.chat.id, text="какую машину хочешь увидеть?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'анекдот':
        bot.send_message(message.chat.id, 'Анекдот №186:\nКолобок повесился')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Удачи!')
    elif message.text.lower() == 'песню!':
        bot.send_message(message.chat.id, 'ху ху, ну держи, повайбь')
        bot.send_message(message.chat.id, 'https://open.spotify.com/track/7EkWXAI1wn8Ii883ecd9xr?si=51LCrMbFTSyESuTgHBoCGg&utm_source=copy-link')
    else:
        bot.send_message(message.chat.id, ':/')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == '1':
        bot.send_photo(call.message.chat.id, 'https://a.d-cd.net/a355568s-960.jpg')
    elif call.data == '2':
        bot.send_photo(call.message.chat.id, 'https://avilon-trade.ru/img/catalog/hyundai/elantra/1.jpg')
    elif call.data == '3':
        bot.send_photo(call.message.chat.id, 'https://www.autopanorama.ru/announcephoto/cee9887075ec66da55b9bde1cff7892d-0.jpeg')

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()