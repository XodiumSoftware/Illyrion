#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import os

import discord
from dotenv import load_dotenv

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"[LOG] {bot.user} (ID={bot.user.id}) is ready and online!")

@bot.command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")
    print(f"[LOG] @{ctx.author} (ID={ctx.author.id}) used /ping in #{ctx.channel} (ID={ctx.channel.id}).")

load_dotenv()
token = os.environ.get("TOKEN")
if not token:
    raise ValueError("No TOKEN found in environment variables. Please set the TOKEN variable.")

bot.run(token)