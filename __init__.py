#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "29141829"
API_HASH = "25020d00fbcfd406fc9979d24d761bff"
BOT_TOKEN = "6998826537:AAE24A88dHWSxFLFQ5jFYs2Sq8UwDPtasug"
SESSION = "BQG8q0UAEbO1nOy4X5K_0Y_2iy72Yh42wPf_wA08yUZvK9GmSNJMrscxcYkr7fURZOLnZlgbVUDnYjXjVCNDGDlyQdocL4B3XyszSIW-iUGMsgLPlvkkEK_xQyns_iJFKlcQDJ3ER_BDIGbH5SxoRLkZvKTwnVmC3x8MY51ITbGXYeUQzsF2lKHPxvUaTOtH-VPsNy11oqfJHWKv7XFLB7gtgZ5-NJkH5AA-gpew8NMCO8xyw98_xUsmjsTuIbxGazXv7G1tKEwCPRzoJuL3Xv5eNXAldb8bpzh9UGFq3y93E0COjvgnCeNUmZAL9N7o3xkbUijMgC1YExUcz2fYMen7KixX9QAAAAE9TLQaAA"
FORCESUB = "jayhind_675"
AUTH = "5323404314"
SUDO_USERS = "5323404314"

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @galib_shayar.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
