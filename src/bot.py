#   Copyright (c) 2025. Xodium.
#   All rights reserved.
import logging
import os
from datetime import datetime

import discord
import dotenv

from src.utils import Utils

dotenv.load_dotenv()


class Bot:
    """
    Main class for the Discord bot, handling initialization, event setup, and command definitions.
    """

    LOGGING_PATH = "/data/logs/latest.log"

    def __init__(self):
        self.GUILD_ID = os.getenv("GUILD_ID")
        self.TOKEN = os.getenv("TOKEN")

        if not self.TOKEN:
            raise ValueError(
                "No TOKEN found in environment variables. Please set the TOKEN variable."
            )
        if not self.GUILD_ID:
            raise ValueError(
                "No GUILD_ID found in environment variables. Please set the GUILD_ID variable."
            )

        self.start_time = datetime.now()
        self.logger = logging.getLogger()
        self.bot = discord.AutoShardedBot(debug_guilds=[int(self.GUILD_ID)])

        Utils.setup_logging(self.LOGGING_PATH, 10, logging.INFO)

        self.setup_events()
        self.load_cogs()
        self.bot.run(self.TOKEN)

    def load_cogs(self):
        """
        Dynamically load all cogs from the 'src/cogs' directory.
        """
        for filename in os.listdir("./src/cogs"):
            if filename.endswith(".py"):
                try:
                    self.bot.load_extension(f"src.cogs.{filename[:-3]}")
                    self.logger.info(f"Loaded cog: {filename}")
                except Exception as e:
                    self.logger.error(f"Failed to load cog {filename}: {e}")

    def setup_events(self):
        """
        Set up event handlers for the bot, including on_ready and before_invoke.
        """
        @self.bot.event
        async def on_ready():
            self.logger.info(
                f"{self.bot.user} (ID={self.bot.user.id}) is ready and online!"
            )

        @self.bot.before_invoke
        async def on_before_invoke(ctx: discord.ApplicationContext):
            self.logger.info(
                f"@{ctx.author} (ID={ctx.author.id}) used /{ctx.command.name} in #{ctx.channel} (ID={ctx.channel.id})"
            )


if __name__ == "__main__":
    Bot()
