#   Copyright (c) 2025. Xodium.
#   All rights reserved.
import logging
import os
from datetime import datetime
from zipfile import ZipFile

import discord
from dotenv import load_dotenv


class Bot:
    def __init__(self):
        self.logger = logging.getLogger()
        self.bot = discord.Bot()
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

    def setup_commands(self):
        @self.bot.command(description="Sends the bot's latency.")
        async def ping(ctx):
            await ctx.respond(embed=discord.Embed(
                title="Pong! 🏓",
                description=f"Latency is `{self.latency_ms():.2f} ms`",
                color=self.get_latency_color(self.latency_ms())
            ))
            print(
                f"[LOG] @{ctx.author} (ID={ctx.author.id}) used /{ctx.command.name} in #{ctx.channel} (ID={ctx.channel.id}).")

    def run(self):
        load_dotenv()
        token = os.environ.get("TOKEN")
        if not token:
            raise ValueError("No TOKEN found in environment variables. Please set the TOKEN variable.")
        self.bot.run(token)

    def latency_ms(self):
        return self.bot.latency * 1000

    @staticmethod
    def get_latency_color(latency_ms):
        if latency_ms < 100:
            return discord.Color.green()
        elif latency_ms < 200:
            return discord.Color.gold()
        else:
            return discord.Color.red()


if __name__ == "__main__":
    Bot().run()
