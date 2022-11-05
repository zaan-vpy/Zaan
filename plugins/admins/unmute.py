# Powered By @AdityaHalder

from pyrogram import filters
from pyrogram.types import Message

from modules.config import BANNED_USERS
from modules.utils.helpers.filters import command
from modules import app
from modules.core.call import Aditya
from modules.utils.database import is_muted, mute_off
from modules.utils.decorators import AdminRightsCheck


@app.on_message(
    command(["unmute", "cunmute"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    if not await is_muted(chat_id):
        return await message.reply_text("**🔊 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 ✨ ...**")
    await mute_off(chat_id)
    await Aditya.unmute_stream(chat_id)
    await message.reply_text(
        "**🔊 𝐔𝐧𝐦𝐮𝐭𝐞𝐝 🌷 ...**".format(message.from_user.mention)
    )
