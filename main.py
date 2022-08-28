# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi!")

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Help!")

def echo(update, context):
    incoming_message = update.message.text
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = data['Valute'][incoming_message]['Value']
    valute_name = data['Valute'][incoming_message]['Name']
    result_message = "Курс \""+valute_name+"\" ("+incoming_message+")"+" по центробанку на данный момент составляет: "+str(result)+" рублей"
    update.message.reply_text(result_message)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    """Start the bot."""
    updater = Updater("Insert token here", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

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