from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from helpers.decorators import authorized_users_only, errors
from callsmusic.callsmusic import client as USER
from config import SUDO_USERS


@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Make Me As Admin First !!</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "helper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤖: I'm Joined Here For Playing Music On Voice Chat.")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Helper Already In Your Chat.</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} Couldn'T Join Your Group Due To Heavy Join Requests For Userbot !! Make Sure User Is Not Banned In Group."
            "\n\nOr Manually Add Asisstant To Your Group And Try Again.</b>",
        )
        return
    await message.reply_text(
        "<b>Helper Userbot Joined Your Chat.</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>User Couldn'T Leave Your Group !! May Be Floodwaits."
            "\n\nOr Manually Kick Me From To Your Group.</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving All Chats.")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant Leaving... Left : {left} Chats. Failed : {failed} Chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} Chats. Failed : {failed} Chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} Chats. Failed : {failed} Chats.")
