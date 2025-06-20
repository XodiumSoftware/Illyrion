#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import os
from functools import wraps

import discord
from discord import Intents
from dotenv import load_dotenv

def log_cmd(cmd):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, message, *args, **kwargs):
            if message.author == self.user:
                return await func(self, message, *args, **kwargs)
            print(f'Command "{cmd}" used by @{message.author} ({message.author.id}) in #{message.channel} ({message.channel.id})')
            response = await func(self, message, *args, **kwargs)
            print(f'Responded with "{response}" to @{message.author} ({message.author.id}) in #{message.channel} ({message.channel.id})')
            return response
        return wrapper
    return decorator

class Bot(discord.Client):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        load_dotenv()

        self.token = os.getenv('DISCORD_BOT_TOKEN')
        if not self.token: raise ValueError("DISCORD_BOT_TOKEN is not set in the .env file")

    async def on_ready(self):
        print(f'Logged on as {self.user}')

    @log_cmd('ping')
    async def on_message(self, message):
        if message.author == self.user: return
        if message.content == 'ping':
            await message.channel.send('pong')

    def run(self, **kwargs):
        super().run(self.token)

if __name__ == '__main__':
    Bot().run()
