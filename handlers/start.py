from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>📌 **Holla, {message.from_user.first_name}** \n
💭 **[{BOT_NAME}](https://t.me/QueenAlishaRobot) I Am A Voice Call Group Music Player. For Info On How To Use Me, You Can Type /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕", url=f"https://t.me/QueenAlishaRobot?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "Commands", url="https://telegra.ph/%F0%9D%99%80%F0%9D%99%87%F0%9D%99%A7%F0%9D%99%9E%F0%9D%99%AD--%F0%9D%99%88%F0%9D%99%AA%F0%9D%99%A8%F0%9D%99%9E%F0%9D%99%98-09-03-2"
                    ),
                    InlineKeyboardButton(
                        "Donate", url=f"https://t.me/Venom_Hai_Hum")
                ],[
                    InlineKeyboardButton(
                        "Official Group", url=f"https://t.me/https://t.me/Shayri_Music_Lovers"
                    ),
                    InlineKeyboardButton(
                        "Official Channel", url=f"https://t.me/ABOUTABHI")
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **ALISHA MUSIC IS RUNNING**\n<b>⚡ **Uptime :**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url=f"https://t.me/Shayri_Music_Lovers"
                    ),
                    InlineKeyboardButton(
                        "Channel", url=f"https://t.me/ABOUTABHI"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hello {message.from_user.mention()}, Please Tap The Button Below To See The Help Message You Can Read For Using This Bot</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❔ HOW TO USE ME", url=f"https://t.me/QueenAlishaRobot?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.mention()}, Welcome To Help Menu ✨
\n📌HOW TO USE ME ?
\n1. first add me to your group.
2. promote me as admin and give all permission.
3. then, add @ElrixXAssistant to your group or type /userbotjoin.
3. make sure you turn on the voice chat first before start playing music.
\n📌**commands for all user:**
\n/play (song name) - play song from youtube
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/current - show the song in streaming
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/vk (song name) - download song from inline mode
\n📌 **commands for admins:**
\n/player - open music player settings panel
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/reload - for refresh the admin list
/cache - for cleared admin cache
/musicplayer (on / off) - disable / enable music player in your group
\n🎧 channel streaming commands:
\n/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
\n🧙‍♂️ command for sudo users:
\n/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
\n📌 **commands for fun:**
\n/lyric - (song name) lyrics scrapper
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "GROUP", url=f"https://t.me/Shayri_Music_Lovers"
                    ),
                    InlineKeyboardButton(
                        "CHANNEL", url=f"https://t.me/ABOUTABHI"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "DEVELOPER", url=f"https://t.me/Venom_Hai_Hum"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("Pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "`PONG !!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} Ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 Bot Status :\n"
        f"• **Uptime :** `{uptime}`\n"
        f"• **Start Time :** `{START_TIME_ISO}`"
    )
