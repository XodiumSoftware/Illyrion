#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import datetime

import discord

from src.selects.poll import PollSelect


class PollView(discord.ui.View):
    """A view for the poll, containing the voting dropdown."""

    def __init__(self, question, options, author, timeout=None):
        super().__init__(timeout=timeout)
        self.question = question
        self.options = options
        self.author = author
        self.votes = {option: [] for option in self.options}
        self.add_item(PollSelect(options=self.options, votes=self.votes))
        self.message = None
        if timeout:
            self.end_time = discord.utils.utcnow() + datetime.timedelta(seconds=timeout)
        else:
            self.end_time = None

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

        footer_text = f"Poll created by {self.author.display_name}"
        if self.end_time:
            footer_text += (
                f" | Ends {discord.utils.format_dt(self.end_time, style='R')}"
            )
        embed.set_footer(text=footer_text)
        return embed

    async def on_timeout(self):
        """Disables the view and updates the message when the poll ends."""
        for item in self.children:
            item.disabled = True

        embed = self.get_embed()
        embed.title = f"📊 {self.question} (Closed)"
        embed.colour = discord.Colour.red()
        embed.set_footer(text=f"Poll by {self.author.display_name} has ended.")

        if self.message:
            await self.message.edit(embed=embed, view=self)
