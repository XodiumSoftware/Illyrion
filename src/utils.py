#   Copyright (c) 2025. Xodium.
#   All rights reserved.

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
    def setup_logging(logging_path, max_archived_logs, log_level):
        """
        Set up logging for the application, including archiving old logs.

        Args:
            logging_path (str): The full path to the current log file.
            max_archived_logs (int): The maximum number of archived logs to keep.
            log_level (int): The logging level (e.g., logging.INFO).

        Returns:
            None
        """
        log_dir = os.path.dirname(logging_path)
        os.makedirs(log_dir, exist_ok=True)
        if os.path.exists(logging_path):
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            zip_path = os.path.join(log_dir, f"{timestamp}.zip")
            with ZipFile(zip_path, "w") as zipf:
                zipf.write(logging_path, arcname=os.path.basename(logging_path))
            os.remove(logging_path)
            zip_files = sorted(
                glob.glob(os.path.join(log_dir, "*.zip")),
                key=os.path.getmtime,
                reverse=True,
            )
            for old_zip in zip_files[max_archived_logs:]:
                os.remove(old_zip)

        logger = logging.getLogger()
        logger.setLevel(log_level)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
        )

        # File handler
        file_handler = logging.FileHandler(logging_path)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
