import telebot
API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    bot.reply_to(message, 'Приветствую! Ищешь что посмотреть? Ты по адресу! (Напиши любое сообщение, чтобы продолжить)')


@bot.message_handler(func=lambda message: message.text == 'Сериал')
def birchpunk(message: telebot.types.Message):
    markup = telebot.util.quick_markup(
        {
            'Ссылочка': {'url': "https://www.kinopoisk.ru/series/5019944/?ysclid=lrjfjkfanb247311562&utm_referrer=yandex.ru"},
        }
    )
    bot.reply_to(message, "Кибердеревня - лучший отечественный сериал!", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Фильм')
def interstellar(message: telebot.types.Message):
    markup = telebot.util.quick_markup(
        {
            'Ссылочка': {'url': "https://www.kinopoisk.ru/film/258687/?ysclid=lrjfmoyd36352353169"},
        }
    )
    bot.reply_to(message, "Интерстеллар - шедевр Кристофера Нолана", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Мультфильм')
def soul(message: telebot.types.Message):
    markup = telebot.util.quick_markup(
        {
            'Ссылочка': {'url': "https://www.kinopoisk.ru/film/775273/?ysclid=lrjfme90cn217630732"},
        }
    )
    bot.reply_to(message, "Душа: смысл жизни - жить", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def buttons(message: telebot.types.Message):
    markup2 = telebot.types.ReplyKeyboardMarkup(row_width=1)
    markup2.add(telebot.types.KeyboardButton("Мультфильм"))
    markup2.add(
        telebot.types.KeyboardButton("Фильм"),
        telebot.types.KeyboardButton("Сериал")
    )
    bot.reply_to(message, "Выбирай:", reply_markup=markup2)


bot.infinity_polling()
