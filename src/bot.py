import os, time
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    bot_token: str = os.getenv("BOT_TOKEN")
    try:
        bot_interval: int = int(os.getenv("BOT_CHECK_INTERVAL")) * 60
    except Exception as e:
        bot_interval: int = 5 * 60
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher

    # add commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # run the bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()