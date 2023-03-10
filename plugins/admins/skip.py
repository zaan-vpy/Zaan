# Powered By @AdityaHalder

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from modules import config
from modules.config import BANNED_USERS
from modules.utils.helpers.filters import command
from modules import YouTube, app
from modules.core.call import Aditya
from modules.misc import db
from modules.utils.database import get_loop
from modules.utils.decorators import AdminRightsCheck
from modules.utils.inline.play import (stream_markup,
                                          telegram_markup)
from modules.utils.stream.autoclear import auto_clean
from modules.utils.thumbnails import gen_thumb


@app.on_message(
    command(["skip", "cskip"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def skip(cli, message: Message, _, chat_id):
    if not len(message.command) < 2:
        loop = await get_loop(chat_id)
        if loop != 0:
            return await message.reply_text("**๐ฅ ๐๐ฅ๐๐๐ฌ๐, ๐๐ญ ๐๐ข๐ซ๐ฌ๐ญ ๐๐ข๐ฌ๐๐๐ฅ๐ ๐๐จ๐จ๐ฉ ๐๐ฅ๐๐ฒ โจ ...**")
        state = message.text.split(None, 1)[1].strip()
        if state.isnumeric():
            state = int(state)
            check = db.get(chat_id)
            if check:
                count = len(check)
                if count > 2:
                    count = int(count - 1)
                    if 1 <= state <= count:
                        for x in range(state):
                            popped = None
                            try:
                                popped = check.pop(0)
                            except:
                                return await message.reply_text(
                                    "**โ๐๐๐ข๐ฅ๐๐ ๐๐จ ๐๐ค๐ข๐ฉ ๐๐จ ๐๐ฉ๐๐๐ข๐๐ข๐ ๐๐จ๐ง๐  โจ ...\n\nโ ๐๐ก๐๐๐ค ๐๐๐๐ญ ๐๐ฎ๐๐ฎ๐ ๐๐ฒ ยป** /queue"
                                )
                            if popped:
                                if (
                                    config.AUTO_DOWNLOADS_CLEAR
                                    == str(True)
                                ):
                                    await auto_clean(popped)
                            if not check:
                                try:
                                    await message.reply_text(
                                        "**๐ฅ ๐๐ฆ๐ฉ๐ญ๐ฒ ๐๐ฎ๐๐ฎ๐, ๐๐๐๐ฏ๐ข๐ง๐ \n๐๐ซ๐จ๐ฆ ๐๐ โจ...**".format(
                                            message.from_user.first_name
                                        )
                                    )
                                    await Aditya.stop_stream(chat_id)
                                except:
                                    return
                                break
                    else:
                        return await message.reply_text(
                            "**โ ๐๐จ๐ญ ๐๐ง๐จ๐ฎ๐ ๐ก ๐๐ซ๐๐๐ค๐ฌ ๐ข๐ง ๐๐ฎ๐๐ฎ๐ ๐๐จ๐ซ ๐๐ก๐ ๐๐๐ฅ๐ฎ๐ ๐๐ข๐ฏ๐๐ง ๐๐ฒ ๐๐จ๐ฎ. ๐ฅ ๐๐ฅ๐๐๐ฌ๐ ๐๐ก๐จ๐จ๐ฌ๐ ๐๐ฎ๐ฆ๐๐๐ซ๐ฌ ๐๐๐ญ๐ฐ๐๐๐ง 1 ๐๐ง๐ {0} โจ ...**".format(count)
                        )
                else:
                    return await message.reply_text("**โ ๐๐ญ๐ฅ๐๐๐ฌ๐ญ ๐ ๐๐จ๐ง๐ ๐ฌ ๐๐๐๐๐๐ ๐ข๐ง ๐๐ฎ๐๐ฎ๐ ๐๐จ ๐๐ค๐ข๐ฉ ๐๐จ ๐ ๐๐ฉ๐๐๐ข๐๐ข๐ ๐๐ฎ๐ฆ๐๐๐ซ. ๐๐ก๐๐๐ค ๐๐ฎ๐๐ฎ๐ ๐๐ฒ ยป** /queue")
            else:
                return await message.reply_text("**๐ซ ๐๐ฎ๐๐ฎ๐๐ ๐๐ข๐ฌ๐ญ ๐ข๐ฌ ๐๐ฆ๐ฉ๐ญ๐ฒโ...**")
        else:
            return await message.reply_text("**โ ๐๐ฅ๐๐๐ฌ๐ ๐๐ฌ๐ ๐๐ฎ๐ฆ๐๐ซ๐ข๐ ๐๐ฎ๐ฆ๐๐๐ซ๐ฌ ๐๐จ๐ซ ๐๐ฉ๐๐๐ข๐๐ข๐ ๐๐จ๐ง๐ ๐ฌ, ๐๐ข๐ค๐ ๐, ๐, ๐ ๐๐ซ ๐ ๐๐ญ๐ โจ **...")
    else:
        check = db.get(chat_id)
        popped = None
        try:
            popped = check.pop(0)
            if popped:
                if config.AUTO_DOWNLOADS_CLEAR == str(True):
                    await auto_clean(popped)
            if not check:
                await message.reply_text(
                    "**๐ฅ ๐๐ฆ๐ฉ๐ญ๐ฒ ๐๐ฎ๐๐ฎ๐, ๐๐๐๐ฏ๐ข๐ง๐ \n๐๐ซ๐จ๐ฆ ๐๐ โจ...**".format(message.from_user.first_name)
                )
                try:
                    return await Aditya.stop_stream(chat_id)
                except:
                    return
        except:
            try:
                await message.reply_text(
                    "**๐ฅ ๐๐ฆ๐ฉ๐ญ๐ฒ ๐๐ฎ๐๐ฎ๐, ๐๐๐๐ฏ๐ข๐ง๐ \n๐๐ซ๐จ๐ฆ ๐๐ โจ...**".format(message.from_user.first_name)
                )
                return await Aditya.stop_stream(chat_id)
            except:
                return
    queued = check[0]["file"]
    title = (check[0]["title"]).title()
    user = check[0]["by"]
    streamtype = check[0]["streamtype"]
    videoid = check[0]["vidid"]
    status = True if str(streamtype) == "video" else None
    if "live_" in queued:
        n, link = await YouTube.video(videoid, True)
        if n == 0:
            return await message.reply_text(
                "**๐ฅ ๐๐ค๐ข๐ฉ๐ฉ๐ข๐ง๐  ๐๐ซ๐ซ๐จ๐ซ, ๐๐จ ๐๐ฅ๐๐๐ฌ๐\n๐๐ค๐ข๐ฉ ๐๐ ๐๐ข๐ง โจ ...**".format(title)
            )
        try:
            await Aditya.skip_stream(chat_id, link, video=status)
        except Exception:
            return await message.reply_text("**๐ฅ ๐๐ค๐ข๐ฉ๐ฉ๐ข๐ง๐  ๐๐ซ๐ซ๐จ๐ซ, ๐๐จ ๐๐ฅ๐๐๐ฌ๐\n๐๐ค๐ข๐ฉ ๐๐ ๐๐ข๐ง โจ ...**")
        button = telegram_markup(_, chat_id)
        img = await gen_thumb(videoid)
        run = await message.reply_photo(
            photo=img,
            caption="**๐ฅ โฐ๐๐๐ข๐ญ๐ฒ๐โ๐๐ฅ๐๐ฒ๐๐ซโฑ ๐ฟ ๐๐จ๐ฐ ๐\n๐ ๐๐ฅ๐๐ฒ๐ข๐ง๐  ๐ ๐๐ ๐ฅ ...**".format(
                user,
                f"https://t.me/{app.username}?start=info_{videoid}",
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
    elif "vid_" in queued:
        mystic = await message.reply_text(
            "**โ ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐ข๐ง๐  ๐๐๐ฑ๐ญ ๐๐จ๐ง๐ \n๐๐ซ๐จ๐ฆ ๐๐ฅ๐๐ฒ๐ฅ๐ข๐ฌ๐ญ ๐ ...**", disable_web_page_preview=True
        )
        try:
            file_path, direct = await YouTube.download(
                videoid,
                mystic,
                videoid=True,
                video=status,
            )
        except:
            return await mystic.edit_text("**๐ฅ ๐๐ค๐ข๐ฉ๐ฉ๐ข๐ง๐  ๐๐ซ๐ซ๐จ๐ซ, ๐๐จ ๐๐ฅ๐๐๐ฌ๐\n๐๐ค๐ข๐ฉ ๐๐ ๐๐ข๐ง โจ ...**")
        try:
            await Aditya.skip_stream(chat_id, file_path, video=status)
        except Exception:
            return await mystic.edit_text("**๐ฅ ๐๐ค๐ข๐ฉ๐ฉ๐ข๐ง๐  ๐๐ซ๐ซ๐จ๐ซ, ๐๐จ ๐๐ฅ๐๐๐ฌ๐\n๐๐ค๐ข๐ฉ ๐๐ ๐๐ข๐ง โจ ...**")
        button = stream_markup(_, videoid, chat_id)
        img = await gen_thumb(videoid)
        run = await message.reply_photo(
            photo=img,
            caption="**๐ฅ โฐ๐๐๐ข๐ญ๐ฒ๐โ๐๐ฅ๐๐ฒ๐๐ซโฑ ๐ฟ ๐๐จ๐ฐ ๐\n๐ ๐๐ฅ๐๐ฒ๐ข๐ง๐  ๐ ๐๐ ๐ฅ ...**".format(
                user,
                f"https://t.me/{app.username}?start=info_{videoid}",
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "stream"
        await mystic.delete()
    elif "index_" in queued:
        try:
            await Aditya.skip_stream(chat_id, videoid, video=status)
        except Exception:
            return await message.reply_text("**๐ฅ ๐๐ค๐ข๐ฉ๐ฉ๐ข๐ง๐  ๐๐ซ๐ซ๐จ๐ซ, ๐๐จ ๐๐ฅ๐๐๐ฌ๐\n๐๐ค๐ข๐ฉ ๐๐ ๐๐ข๐ง โจ ...**")
        button = telegram_markup(_, chat_id)
        run = await message.reply_photo(
            photo=config.STREAM_IMG_URL,
            caption="**๐ฅ โฐ๐๐๐ข๐ญ๐ฒ๐โ๐๐ฅ๐๐ฒ๐๐ซโฑ ๐ฟ ๐๐จ๐ฐ ๐\n๐ ๐๐ฅ๐๐ฒ๐ข๐ง๐  ๐ ๐๐ ๐ฅ ...**".format(user),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
    else:
        try:
            await Aditya.skip_stream(chat_id, queued, video=status)
        except Exception:
            return await message.reply_text("**๐ฅ ๐๐ค๐ข๐ฉ๐ฉ๐ข๐ง๐  ๐๐ซ๐ซ๐จ๐ซ, ๐๐จ ๐๐ฅ๐๐๐ฌ๐\n๐๐ค๐ข๐ฉ ๐๐ ๐๐ข๐ง โจ ...**")
        if videoid == "telegram":
            button = telegram_markup(_, chat_id)
            run = await message.reply_photo(
                photo=config.TELEGRAM_AUDIO_URL
                if str(streamtype) == "audio"
                else config.TELEGRAM_VIDEO_URL,
                caption="**๐ฅ โฐ๐๐๐ข๐ญ๐ฒ๐โ๐๐ฅ๐๐ฒ๐๐ซโฑ ๐ฟ ๐๐จ๐ฐ ๐\n๐ ๐๐ฅ๐๐ฒ๐ข๐ง๐  ๐ ๐๐ ๐ฅ ...**".format(
                    title, check[0]["dur"], user
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
        elif videoid == "soundcloud":
            button = telegram_markup(_, chat_id)
            run = await message.reply_photo(
                photo=config.SOUNCLOUD_IMG_URL
                if str(streamtype) == "audio"
                else config.TELEGRAM_VIDEO_URL,
                caption="**๐ฅ โฐ๐๐๐ข๐ญ๐ฒ๐โ๐๐ฅ๐๐ฒ๐๐ซโฑ ๐ฟ ๐๐จ๐ฐ ๐\n๐ ๐๐ฅ๐๐ฒ๐ข๐ง๐  ๐ ๐๐ ๐ฅ ...**".format(
                    title, check[0]["dur"], user
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
        else:
            button = stream_markup(_, videoid, chat_id)
            img = await gen_thumb(videoid)
            run = await message.reply_photo(
                photo=img,
                caption="**๐ฅ โฐ๐๐๐ข๐ญ๐ฒ๐โ๐๐ฅ๐๐ฒ๐๐ซโฑ ๐ฟ ๐๐จ๐ฐ ๐\n๐ ๐๐ฅ๐๐ฒ๐ข๐ง๐  ๐ ๐๐ ๐ฅ ...**".format(
                    user,
                    f"https://t.me/{app.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
