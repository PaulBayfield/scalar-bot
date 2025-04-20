import discord

from discord.ext import commands
from textwrap import shorten


class Events(commands.Cog):
    """
    Events handler.
    """
    def __init__(self, client: discord.Client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot or message.guild is None or message.author.id == self.client.user.id or message.content == "":
            return

        if message.channel.id == self.client.config.channel_general:
            messages = [msg async for msg in message.channel.history(limit=10)]

            if len(messages) == 1:
                embed = discord.Embed(
                    title="New thread",
                    description=f"Hello {message.author.mention}!\n\nThis thread was automatically created after you sent your first message in the general channel.\nFeel free to continue the conversation here if you need help or have any questions.\n\nSomeone will answer you as soon as possible.\n\nThank you!",
                    color=self.client.config.embed_colour,
                )
                embed.set_footer(
                    text=self.client.config.footer_text,
                    icon_url=self.client.user.avatar.url,
                )

                thread = await message.create_thread(
                    name=shorten(message.content, width=94, placeholder=" [...]"),
                    reason=f"Thread created by {message.author} after first message in the general channel.",
                )
                await thread.send(
                    embed=embed
                )
        elif message.channel.id == self.client.config.channel_introductions:
            await message.add_reaction("👋")
        elif message.channel.id == self.client.config.channel_showcase:
            await message.add_reaction("🔥")


async def setup(client: discord.Client):
    await client.add_cog(Events(client))
