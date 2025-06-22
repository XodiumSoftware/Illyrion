#   Copyright (c) 2025. Xodium.
#   All rights reserved.
import logging
import os
from datetime import datetime

import discord
import dotenv
import psutil

from src.utils import Utils

dotenv.load_dotenv()

class Bot:
    """
    Main class for the Discord bot, handling initialization, event setup, and command definitions.
    """

    LOGGING_PATH = os.path.join(os.path.dirname(__file__), "data", "logs", "latest.log")

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
        self.setup_commands()
        self.bot.run(self.TOKEN)

    def setup_events(self):
        @self.bot.event
        async def on_ready():
            self.logger.info(
                f"{self.bot.user} (ID={self.bot.user.id}) is ready and online!"
            )

    def setup_commands(self):
        @Utils.log_command
        @self.bot.command(
            description="Sends the bot's latency.",
            default_member_permissions=discord.Permissions(administrator=True),
        )
        async def ping(ctx):
            await ctx.send_response(
                embed=discord.Embed(
                    title="Pong! 🏓",
                    description=f"Latency: `{Utils.latency_ms(self.bot):.2f} ms`",
                    color=Utils.get_latency_color(Utils.latency_ms(self.bot)),
                ),
                ephemeral=True,
            )

        @Utils.log_command
        @self.bot.command(description="Returns the server IP address.")
        async def ip(ctx):
            await ctx.send_response(
                embed=discord.Embed(
                    title="ℹ️ Server IP:",
                    description="`illyria.xodium.org`",
                    color=discord.Color.blue(),
                )
            )

        @Utils.log_command
        @self.bot.command(
            description="Displays the bot's uptime.",
            default_member_permissions=discord.Permissions(administrator=True),
        )
        async def uptime(ctx):
            await ctx.send_response(
                embed=discord.Embed(
                    title="⌛ Bot Uptime",
                    description=f"Uptime: `{Utils.format_uptime(datetime.now() - self.start_time)}`",
                    color=discord.Color.green(),
                ),
                ephemeral=True,
            )

        @Utils.log_command
        @self.bot.command(
            description="Displays the bot's metrics.",
            default_member_permissions=discord.Permissions(administrator=True),
        )
        async def metrics(ctx):
            await ctx.send_response(
                embed=discord.Embed(
                    title="📈 Metrics",
                    description=(
                        f"Latency: `{Utils.latency_ms(self.bot):.2f} ms`\n"
                        f"CPU Usage: `{psutil.cpu_percent()}%`\n"
                        f"Memory Usage: `{psutil.virtual_memory().percent}%`"
                    ),
                    color=discord.Color.blue(),
                ),
                ephemeral=True,
            )

        @Utils.log_command
        @self.bot.command(description="Displays the server version.")
        async def version(ctx):
            await ctx.send_response(
                embed=discord.Embed(
                    title="ℹ️ Server Version:",
                    description="`1.21.6`",
                    color=discord.Color.blue(),
                )
            )

        @Utils.log_command
        @self.bot.command(description="Displays the link for color coding.")
        async def cc(ctx):
            await ctx.send_response(
                embed=discord.Embed(
                    title="ℹ️ Color Coding:",
                    description=(
                        "Website: `https://www.birdflop.com/resources/rgb/`\n"
                        "Color Format: `MiniMessage`\n"
                        "Usage: Play with the colors and then copy the output and paste it into the chat."
                    ),
                    color=discord.Color.blue(),
                )
            )


if __name__ == "__main__":
    Bot()
