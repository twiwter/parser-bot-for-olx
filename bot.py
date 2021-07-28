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
    pass


# All Callbacks are registered here


# Bot launch
bot.polling()
