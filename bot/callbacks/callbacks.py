from bot.languages.language_manager import LanguageManager
from bot.keyboards.keyboards import get_start_keyboard
from bot.utils.decorators import get_user
from logger.logger import logger

lang_manager = LanguageManager()

@get_user()
async def language_callback(client, callback_query, user, session):
    try:
        new_lang = lang_manager.get_next_language(user.language)
        user.language = new_lang
        session.commit()
        
        await callback_query.message.edit_text(
            lang_manager.get_text(new_lang, "welcome_message", user.first_name),
            reply_markup=get_start_keyboard(new_lang)
        )
    except Exception as e:
        logger.error(f"Error in language_callback: {e}")