from telebot import TeleBot  # Bot module
from telebot.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import time  # Temporary module
import config  # Bot configuration, all settings are listed here

bot = TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    '''Start the bot, gives instructions on how to use the bot,
     creates a cell in the database for the client'''
    pass


@bot.message_handler(commands=['help'])
def help(message):
    '''Gives an excursion on how to use the bot, what commands are there'''
    pass


@bot.message_handler(commands=['myprofile'])
def myprofile(message):
    '''Client profile, inlinekeyboard will be issued here'''
    pass


@bot.message_handler(commands=['settings'])
def settings(message):
    '''Bot settings'''
    bot.send_message(message.chat.id, 'Настройки бота', reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(
                "Настройки языка", callback_data='language_settings')],
            [InlineKeyboardButton(
                "Интервальность", callback_data='interval')]
        ]
    ))

# All Callbacks are registered here


@bot.callback_query_handler(lambda c: c.data == "language_settings")
def process_callback_language_settings(c):
    '''Callback actions for func LANGUAGES'''
    language_keyboard = []
    for language in config.BOT_SETTINGS['language']:
        language_keyboard.append(
            [InlineKeyboardButton(language[0], callback_data=str(language[1]))]
        )

    language_keyboard.append(
        [InlineKeyboardButton(
            'Назад', callback_data='back')
         ]
    )

    bot.edit_message_text('Выберите язык', c.message.chat.id, c.message.id)
    bot.edit_message_reply_markup(
        c.message.chat.id, c.message.id, reply_markup=InlineKeyboardMarkup(language_keyboard))


@bot.callback_query_handler(lambda c: c.data == "back")
def process_callback_language_settings(c):
    '''Callback action for func BACK'''
    message = c.message.text

    if message == 'Выберите язык':
        bot.edit_message_text(
            'Настройки бота', c.message.chat.id, c.message.id)

        bot.edit_message_reply_markup(c.message.chat.id, c.message.id, reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(
                    "Настройки языка", callback_data='language_settings')],
                [InlineKeyboardButton(
                    "Интервальность", callback_data='interval')]
            ]
        ))


# Bot launch
bot.polling()
