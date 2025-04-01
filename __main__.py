import asyncio
import logging
import logging.handlers

from ScalarBot.bot import Bot
from os import environ
from dotenv import load_dotenv
from aiohttp import ClientSession


load_dotenv(dotenv_path=".env")


async def main():
    """
    Start the bot
    """
    client = Bot()

    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    async with ClientSession() as session:
        async with client:
            client.session = session
            await client.start(environ["TOKEN"], reconnect=True)


asyncio.run(main())
