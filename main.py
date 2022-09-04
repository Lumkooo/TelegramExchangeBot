# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from Token import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
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
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()