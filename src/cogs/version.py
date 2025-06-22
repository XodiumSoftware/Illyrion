#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
from discord.ext import commands


class Version(commands.Cog):
    """
    A cog for handling Version-related commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Displays the server version.")
    async def version(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="ℹ️ Server Version:",
                description="`1.21.6`",
                color=discord.Color.blue(),
            )
        )


def setup(bot):
    bot.add_cog(Version(bot))
