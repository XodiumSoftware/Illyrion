#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
from discord.ext import commands


class FaqView(discord.ui.View):
    """A view that contains buttons for the FAQ."""

    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label="Info", style=discord.ButtonStyle.primary)
    async def info_button(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content="Displays the server info.")

    @discord.ui.button(label="Colour Coding", style=discord.ButtonStyle.secondary)
    async def colour_coding_button(self, interaction: discord.Interaction):
        await interaction.response.edit_message(
            content="Explains the colour coding used in the bot."
        )

    @discord.ui.button(label="Metrics", style=discord.ButtonStyle.secondary)
    async def metrics_button(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content="Displays the bot's metrics.")


class Faq(commands.Cog):
    """A cog for Faq-related commands."""

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="faq", description="Displays the FAQ menu.")
    async def faq(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="ℹ️ help",
                description="Please select a category.",
                color=discord.Colour.blue(),
            ),
            view=FaqView(),
        )


def setup(bot):
    bot.add_cog(Faq(bot))
