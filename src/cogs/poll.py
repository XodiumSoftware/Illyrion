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
        option1: discord.Option(str, "The first option."),
        option2: discord.Option(str, "The second option."),
        option3: discord.Option(str, "The third option.", required=False),
        option4: discord.Option(str, "The fourth option.", required=False),
        option5: discord.Option(str, "The fifth option.", required=False),
        option6: discord.Option(str, "The sixth option.", required=False),
        option7: discord.Option(str, "The seventh option.", required=False),
        option8: discord.Option(str, "The eighth option.", required=False),
        option9: discord.Option(str, "The ninth option.", required=False),
        option10: discord.Option(str, "The tenth option.", required=False),
    ):
        options = [
            opt
            for opt in [
                option1,
                option2,
                option3,
                option4,
                option5,
                option6,
                option7,
                option8,
                option9,
                option10,
            ]
            if opt is not None
        ]

        view = PollView(question, options, ctx.author)
        await ctx.send_response(embed=view.get_embed(), view=view)


def setup(bot):
    bot.add_cog(Poll(bot))
