from telebot import TeleBot                        # Модуль бота
import time                                        # Временный модуль
# Конфигурация бота, все настройки указаны тут
import config as conf

bot = TeleBot(conf.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    '''Старт бота, дает наставления по использованию бота,
    создает ячейку в базе данных для клиента'''
    pass


@bot.message_handler(commands=['help'])
def help(message):
    '''Дает экскурс на пользование бота, какие есть команды'''
    pass


@bot.message_handler(commands=['myprofile'])
def myprofile(message):
    '''Профиль клиента, тут будет выдаваться inlinekeyboard'''
    pass


@bot.message_handler(commands=['settings'])
def settings(message):
    '''Настройки бота'''
    pass


# Тут прописаны все Callback'и


# Запуск бота
bot.polling()
