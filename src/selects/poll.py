import discord


class PollSelect(discord.ui.Select):
    """The select menu for the poll."""

    def __init__(self, options: list[str], votes: dict[str, list[int]]):
        select_options = [discord.SelectOption(label=opt) for opt in options]
        super().__init__(placeholder="Cast your vote...", options=select_options)
        self.votes = votes

    async def callback(self, interaction: discord.Interaction):
        """Handles a selection from the dropdown."""
        if interaction.user is None:
            await interaction.response.send_message(
                "Could not determine user.", ephemeral=True
            )
            return

        user_id = interaction.user.id
        selected_option = str(self.values[0])

        if any(user_id in voters for voters in self.votes.values()):
            await interaction.response.send_message(
                "You have already voted.", ephemeral=True
            )
            return

        self.votes[selected_option].append(user_id)
        self.disabled = True
        self.placeholder = "You have already voted"

        await interaction.response.edit_message(
            embed=self.view.get_embed(), view=self.view
        )
