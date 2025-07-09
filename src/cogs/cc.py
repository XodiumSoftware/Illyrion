import discord
from discord.ext import commands


class CC(commands.Cog):
    """A cog for handling CC-related commands."""

    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot

    @discord.slash_command(description="Explains the colour coding used on the server.")  # type: ignore
    async def cc(self, ctx: discord.ApplicationContext) -> None:
        await ctx.send_response(
            embed=discord.Embed(
                title="ℹ️ Color Coding:",
                description=(
                    "Website: https://www.birdflop.com/resources/rgb/\n"
                    "Color Format: `MiniMessage`\n"
                    "Usage: https://youtu.be/F43yRnvHICA"
                ),
                color=discord.Colour.blue(),
            )
        )


def setup(bot: commands.AutoShardedBot) -> None:
    bot.add_cog(CC(bot))
