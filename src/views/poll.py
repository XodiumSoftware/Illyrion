#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord

from src.selects.poll import PollSelect


class PollView(discord.ui.View):
    """A view for the poll, containing the voting dropdown."""

    def __init__(self, question, options, author):
        super().__init__(timeout=None)
        self.question = question
        self.options = options
        self.author = author
        self.votes = {option: [] for option in self.options}
        self.add_item(PollSelect(options=self.options, votes=self.votes))

    def get_embed(self):
        """Creates the poll embed with the current vote counts."""
        description = []
        total_votes = sum(len(voters) for voters in self.votes.values())
        for option, voters in self.votes.items():
            vote_count = len(voters)
            percentage = (
                f"({(vote_count / total_votes) * 100:.1f}%)" if total_votes > 0 else ""
            )
            description.append(f"**{option}**: {vote_count} vote(s) {percentage}")

        embed = discord.Embed(
            title=f"📊 {self.question}",
            description="\n".join(description),
            color=discord.Colour.blue(),
        )
        embed.set_footer(text=f"Poll created by {self.author.display_name}")
        return embed
