import discord
from discord.ext import commands

from src.utils import Utils
from src.views.poll import PollView


class Poll(commands.Cog):
    """A cog for Poll-related commands."""

    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot

    @discord.slash_command( # type: ignore
        description="Create a poll with up to 10 options using a dropdown.",
        default_member_permissions=discord.Permissions(administrator=True),
    )
    async def poll(
        self,
        ctx: discord.ApplicationContext,
        question: discord.Option(str, "The question for the poll."),
        options: discord.Option(str, "The poll options, separated by a semicolon (;)."),
        mention: discord.Option(
            discord.Role,
            "Role to mention with the poll.",
            required=False,
            default=None,
        ),
        deadline: discord.Option(
            str,
            "Poll deadline (e.g., 10s, 30m, 2h, 1d).",
            required=False,
            default=None,
        ),
    ):
        option_list: list[str] = [opt.strip() for opt in options.split(";") if opt.strip()]

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

        timeout = Utils.parse_duration(deadline)
        if deadline and timeout is None:
            await ctx.send_response(
                "Invalid deadline format. Use 'm' for minutes, 'h' for hours, 'd' for days (e.g., 30m, 2h, 1d).",
                ephemeral=True,
            )
            return

        view = PollView(question, option_list, ctx.author, timeout=timeout)
        content = mention.mention if mention else None
        await ctx.send_response(content=content, embed=view.get_embed(), view=view)
        view.message = await ctx.interaction.original_response()


def setup(bot: commands.AutoShardedBot) -> None:
    bot.add_cog(Poll(bot))
