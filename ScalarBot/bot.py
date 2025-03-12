import discord

from .utils.config import Config
from discord.ext import commands
from os import listdir, environ
from aiohttp import ClientSession
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")


class Bot(commands.Bot):
    """
    Bot
    """
    session: ClientSession

    def __init__(self):
        intents = discord.Intents(
            messages = True,
            message_content = True,
            members = True,
            guilds = True
        )
        super().__init__(
            command_prefix = commands.when_mentioned_or("!"), 
            intents=intents, 
            help_command = None,
            owner_ids = [
                852846322478219304, # @polo_byd
                1128013199933964378, # @scalar_employee_01 (aka Marc)
            ],
            allowed_mentions = discord.AllowedMentions(
                everyone=False, 
                users=False, 
                roles=False, 
                replied_user=True
            ),
            slash_commands = True,
            activity = discord.CustomActivity(name="scalar.com"),
            status = discord.Status.online
        )


        self.config = Config(environ)


    async def setup_hook(self) -> None:
        """
        Setup
        """
        for file in listdir("./ScalarBot/cogs"):
            if file.endswith(".py") and not file.startswith("_"):
                try:
                    await self.load_extension(f"ScalarBot.cogs.{file[:-3]}")
                    print(f"Loaded {file[:-3]} cog")
                except Exception as e:
                    print(f"Error loading {file[:-3]} cog: {e}")


    async def on_ready(self) -> None:
        """
        When the bot is ready
        """
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("ScalarBot is now online!")


    async def close(self) -> None:
        """
        Shutdown the bot
        """
        await self.session.close()
        await super().close()
