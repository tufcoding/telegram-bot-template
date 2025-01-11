from bot.languages.language_manager import lang_manager
from bot.keyboards.keyboards import get_start_keyboard
from bot.utils.decorators import get_user
from logger.logger import logger

from pyrogram.types import BotCommand, Message

async def get_bot_commands():
    return [
        BotCommand(command="start", description="Start the bot"),
    ]

@get_user()
async def start_command(client, message: Message, user, session):
    try:
        await message.reply_text(
            lang_manager.get_text(user.language, "welcome_message", user.first_name),
            reply_markup=get_start_keyboard(user.language)
        )
    except Exception as e:
        logger.error(f"Error in start_command: {e}")