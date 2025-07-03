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
        option11: discord.Option(str, "The eleventh option.", required=False),
        option12: discord.Option(str, "The twelfth option.", required=False),
        option13: discord.Option(str, "The thirteenth option.", required=False),
        option14: discord.Option(str, "The fourteenth option.", required=False),
        option15: discord.Option(str, "The fifteenth option.", required=False),
        option16: discord.Option(str, "The sixteenth option.", required=False),
        option17: discord.Option(str, "The seventeenth option.", required=False),
        option18: discord.Option(str, "The eighteenth option.", required=False),
        option19: discord.Option(str, "The nineteenth option.", required=False),
        option20: discord.Option(str, "The twentieth option.", required=False),
        option21: discord.Option(str, "The twenty-first option.", required=False),
        option22: discord.Option(str, "The twenty-second option.", required=False),
        option23: discord.Option(str, "The twenty-third option.", required=False),
        option24: discord.Option(str, "The twenty-fourth option.", required=False),
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
                option11,
                option12,
                option13,
                option14,
                option15,
                option16,
                option17,
                option18,
                option19,
                option20,
                option21,
                option22,
                option23,
                option24,
            ]
            if opt is not None
        ]

        view = PollView(question, options, ctx.author)
        await ctx.send_response(embed=view.get_embed(), view=view)


def setup(bot):
    bot.add_cog(Poll(bot))
