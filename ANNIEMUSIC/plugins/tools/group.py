from pyrogram import filters
from pyrogram.types import Message

from ANNIEMUSIC import app
from config import OWNER_ID


@app.on_message(filters.video_chat_started)
async def on_voice_chat_started(_, message: Message):
    await message.reply_text("🎙 **ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ʜᴀs sᴛᴀʀᴛᴇᴅ!**")




@app.on_message(filters.command("leavegroup") & filters.user(OWNER_ID))
async def leave_group(_, message: Message):
    await message.reply_text("👋 **ʟᴇᴀᴠɪɴɢ ᴛʜɪs ɢʀᴏᴜᴘ...**")
    await app.leave_chat(chat_id=message.chat.id, delete=True)
