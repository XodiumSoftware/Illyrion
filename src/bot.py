#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

class Bot:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('DISCORD_BOT_TOKEN')
        if not self.token:
            raise ValueError("DISCORD_BOT_TOKEN is not set in the .env file")

        intents = discord.Intents.default()
        intents.message_content = True

        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self._register_handlers()

    def _register_handlers(self):
        self.bot.event(self.on_ready)
        self.bot.command()(self.hello)

    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')

    @staticmethod
    async def hello(ctx):
        await ctx.send('Hello! I am your bot.')

    def run(self):
        self.bot.run(self.token)

if __name__ == "__main__":
    Bot().run()