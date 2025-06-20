#   Copyright (c) 2025. Xodium.
#   All rights reserved.

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
