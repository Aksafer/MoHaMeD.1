import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 29380940))
API_HASH = getenv("API_HASH", "a0d123fa03f3bf5e3942301ef74c04ab")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1900700 ))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6816180621))
DEVELOPERS = [6816180621]
OWNER_BOT = 6816180621

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Aksafer/MoHaMeD.1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SOURCE_EROR")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Y_D_ll")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/a0d8b418cbfe7fc6b780b.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/895e5649bccc12b4943f3.jpg"
STATS_IMG_URL = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"
AdRenalen_KleCha_play = "https://telegra.ph/file/f57c7937f483cb36e09bd.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
