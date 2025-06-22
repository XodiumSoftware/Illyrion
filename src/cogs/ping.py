#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
from discord.ext import commands

from src.utils import Utils


class Ping(commands.Cog):
    """
    A cog for handling Ping-related commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        description="Sends the bot's latency.",
        default_member_permissions=discord.Permissions(administrator=True),
    )
    async def ping(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="Pong! 🏓",
                description=f"Latency: `{Utils.latency_ms(self.bot):.2f} ms`",
                color=Utils.get_latency_color(Utils.latency_ms(self.bot)),
            ),
            ephemeral=True,
        )


def setup(bot):
    bot.add_cog(Ping(bot))
