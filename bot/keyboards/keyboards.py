from bot.languages.language_manager import lang_manager

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_keyboard(lang_code: str):
    return InlineKeyboardMarkup(
        [
            # Change language button
            [
                InlineKeyboardButton(
                    text=lang_manager.get_text(lang_code, "language"),
                    callback_data="change_lang"
                )
            ],
            # Credits link button
            [
                InlineKeyboardButton(
                    text=lang_manager.get_text(lang_code, "credits"),
                    url="https://tufcoding.com"
                )
            ]
        ]
    )