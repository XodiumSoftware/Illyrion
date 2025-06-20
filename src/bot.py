#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import os
from functools import wraps

import discord
from discord import Intents, Interaction, Object
from discord.app_commands import CommandTree
from dotenv import load_dotenv

def log_cmd(func):
    @wraps(func)
    async def wrapper(interaction: Interaction, *args, **kwargs):
        cmd_name = func.__name__
        print(f'Command "{cmd_name}" used by @{interaction.user} ({interaction.user.id}) in #{interaction.channel} ({interaction.channel.id})')
        response = await func(interaction, *args, **kwargs)
        print(f'Responded with "{response}" to @{interaction.user} ({interaction.user.id}) in #{interaction.channel} ({interaction.channel.id})')
        return response
    return wrapper

class Bot(discord.Client):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        load_dotenv()

        self.token = os.getenv('DISCORD_BOT_TOKEN')
        if not self.token: raise ValueError("DISCORD_BOT_TOKEN is not set in the .env file")

        self.tree = CommandTree(self)
        self.guild = Object(id=691029695894126623)

    async def setup_hook(self):
        @log_cmd
        @self.tree.command(name="test", description="Responds with pong")
        async def ping(interaction: Interaction):
            await interaction.channel.send("pong")

        await self.tree.sync(guild=self.guild)

    async def on_ready(self): print(f'Logged on as {self.user} ({self.user.id})')

    def run(self, **kwargs):
        super().run(self.token)

if __name__ == '__main__':
    Bot().run()
