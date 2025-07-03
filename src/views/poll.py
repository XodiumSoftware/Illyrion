#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord


class PollView(discord.ui.View):
    """A view for the poll, containing the voting dropdown."""

    def __init__(self, question, options, author):
        super().__init__(timeout=None)
        self.question = question
        self.options = options
        self.author = author
        self.votes = {option: [] for option in self.options}

        select_options = [discord.SelectOption(label=opt) for opt in self.options]
        self.select_menu = discord.ui.Select(
            placeholder="Cast your vote...", options=select_options
        )
        self.select_menu.callback = self.select_callback
        self.add_item(self.select_menu)

    def get_embed(self):
        """Creates the poll embed with the current vote counts."""
        description = []
        for option, voters in self.votes.items():
            vote_count = len(voters)
            description.append(f"**{option}**: {vote_count} vote(s)")

        embed = discord.Embed(
            title=f"📊 {self.question}",
            description="\n".join(description),
            color=discord.Colour.blue(),
        )
        embed.set_footer(text=f"Poll created by {self.author.display_name}")
        return embed

    async def select_callback(self, interaction: discord.Interaction):
        """Handles a selection from the dropdown."""
        user_id = interaction.user.id
        selected_option = self.select_menu.values[0]

        for voters in self.votes.values():
            if user_id in voters:
                await interaction.response.send_message(
                    "You have already voted in this poll.", ephemeral=True
                )
                return

        self.votes[selected_option].append(user_id)

        await interaction.response.edit_message(embed=self.get_embed(), view=self)
