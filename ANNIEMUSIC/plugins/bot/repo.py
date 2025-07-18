from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANNIEMUSIC import app
from config import BOT_USERNAME

repo_caption = """**
🚀 ᴄʟᴏɴᴇ ᴀɴᴅ ᴅᴇᴘʟᴏʏ – ᴄᴇʀᴛɪꜰɪᴇᴅ ᴄᴏᴅᴇʀꜱ ʀᴇᴘᴏ 🚀

➤ ᴅᴇᴘʟᴏʏ ᴇᴀsɪʟʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴇʀʀᴏʀꜱ  
➤ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪꜱꜱᴜᴇ  
➤ ɴᴏ ɪᴅ ʙᴀɴ ɪꜱꜱᴜᴇ  
➤ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏꜱ  
➤ ʀᴜɴ 24/7 ʟᴀɢ ꜰʀᴇᴇ

ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ꜱᴇɴᴅ ꜱꜱ ɪɴ ꜱᴜᴘᴘᴏʀᴛ
**"""

@app.on_message(filters.command("repo"))
async def show_repo(_, msg):
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url="https://t.me/MrPerfectXd"),
            InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/Telugu_Grpz")
        ],
        [
            InlineKeyboardButton("🛠️ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/Telugu_Grpz"),
            InlineKeyboardButton("🎵 ɢɪᴛʜᴜʙ", url="https://t.me/TitanNetwrk")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://graph.org/file/5b5803b02a24b043fc6d0.jpg",
        caption=repo_caption,
        reply_markup=reply_markup
    )
