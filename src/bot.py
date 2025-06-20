#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import os

import discord
from dotenv import load_dotenv
from datetime import datetime

class Bot:
    def __init__(self):
        self.bot = discord.Bot()
        self.setup_logging()
        self.setup_events()
        self.setup_commands()

    def setup_logging(self):
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
        self.logger = logging.getLogger()

    def setup_events(self):
        @self.bot.event
        async def on_ready():
            print(f"[LOG] {self.bot.user} (ID={self.bot.user.id}) is ready and online!")

    def setup_commands(self):
        @self.bot.command(description="Sends the bot's latency.")
        async def ping(ctx):
            await ctx.respond(f"Pong! Latency is {self.bot.latency}")
            print(f"[LOG] @{ctx.author} (ID={ctx.author.id}) used /{ctx.command.name} in #{ctx.channel} (ID={ctx.channel.id}).")

    def run(self):
        load_dotenv()
        token = os.environ.get("TOKEN")
        if not token:
            raise ValueError("No TOKEN found in environment variables. Please set the TOKEN variable.")
        self.bot.run(token)

if __name__ == "__main__":
    Bot().run()