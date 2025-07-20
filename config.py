import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ───── Basic Bot Configuration ───── #
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", 5555422614))
OWNER_USERNAME = getenv("OWNER_USERNAME", "MrPerfectXd")
BOT_USERNAME = getenv("BOT_USERNAME", "TomXJerry_Bot")
BOT_NAME = getenv("BOT_NAME", "˹● 𝑻𝑶𝑴 ✘ 𝑱𝑬𝑹𝑹𝒀 𝑴𝑼𝑺𝑰𝑪 ●˼™ 🫧")
ASSUSERNAME = getenv("ASSUSERNAME", "TomXJerry0")
EVALOP = list(map(int, getenv("EVALOP", "6797202080").split()))

# ───── Mongo & Logging ───── #
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", -1002645692318))

# ───── Limits and Durations ───── #
RESTART_INTERVAL = int(getenv("RESTART_INTERVAL", 86400))  # default 24 hours
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ───── Custom API Configs ───── #
API_URL = getenv("API_URL") #optional
API_KEY = getenv("API_KEY") #optional
COOKIE_URL = getenv("COOKIE_URL") #necessary
DEEP_API = getenv("DEEP_API") #optional

# ───── Heroku Configuration ───── #
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ───── Git & Updates ───── #
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Mrperfectxd/Titan-Tom")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")

# ───── Support & Community ───── #
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TitanNetwrk")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Telugu_Grpz")

# ───── Assistant Auto Leave ───── #
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

# ───── Error Handling ───── #
DEBUG_IGNORE_LOG =True

# ───── Spotify Credentials ───── #
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ───── Session Strings ───── #
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ───── Server Settings ───── #
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))

# ───── Bot Media Assets ───── #

START_VIDS = [
    "https://files.catbox.moe/00ar3w.mp4",
    "https://files.catbox.moe/00ar3w.mp4",
    "https://files.catbox.moe/00ar3w.mp4"
]

STICKERS = [
    "CAACAgUAAx0Cd6nKUAACASBl_rnalOle6g7qS-ry-aZ1ZpVEnwACgg8AAizLEFfI5wfykoCR4h4E",
    "CAACAgUAAx0Cd6nKUAACATJl_rsEJOsaaPSYGhU7bo7iEwL8AAPMDgACu2PYV8Vb8aT4_HUPHgQ"
]
HELP_IMG_URL = "https://telegra.ph/file/c316aa782ab03f45ba9c2.jpg"
PING_VID_URL = "https://files.catbox.moe/00ar3w.mp4"
PLAYLIST_IMG_URL = "https://telegra.ph/file/64dacee61bdf2365497ef.jpg"
STATS_VID_URL = "https://files.catbox.moe/00ar3w.mp4"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/2879947fdf1397639a867.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/00ar3w.mp4"
STREAM_IMG_URL = "https://telegra.ph/file/2879947fdf1397639a867.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/2879947fdf1397639a867.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/2879947fdf1397639a867.jpg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ───── Utility & Functional ───── #
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── Bot Introduction Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🌈", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌", "🧨"]
AYUV = [
    "<b>🎶 ʜᴇʏ {0},</b>\n\n<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {1} ♪</b>\n\n<b>➤ ʏᴏᴜʀ ᴘᴇʀꜱᴏɴᴀʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ</b>\n\n<b>🎧 ɴᴏᴡ ᴘʟᴀʏɪɴɢ :</b> ʏᴏᴜᴛᴜʙᴇ • sᴘᴏᴛɪꜰʏ • ʀᴇꜱꜱᴏ • ᴀᴘᴘʟᴇ\n\n<b>🔎 ᴛᴀᴘ ʜᴇʟᴘ ꜰᴏʀ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ</b>",
    "<b>🎶 ʜᴇʏ {0},</b>\n\n<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {1} ♪</b>\n\n<b>➤ ʏᴏᴜʀ ᴘᴇʀꜱᴏɴᴀʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ</b>\n\n<b>🎧 ɴᴏᴡ ᴘʟᴀʏɪɴɢ :</b> ʏᴏᴜᴛᴜʙᴇ • sᴘᴏᴛɪꜰʏ • ʀᴇꜱꜱᴏ • ᴀᴘᴘʟᴇ\n\n<b>🔎 ᴛᴀᴘ ʜᴇʟᴘ ꜰᴏʀ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ</b>",
]

# ───── Runtime Structures ───── #
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ───── URL Validation ───── #
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
