class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 25614292
    API_HASH = "59ee8005ce6b056fa639d956f028eeeb"

    CASH_API_KEY = "4Z5UHYEW3LJ7U99J" # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://xrlkskby:gobwyeqocauwmdrggqom@alpha.mkdb.sh:5432/rjfvbvc"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002024032988)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://chalcogen:dumb980@cluster0.u25jq25.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/5618197d321f4f555bb9c.jpg"

    SUPPORT_CHAT = "kittybothub"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6909402640:AAEUXjuibT9DlAl72lSi3JtVFnwUWwG931Q"   # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "V33SSMCSDT6L" # Get this value from https://timezonedb.com/api

    OWNER_ID = 7006715434  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [7006715434]  # User id of sudo users
    DEV_USERS = [7006715434]  # User id of dev users
    DEMONS = [7006715434]  # User id of support users
    TIGERS = [7006715434]  # User id of tiger users
    WOLVES = [7006715434]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
