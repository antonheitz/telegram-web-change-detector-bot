import os, time
import logging
from typing import List
from telegram import Update, ForceReply, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from .utils import create_table
from .database import Database, WatchItem

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


class Bot:
    def __init__(self, token: str, inteval: int) -> None:
        updater = Updater(token)
        dispatcher = updater.dispatcher
        self.database: Database = Database()

        # add commands
        dispatcher.add_handler(CommandHandler("start", self.start))
        dispatcher.add_handler(CommandHandler("help", self.help_command))
        dispatcher.add_handler(CommandHandler("add", self.add_website))
        dispatcher.add_handler(CommandHandler("list", self.show_websites))

        # run the bot
        updater.start_polling()
        updater.idle()

    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        update.message.reply_markdown_v2(
            fr'Hi {user.mention_markdown_v2()}\!',
            reply_markup=ForceReply(selective=True),
        )

    def help_command(self, update: Update, context: CallbackContext) -> None:
        help_text: str = f"""Use following commands:
"`/add <url> <interval>`" add a website to watch
"`/add <url> <interval>`" add a website to watch

"""
        update.message.reply_markdown_v2(help_text)

    def add_website(self, update: Update, context: CallbackContext) -> None:
        message_parts: List[str] = update.message.text.split(" ")
        if len(message_parts)< 3 and not message_parts[2].isnumeric():
            update.message.reply_text("Please enter correct arguments!")
            return
        chat_id: int = update.message.chat_id
        url: str = message_parts[1]
        update_interval: int = int(message_parts[2]) * 60
        # add to the database
        self.database.add_url(chat_id, url, update_interval)
        update.message.reply_text(f"Added `{url}` to watch!")

    def show_websites(self, update: Update, context: CallbackContext) -> None:
        items: List[WatchItem] = self.database.get_urls(update.message.chat_id)
        text: str = """Your watched items:"""
        for item in items:
            print(item)
            text += f"""
            
            id: {item.id}
            site: {item.url}
            interval: {item.interval/60}
            """
        update.message.reply_text(text)
    
def start_wtih_env() -> None:
    bot_token: str = os.getenv("BOT_TOKEN")
    try:
        bot_interval: int = int(os.getenv("BOT_CHECK_INTERVAL")) * 60
    except Exception as e:
        bot_interval: int = 5 * 60
    bot = Bot(bot_token, bot_interval)

if __name__ == '__main__':
    start_wtih_env()