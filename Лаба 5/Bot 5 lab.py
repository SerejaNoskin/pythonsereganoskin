import telebot

token = '5018607839:AAHBNBdbpsf4Ouj7BiyvAHuTlNnbPCiJUQk'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Уроки', 'Ничего')
    bot.send_message(message.chat.id, 'Привет!Что делаешь', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'уроки':
        bot.send_message(message.chat.id, 'Ты молодец!')
    elif message.text.lower() == 'ничего':
        bot.send_message(message.chat.id, 'Жалко(!')
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, 'Напиши /start')
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start', '/help')
        bot.send_message(message.chat.id, 'Если тебе нужна помощь, нажми или напиши /help, если нет - нажми /start', reply_markup=keyboard)


bot.polling()
