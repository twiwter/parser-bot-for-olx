from telebot import TeleBot  # Bot module
# Modules for Inline Keyboard
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
    bot.send_message(message.chat.id, config.setting_screens['first'], reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton(
            "Настройки языка", callback_data='language_settings')]]
    ))

# All Callbacks are registered here


@bot.callback_query_handler(lambda c: c.data == "language_settings")
def process_callback_language_settings(c):
    '''Callback actions for func LANGUAGES'''
    language_keyboard = []
    for language in config.BOT_SETTINGS['language']:
        language_keyboard.append([InlineKeyboardButton(
            language[0], callback_data=str(language[1]))])

    language_keyboard.append([InlineKeyboardButton(
            'Назад', callback_data='back')])

    bot.edit_message_text('Language Settings', c.message.chat.id, c.message.id)
    bot.edit_message_reply_markup(
        c.message.chat.id, c.message.id, reply_markup=InlineKeyboardMarkup(language_keyboard))


# Bot launch
bot.polling()
