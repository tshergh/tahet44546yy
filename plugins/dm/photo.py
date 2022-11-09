# fileName : Plugins/dm/photo.py
# copyright ©️ 2021 nabilanavab

# LOGGING INFO: INFO
import logging
logger=logging.getLogger(__name__)
logging.basicConfig(
                   level=logging.INFO,
                   format="%(levelname)s:%(name)s:%(message)s" # %(asctime)s:
                   )

import os
from PIL import Image
from pyrogram.types import (
                           InlineKeyboardButton,
                           InlineKeyboardMarkup
                           )
from pyrogram import filters
from configs.dm import Config
from pdf import PDF, invite_link
from pyrogram import Client as ILovePDF
from configs.images import WELCOME_PIC, BANNED_PIC

UPDATE_CHANNEL = Config.UPDATE_CHANNEL

#--------------->
#--------> LOCAL VARIABLES
#------------------->
UCantUse = "لا يمكنك استخدام هذا الروبوت لبعض الأسباب 🛑"


imageAdded = """`تمت إضافة {} صفحة / إلى ملف pdf ..`🤓
fileName(أسم الملف): `{}.pdf`"""

forceSubMsg = """مرحبا [{}](tg://user?id={}) 🤚🏻..!!
🚸| عذرا عزيزي | sorry dear
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه:
🔰|  You have to subscribe to the bot channel to be able to use it:
👇👇👇👇
 @i2pdfbotchannel
"""
#--------------->
#--------> REPLY TO IMAGES
#------------------->

@ILovePDF.on_message(
                    filters.photo &
                    filters.private &
                    ~filters.edited &
                    filters.incoming
                    )
async def images(bot, message):
    try:
        global invite_link
        await message.reply_chat_action("typing")
        # CHECK USER IN CHANNEL (IF UPDATE_CHANNEL ADDED)
        if UPDATE_CHANNEL:
            try:
                userStatus = await bot.get_chat_member(
                                                      str(UPDATE_CHANNEL),
                                                      message.chat.id
                                                      )
                # IF USER BANNED FROM CHANNEL
                if userStatus.status == 'banned':
                     return await message.reply_photo(
                                                     photo = BANNED_PIC, quote = True,
                                                     caption = "لا يمكنك استخدام هذا الروبوت لبعض الأسباب\nFor Some Reason You Can't Use This Bot"
                                                        "\nاتصل بمالك البوت 🤐\nContact Bot Owner 🤐",
                                                     reply_markup = InlineKeyboardMarkup(
                                                    [[InlineKeyboardButton("المالك Owner 🎊",
                                                      url="https://t.me/ta_ja199")]]
                                              ))
            except Exception:
                if invite_link == None:
                    invite_link = await bot.create_chat_invite_link(
                                                                   int(UPDATE_CHANNEL)
                                                                   )
                return await message.reply_photo(
                                         photo = WELCOME_PIC,
                                         quote = True,
                                         caption = forceSubMsg.format(
                                             message.from_user.first_name, message.chat.id
                                         ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("📢 قناة البوت|channel bot 📢", url=invite_link.invite_link)
                            ],[
                                InlineKeyboardButton("تحديث | Refresh ♻️", callback_data="refresh")
                            ]]
                    ))
        imageReply = await message.reply_text(
                                             "`تنزيل صورتك(Downloading your Image)..⏳`",
                                             quote=True
                                             )
        if not isinstance(PDF.get(message.chat.id), list):
            PDF[message.chat.id] = []
        await message.download(
                              f"{message.chat.id}/{message.chat.id}.jpg"
                              )
        img = Image.open(
            f"{message.chat.id}/{message.chat.id}.jpg"
        ).convert("RGB")
        PDF[message.chat.id].append(img)
        await imageReply.edit(
                             imageAdded.format(
                                              len(PDF[message.chat.id]),
                                              message.chat.id
                                              ),
                             reply_markup = InlineKeyboardMarkup(
                                                                [[
                                                                    InlineKeyboardButton(
                                                                                        "GENERATE|pdfانشاء📕",
                                                                                        callback_data="generate"
                                                                                        ),
                                                                    InlineKeyboardButton(
                                                                                        "RENAME|إعادة تسمية✍️",
                                                                                        callback_data="generateREN"
                                                                                        )
                                                                ]]
                                            )
                             )
    
    except Exception as e:
        logger.exception(
                        "PHOTO:CAUSES %(e)s ERROR خطا",
                        exc_info=True
                        )

#                                                                                              Telegram: @nabilanavab
