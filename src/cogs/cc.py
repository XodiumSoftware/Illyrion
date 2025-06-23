#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
from discord.ext import commands


class CC(commands.Cog):
    """A cog for handling CC-related commands."""

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Explains the colour coding used in the bot.")
    async def cc(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="ℹ️ Color Coding:",
                description=(
                    "Website: `https://www.birdflop.com/resources/rgb/`\n"
                    "Color Format: `MiniMessage`\n"
                    "Usage: Play with the colors and then copy the output and paste it into the chat."
                ),
                color=discord.Colour.blue(),
            )
        )


def setup(bot):
    bot.add_cog(CC(bot))
