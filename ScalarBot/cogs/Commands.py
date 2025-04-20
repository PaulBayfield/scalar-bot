import discord

from discord import app_commands
from discord.ext import commands


class Commands(commands.Cog):
    """
    Bot commands for the Scalar bot.
    """
    def __init__(self, client: commands.Bot):
        self.client = client


    # /scalar

    @app_commands.command(name="scalar", description="Scalar information")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def scalar(
        self, 
        interaction: discord.Interaction,
    ):
        embed = discord.Embed(
            title="Scalar",
            description="The modern open-source developer experience platform for your APIs.\n\nCreate world-class API Docs with a built-in interactive playground which seamlessly turns to a full featured API Client",
            color=self.client.config.embed_colour,
        )
        embed.set_image(
            url="https://github.com/user-attachments/assets/7c4d4971-a6d9-457d-a7ab-11894889f6f9"
        )
        embed.set_footer(
            text=self.client.config.footer_text,
            icon_url=self.client.user.avatar.url,
        )

        button_website = discord.ui.Button(
            style=discord.ButtonStyle.link,
            label="Website",
            url="https://scalar.com",
        )
        button_docs = discord.ui.Button(
            style=discord.ButtonStyle.link,
            label="Documentation",
            url="https://guides.scalar.com",
        )
        button_github = discord.ui.Button(
            style=discord.ButtonStyle.link,
            label="Github",
            url="https://github.com/scalar/scalar",
        )
        button_discord = discord.ui.Button(
            style=discord.ButtonStyle.link,
            label="Discord",
            url=self.client.config.discord_invite,
        )

        view = discord.ui.View()
        view.add_item(button_website)
        view.add_item(button_docs)
        view.add_item(button_github)
        view.add_item(button_discord)

        await interaction.response.send_message(
            embed=embed,
            view=view,
        )


async def setup(client: commands.Bot):
    await client.add_cog(Commands(client))
