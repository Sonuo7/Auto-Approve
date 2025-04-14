from os import environ

API_ID = int(environ.get("API_ID", "28137469"))
API_HASH = environ.get("API_HASH", "3b33568aa7119719d1f37cb15b3ae587")
BOT_TOKEN = environ.get("BOT_TOKEN", "7998385476:AAGZatpVbPDoCZTA_X6OMTgEdzrJRP-Q-Mo")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002169575469"))
ADMINS = int(environ.get("ADMINS", "897584437"))
DB_URI = environ.get("DB_URI", "mongodb+srv://sonuoj:sonuhij@cluster0.a9dkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
IS_FSUB = bool(environ.get("FSUB", True))
AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "-1002189546391")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]
