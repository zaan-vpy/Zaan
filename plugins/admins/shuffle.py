# Powered By @AdityaHalder

import random

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS
from modules.utils.helpers.filters import command
from modules import app
from modules.misc import db
from modules.utils.decorators import AdminRightsCheck


@app.on_message(
    command(["shuffle", "cshuffle"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text("**ā šš«š«šØš«, šš«šØš§š  šš¬šš š šš ššØš¦š¦šš§šā...**")
    check = db.get(chat_id)
    if not check:
        return await message.reply_text("**ā ššØš­š”š¢š§š  š¢š§š¬š¢šš šš®šš®š ššØ šš”š®ššš„šā...**")
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text("**ā ššš¢š„šš ššØ šš”š®ššš„š.\n\nšš”ššš¤ šš®šš®š :** /queue")
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text("**ā ššš¢š„šš ššØ šš”š®ššš„š.\n\nšš”ššš¤ šš®šš®š :** /queue")
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        "**ā šš®šš®š šš”š®ššš„šš šš² {0}**\n\n**šš”ššš¤ šš”š®ššš„šš šš®šš®š :** /queue".format(message.from_user.first_name)
    )
