#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from telegram import *
from telegram.ext import *
"""HERE IS YOUR API-TOKEN"""
TOKEN = 'HERE IS YOUR TOKEN' 


"""Here is the text that will be used to represent the project in different languages"""
replyForUkr = 'you choose Ukrainian'
replyForRus = 'you choose Russian'
replyForEng = 'you choose English'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context: CallbackContext):
    buttons = [[InlineKeyboardButton("Ukrainian🇺🇦", callback_data="ukrainian")], [InlineKeyboardButton("English🇺🇸", callback_data="english")], [InlineKeyboardButton("Russian🇷🇺", callback_data="russian")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Choose language you prefer")

def messageHandler(update, context):
    """"""

def help(update, context):
    update.message.reply_text('Help!')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    
    if "ukrainian" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text=replyForUkr)
    if "english" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text=replyForEng)   
    if "russian" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text=replyForRus)



def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # on noncommand i.e message - echo the message on Telegram
   
    dp.add_handler(CallbackQueryHandler(queryHandler))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()