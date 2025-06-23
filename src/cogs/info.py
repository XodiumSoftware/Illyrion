#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
from discord.ext import commands


class Info(commands.Cog):
    """
    A cog for handling Info-related commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Displays the server info.")
    async def info(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="ℹ️ Server Info:",
                description=("IP: `illyria.xodium.org`\nVersion: `1.21.6`"),
                color=discord.Color.blue(),
            )
        )


def setup(bot):
    bot.add_cog(Info(bot))
