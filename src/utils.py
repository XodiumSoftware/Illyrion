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
