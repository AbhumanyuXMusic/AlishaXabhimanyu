import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ElrixXMusic")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/ccdb7dd3392bc90248472.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "ELrixXBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ElrixXAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Dramaa_Club")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Sanki_BOTs")
OWNER_NAME = getenv("OWNER_NAME", "Oo_Elrix") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "Oo_Elrix")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
