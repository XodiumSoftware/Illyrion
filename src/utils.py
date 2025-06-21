#   Copyright (c) 2025. Xodium.
#   All rights reserved.

import functools
import glob
import logging
import os
from datetime import datetime
from zipfile import ZipFile

import discord


class Utils:
    """
    Utility class containing various helper methods for the Discord bot.
    """

    @staticmethod
    def latency_ms(bot):
        """
        Calculate the latency of the bot in milliseconds.

        Args:
            bot (discord.AutoShardedBot): The Discord bot instance.

        Returns:
            float: The latency in milliseconds.
        """
        return bot.latency * 1000

    @staticmethod
    def get_latency_color(latency_ms):
        """
        Determine the color based on the bot's latency.

        Args:
            latency_ms (float): The latency in milliseconds.

        Returns:
            discord.Color: Green for low latency, gold for moderate latency, and red for high latency.
        """
        if latency_ms < 100:
            return discord.Color.green()
        elif latency_ms < 200:
            return discord.Color.gold()
        else:
            return discord.Color.red()

    @staticmethod
    def log_command_usage(command):
        """
        Decorator to log the usage of bot commands, reading directly from the command object.

        Args:
            command (discord.ext.commands.Command): The command object.

        Returns:
            function: The wrapped function with logging functionality.
        """
        original_callback = command.callback

        @functools.wraps(original_callback)
        async def wrapper(ctx, *args, **kwargs):
            logging.info(
                f"@{ctx.author} (ID={ctx.author.id}) used /{ctx.command.name} in #{ctx.channel} (ID={ctx.channel.id})"
            )
            return await original_callback(ctx, *args, **kwargs)

        command.callback = wrapper
        return command

    @staticmethod
    def format_uptime(duration):
        """
        Format a duration into a human-readable uptime string.

        Args:
            duration (datetime.timedelta): The duration to format.

        Returns:
            str: A formatted string representing the uptime (e.g., "1d 2h 3m 4s").
        """
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
        if seconds >= 1:
            parts.append(f"{int(seconds)}s")

        return " ".join(parts)

    @staticmethod
    def setup_logging(log_dir, log_file, max_archived_logs, log_level):
        """
        Set up logging for the application, including archiving old logs.

        Args:
            log_dir (str): The directory where logs are stored.
            log_file (str): The name of the current log file.
            max_archived_logs (int): The maximum number of archived logs to keep.
            log_level (int): The logging level (e.g., logging.INFO).

        Returns:
            None
        """
        os.makedirs(log_dir, exist_ok=True)
        latest_log_path = os.path.join(log_dir, log_file)
        if os.path.exists(latest_log_path):
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            zip_path = os.path.join(log_dir, f"{timestamp}.zip")
            with ZipFile(zip_path, "w") as zipf:
                zipf.write(latest_log_path, arcname=log_file)
            os.remove(latest_log_path)
            zip_files = sorted(
                glob.glob(os.path.join(log_dir, "*.zip")),
                key=os.path.getmtime,
                reverse=True,
            )
            for old_zip in zip_files[max_archived_logs:]:
                os.remove(old_zip)

        logger = logging.getLogger()
        logger.setLevel(log_level)

        # File handler
        file_handler = logging.FileHandler(latest_log_path)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
            )
        )
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
            )
        )
        logger.addHandler(console_handler)
