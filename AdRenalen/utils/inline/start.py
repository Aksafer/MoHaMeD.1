from pyrogram.types import InlineKeyboardButton

import config
from AdRenalen import app


def start_panel(_):
    buttons = [
        [InlineKeyboardButton(text="الاوامـر 🌿 ", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="الـمـطـور 🌿 ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="قـنـاة الـسـورس 🌿 ", url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [InlineKeyboardButton(text="الاوامر ⚙", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="المطور ⋅", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="قناة السورس ⋅", url=config.SUPPORT_CHANNEL),
        ],
    [
            InlineKeyboardButton(
                text="اضف البوت الي مجموعتك ✅ ⋅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],]
    return buttons
