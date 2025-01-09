
from bot.callbacks.callbacks import language_callback
from bot.commands.commands import start_command

from pyrogram import Client, filters

def register_handlers(app: Client):
    app.on_message(filters.command("start"))(start_command)
    app.on_callback_query(filters.regex("^change_lang$"))(language_callback)