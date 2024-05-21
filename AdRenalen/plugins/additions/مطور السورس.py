import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AdRenalen import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AdRenalen import app
from random import  choice, randint
from asyncio import gather
from pyrogram.errors import FloodWait
from pyrogram.enums import ParseMode, ChatMemberStatus


                
@app.on_message(
    command(["مطور السورس"])
 
)
async def yas(client, message):
    
    usr = await client.get_chat("Y_D_ll")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**مـعـلـومـات مـطـور الـسـورس,☕🌿 السورس\n\n↜︙𝐧𝐚𝐦𝐞 ↬:{name}\n↜︙𝐮𝐬𝐞𝐫 ↬ :@{usr.username}\n↜︙𝐈𝐃 ↬ :`{usr.id}`\n↜︙𝐛𝐢𝐨 ↬: {usr.bio}**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


