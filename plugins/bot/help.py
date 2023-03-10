# Powered By @AdityaHalder


from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from modules.config import BANNED_USERS
from modules.utils.helpers.filters import command
from modules.strings import get_string, helpers
from modules import app
from modules.misc import SUDOERS
from modules.utils import help_pannel
from modules.utils.database import get_lang, is_commanddelete_on
from modules.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from modules.utils.inline.help import (help_back_markup,
                                          private_help_panel)




@app.on_message(
    command(["help"])
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_callback_query(
    filters.regex("settings_back_helper") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        if update.message.photo:
            await update.message.delete()
            await update.message.reply_text(
                "**โ ๐๐ฅ๐ข๐๐ค ๐๐ง ๐๐ก๐ ๐บ ๐๐๐ฅ๐จ๐ฐ ๐๐ฎ๐ญ๐ญ๐จ๐ง๐ฌ ๐๐จ๐ซ\n๐๐จ๐ซ๐ ๐๐ง๐๐จ๐ซ๐ฆ๐๐ญ๐ข๐จ๐ง โจ ...\n\n๐ฅ๐๐ ๐๐จ๐ฎ ๐๐ซ๐ ๐๐๐๐ข๐ง๐  ยป ๐๐ง๐ฒ ๐๐ซ๐จ๐๐ฅ๐๐ฆ๐ฌ ๐ข๐ง ๐๐จ๐ฆ๐ฆ๐๐ง๐ ๐๐ก๐๐ง โฅ๏ธ ๐๐จ๐ฎ ๐๐๐ง ๐๐จ๐ง๐ญ๐๐๐ญ ๐๐จ\n๐๐ฒ ๐๐ฐ๐ง๐๐ซ โฅ๏ธ ๐๐ซ ๐๐ฌ๐ค ๐ข๐ง โฅ๏ธ ๐๐ฎ๐ซ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ\n๐๐ก๐๐ญ ๐๐ซ๐จ๐ฎ๐ฉ ๐ ...\n\n๐ท๐๐ฅ๐ฅ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐๐ง ๐๐ ๐๐ฌ๐๐ ๐๐ข๐ญ๐ก: /**", reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                "**โ ๐๐ฅ๐ข๐๐ค ๐๐ง ๐๐ก๐ ๐บ ๐๐๐ฅ๐จ๐ฐ ๐๐ฎ๐ญ๐ญ๐จ๐ง๐ฌ ๐๐จ๐ซ\n๐๐จ๐ซ๐ ๐๐ง๐๐จ๐ซ๐ฆ๐๐ญ๐ข๐จ๐ง โจ ...\n\n๐ฅ๐๐ ๐๐จ๐ฎ ๐๐ซ๐ ๐๐๐๐ข๐ง๐  ยป ๐๐ง๐ฒ ๐๐ซ๐จ๐๐ฅ๐๐ฆ๐ฌ ๐ข๐ง ๐๐จ๐ฆ๐ฆ๐๐ง๐ ๐๐ก๐๐ง โฅ๏ธ ๐๐จ๐ฎ ๐๐๐ง ๐๐จ๐ง๐ญ๐๐๐ญ ๐๐จ\n๐๐ฒ ๐๐ฐ๐ง๐๐ซ โฅ๏ธ ๐๐ซ ๐๐ฌ๐ค ๐ข๐ง โฅ๏ธ ๐๐ฎ๐ซ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ\n๐๐ก๐๐ญ ๐๐ซ๐จ๐ฎ๐ฉ ๐ ...\n\n๐ท๐๐ฅ๐ฅ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐๐ง ๐๐ ๐๐ฌ๐๐ ๐๐ข๐ญ๐ก: /**", reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_text("**โ ๐๐ฅ๐ข๐๐ค ๐๐ง ๐๐ก๐ ๐บ ๐๐๐ฅ๐จ๐ฐ ๐๐ฎ๐ญ๐ญ๐จ๐ง๐ฌ ๐๐จ๐ซ\n๐๐จ๐ซ๐ ๐๐ง๐๐จ๐ซ๐ฆ๐๐ญ๐ข๐จ๐ง โจ ...\n\n๐ฅ๐๐ ๐๐จ๐ฎ ๐๐ซ๐ ๐๐๐๐ข๐ง๐  ยป ๐๐ง๐ฒ ๐๐ซ๐จ๐๐ฅ๐๐ฆ๐ฌ ๐ข๐ง ๐๐จ๐ฆ๐ฆ๐๐ง๐ ๐๐ก๐๐ง โฅ๏ธ ๐๐จ๐ฎ ๐๐๐ง ๐๐จ๐ง๐ญ๐๐๐ญ ๐๐จ\n๐๐ฒ ๐๐ฐ๐ง๐๐ซ โฅ๏ธ ๐๐ซ ๐๐ฌ๐ค ๐ข๐ง โฅ๏ธ ๐๐ฎ๐ซ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ\n๐๐ก๐๐ญ ๐๐ซ๐จ๐ฎ๐ฉ ๐ ...\n\n๐ท๐๐ฅ๐ฅ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐๐ง ๐๐ ๐๐ฌ๐๐ ๐๐ข๐ญ๐ก: /**", reply_markup=keyboard)


@app.on_message(
    filters.command(["help"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(
        "**๐ฅ ๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ยป ๐ข๐ง ๐๐ซ๐ข๐ฏ๐๐ญ๐\n๐๐จ๐ซ ๐๐จ๐ซ๐ ๐๐๐ฅ๐ฉ ๐ ...**", reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb5":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "๐ฅ ๐๐ง๐ฅ๐ฒ ๐๐จ๐ซ ๐๐ฎ๐๐จ ๐๐ฌ๐๐ซ๐ฌ ๐", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_5, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            helpers.HELP_1, reply_markup=keyboard
        )
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            helpers.HELP_2, reply_markup=keyboard
        )
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            helpers.HELP_3, reply_markup=keyboard
        )
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            helpers.HELP_4, reply_markup=keyboard
        )
