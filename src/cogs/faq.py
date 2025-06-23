#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import discord
from discord import Color, Interaction
from discord.ext import commands
from discord.types.components import ButtonStyle


class FaqView(discord.ui.View):
    """A view that contains buttons for the FAQ."""

    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label="General", style=ButtonStyle.primary)
    async def general_button(self, button: discord.ui.Button, interaction: Interaction):
        await interaction.response.edit_message(content="Here is the general FAQ.")

    @discord.ui.button(label="Commands", style=ButtonStyle.secondary)
    async def commands_button(
        self, button: discord.ui.Button, interaction: Interaction
    ):
        await interaction.response.edit_message(content="Here is the list of commands.")


class Faq(commands.Cog):
    """A cog for Faq-related commands."""

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="faq", description="")
    async def faq(self, ctx):
        await ctx.send_response(
            embed=discord.Embed(
                title="ℹ️ help",
                color=Color.blue(),
            )
        )


def setup(bot):
    bot.add_cog(Faq(bot))
