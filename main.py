from bot import client

from utils.logger import logger


if __name__ == "__main__":
    logger.info("START BOT")

    client.run()
