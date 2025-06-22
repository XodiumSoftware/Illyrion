#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
from discord.ext import commands


class IP(commands.Cog):
    """
    A cog for handling IP-related commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Returns the server IP address.")
    async def ip(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="ℹ️ Server IP:",
                description="`illyria.xodium.org`",
                color=discord.Color.blue(),
            )
        )


def setup(bot):
    bot.add_cog(IP(bot))
