from config.settings import API_ID, API_HASH, BOT_TOKEN
from bot.callbacks.callbacks import language_callback
from bot.commands.commands import start_command
from logger.logger import logger

from pyrogram import Client, filters

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

app.on_message(filters.command("start"))(start_command)
app.on_callback_query(filters.regex("^change_lang$"))(language_callback)

if __name__ == "__main__":
    logger.info("Bot is running...")
    app.run()