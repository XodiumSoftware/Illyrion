#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import functools

import discord


class Utils:
    @staticmethod
    def latency_ms(bot):
        return bot.latency * 1000

    @staticmethod
    def get_latency_color(latency_ms):
        if latency_ms < 100:
            return discord.Color.green()
        elif latency_ms < 200:
            return discord.Color.gold()
        else:
            return discord.Color.red()

    @staticmethod
    def log_command_usage(func):
        @functools.wraps(func)
        async def wrapper(ctx, *args, **kwargs):
            print(
                f"[LOG] @{ctx.author} (ID={ctx.author.id}) used /{ctx.command.name} in #{ctx.channel} (ID={ctx.channel.id})."
            )
            return await func(ctx, *args, **kwargs)

        return wrapper

    @staticmethod
    def format_uptime(duration):
        days, remainder = divmod(duration.total_seconds(), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        parts = []
        if days > 0:
            parts.append(f"{int(days)}d")
        if hours > 0:
            parts.append(f"{int(hours)}h")
        if minutes > 0:
            parts.append(f"{int(minutes)}m")
        if seconds > 0:
            parts.append(f"{int(seconds)}s")

        return " ".join(parts)
