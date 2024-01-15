import os

API_ID = API_ID =22609670

API_HASH = os.environ.get("API_HASH", "3506d8474ad1f4f5e79b7c52a5c3e88d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6334241757:AAHo1iSa_LcjP6jbbEO-Wz1H8wp9Oj9tZSk")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 6567662829))
LOG = -1002021098463,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6981453498").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
