import asyncio
from pyrogram import Client, filters
from strings.filters import command
from AdRenalen.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AdRenalen import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "🧑🏻‍✈️︙اهلا بك عزيزي العضو ♥️\n\n اليـكـ كـيب الاعـضاء الـخاص بــ سورس ايـرور"




REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
        ("الاوامر")
    ],
    
    [
        ("احرف")
    ],
    [
        ("مطور السورس"),
    ],
   
    [
        ("المطور")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("نكته"),
        ("حكمه")
    ],
    [
        ("انصحني")
    ],
    [
        ("لو خيروك"),
        ("حساب العمر")
    ],    
    [
        ("غنيلي")
    ],
    [
        ("اغلاق الكيبورد")
        
    ]
  
]



  

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اغلاق الكيبورد"))
async def down(client, message):
          m = await message.reply("تم اغلاق الكيبورد بنجاح 💘 ⋅ ", reply_markup= ReplyKeyboardRemove(selective=True))

