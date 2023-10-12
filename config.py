import os

API_ID = API_ID =24250238 

API_HASH = os.environ.get("API_HASH", "cb3f118ce5553dc140127647edcf3720")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5900432090:AAGh66GjvNR0fnGCiOngV4rC5tg5pninmlU")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 6175650047))
LOG = -1001923813329,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6175650047").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
