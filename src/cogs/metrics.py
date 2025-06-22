#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
import psutil
from discord.ext import commands

from src.utils import Utils


class Metrics(commands.Cog):
    """
    A cog for handling Metrics-related commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        description="Displays the bot's metrics.",
        default_member_permissions=discord.Permissions(administrator=True),
    )
    async def metrics(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="📈 Metrics",
                description=(
                    f"Latency: `{Utils.latency_ms(self.bot):.2f} ms`\n"
                    f"CPU Usage: `{psutil.cpu_percent()}%`\n"
                    f"Memory Usage: `{psutil.virtual_memory().percent}%`"
                ),
                color=discord.Color.blue(),
            ),
            ephemeral=True,
        )


def setup(bot):
    bot.add_cog(Metrics(bot))
