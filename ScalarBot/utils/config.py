from datetime import datetime


class Config:
    def __init__(self, environ: dict):
        self.environ = environ

        self.channel_general = int(environ.get("DISCORD_CHANNEL_GENERAL", 0))
        self.channel_introductions = int(environ.get("DISCORD_CHANNEL_INTRODUCTIONS", 0))
        self.channel_showcase = int(environ.get("DISCORD_CHANNEL_SHOWCASE", 0))
        self.embed_colour = int(environ.get("DISCORD_EMBED_COLOUR", 0), base=16)
        self.footer_text = f"© {datetime.now().year} Scalar • scalar.com" 
        self.discord_invite = environ.get("DISCORD_INVITE", "https://discord.gg/scalar")
