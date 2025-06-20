#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import glob
import logging
import os
from datetime import datetime
from zipfile import ZipFile

import discord
import dotenv
import psutil

dotenv.load_dotenv()

from src.utils import Utils


class Bot:
    GUILD_ID = os.environ.get("GUILD_ID")
    TOKEN = os.environ.get("TOKEN")

    def __init__(self):
        if not self.TOKEN:
            raise ValueError("No TOKEN found in environment variables. Please set the TOKEN variable.")
        if not self.GUILD_ID:
            raise ValueError("No GUILD_ID found in environment variables. Please set the GUILD_ID variable.")
        self.start_time = datetime.now()
        self.logger = logging.getLogger()
        self.bot = discord.Bot(debug_guilds=[int(self.GUILD_ID)])
        self.setup_logging()
        self.setup_events()
        self.setup_commands()

    @staticmethod
    def setup_logging():
        os.makedirs("logs", exist_ok=True)
        latest_log_path = "logs/latest.log"
        if os.path.exists(latest_log_path):
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            zip_path = f"logs/{timestamp}.zip"
            with ZipFile(zip_path, "w") as zipf:
                zipf.write(latest_log_path, arcname="latest.log")
            os.remove(latest_log_path)
            zip_files = sorted(
                glob.glob("logs/*.zip"),
                key=os.path.getmtime,
                reverse=True
            )
            for old_zip in zip_files[10:]:
                os.remove(old_zip)
        logging.basicConfig(
            filename=latest_log_path,
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    def setup_events(self):
        @self.bot.event
        async def on_ready():
            print(f"[LOG] {self.bot.user} (ID={self.bot.user.id}) is ready and online!")
            print(f"[LOG] Latency: {Utils.latency_ms(self.bot):.2f} ms")

    def setup_commands(self):
        @self.bot.command(description="Sends the bot's latency.",
                          default_member_permissions=discord.Permissions(administrator=True))
        @Utils.log_command_usage
        async def ping(ctx):
            await ctx.respond(embed=discord.Embed(
                title="Pong! 🏓",
                description=f"Latency is `{Utils.latency_ms(self.bot):.2f} ms`",
                color=Utils.get_latency_color(Utils.latency_ms(self.bot))
            ))

        @self.bot.command(description="Returns the server IP address.")
        @Utils.log_command_usage
        async def ip(ctx):
            await ctx.respond(embed=discord.Embed(
                title="Server IP Address",
                description="`illyria.xodium.org`",
                color=discord.Color.blue()
            ))

        @self.bot.command(description="Displays the bot's uptime.",
                          default_member_permissions=discord.Permissions(administrator=True))
        @Utils.log_command_usage
        async def uptime(ctx):
            await ctx.respond(embed=discord.Embed(
                title="Bot Uptime",
                description=f"Uptime: `{Utils.format_uptime(datetime.now() - self.start_time)}`",
                color=discord.Color.green()
            ))

        @self.bot.command(description="Displays the bot's metrics.",
                          default_member_permissions=discord.Permissions(administrator=True))
        @Utils.log_command_usage
        async def metrics(ctx):
            await ctx.respond(embed=discord.Embed(
                title="Metrics",
                description=(
                    f"Latency is `{Utils.latency_ms(ctx.bot):.2f} ms`\n"
                    f"CPU Usage: `{psutil.cpu_percent()}%`\n"
                    f"Memory Usage: `{psutil.virtual_memory().percent}%`"
                ),
                color=discord.Color.blue()
            ))


if __name__ == "__main__":
    Bot().bot.run(Bot.TOKEN)
