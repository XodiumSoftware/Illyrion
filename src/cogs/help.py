#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
from discord.ext import commands


class Help(commands.Cog):
    """
    A cog for Help-related commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="help", description="")
    async def help(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="ℹ️ help",
                description="",
                color=discord.Color.blue(),
            )
        )


def setup(bot):
    bot.add_cog(Help(bot))
