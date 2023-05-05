from Config.config import  offset
from Object.bot import VKBot
# from vk_api.longpoll import VkLongPoll, VkEventType
# 
# from DB.database import *


def main():
    bot = VKBot(offset=offset)
    bot.start()


if __name__ == "__main__":
    main()
