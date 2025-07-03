#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
from discord.ext import commands

from src.views.poll import PollView


class Poll(commands.Cog):
    """A cog for Poll-related commands."""

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        description="Create a poll with up to 10 options using a dropdown.",
        default_member_permissions=discord.Permissions(administrator=True),
    )
    async def poll(
        self,
        ctx: discord.ApplicationContext,
        question: discord.Option(str, "The question for the poll."),
        options: discord.Option(str, "The poll options, separated by a semicolon (;)."),
    ):
        option_list = [opt.strip() for opt in options.split(";") if opt.strip()]

        if len(option_list) < 2:
            await ctx.send_response(
                "Please provide at least two options separated by ';'.", ephemeral=True
            )
            return

        if len(option_list) > 25:
            await ctx.send_response(
                "You can provide a maximum of 25 options.", ephemeral=True
            )
            return

        view = PollView(question, option_list, ctx.author)
        await ctx.send_response(embed=view.get_embed(), view=view)


def setup(bot):
    bot.add_cog(Poll(bot))
