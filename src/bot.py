#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

bot.run("TOKEN")