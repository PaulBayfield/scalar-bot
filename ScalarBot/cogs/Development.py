from discord.ext import commands


class Development(commands.Cog):
    """
    Administration commands for the bot.
    """
    def __init__(self, client: commands.Bot):
        self.client = client


    @commands.command(help="sync", hidden=True)
    @commands.is_owner()
    async def sync(self, ctx: commands.Context):
        await self.client.tree.sync()
        await ctx.send("Done")


    @commands.command(help="logout", hidden=True)
    @commands.is_owner()
    async def logout(self, ctx: commands.Context):
        await ctx.send("Logging out...")
        await self.client.close()


    @commands.command(help="reload", hidden=True)
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, cog: str):
        try:
            await self.client.reload_extension(f"ScalarBot.cogs.{cog.title()}")
            await ctx.reply(f"Reloading module `{cog.title()}`")
        except Exception as e:
            await ctx.reply(f"Could not reload module `{cog.title()}` : `{e}`")


    @commands.command(help="load", hidden=True)
    @commands.is_owner()
    async def load(self, ctx: commands.Context, cog: str):
        try:
            await self.client.load_extension(f"ScalarBot.cogs.{cog.title()}")
            await ctx.reply(f"Loaded module `{cog.title()}`")
        except Exception as e:
            await ctx.reply(f"Could not load module `{cog.title()}` : `{e}`")


    @commands.command(help="unload", hidden=True)
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, cog: str):
        try:
            await self.client.unload_extension(f"ScalarBot.cogs.{cog.title()}")
            await ctx.reply(f"Unloaded module `{cog.title()}`")
        except Exception as e:
            await ctx.reply(f"Could not unload module `{cog.title()}` : `{e}`")


async def setup(client: commands.Bot):
    await client.add_cog(Development(client))
