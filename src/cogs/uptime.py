#   Copyright (c) 2025. Xodium.
#   All rights reserved.

from datetime import datetime

import discord
from discord.ext import commands

from src.utils import Utils


class Uptime(commands.Cog):
    """
    A cog for handling Uptime-related commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        description="Displays the bot's metrics.",
        default_member_permissions=discord.Permissions(administrator=True),
    )
    async def uptime(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="⌛ Bot Uptime",
                description=f"Uptime: `{Utils.format_uptime(datetime.now() - self.start_time)}`",
                color=discord.Color.green(),
            ),
            ephemeral=True,
        )


def setup(bot):
    bot.add_cog(Uptime(bot))
