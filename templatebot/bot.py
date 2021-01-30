from time import time
from discord.ext import commands
from typing import List

from .utils.logger import WebhookLogger, LogLevel


class Bot(commands.Bot):
    """A subclassed version of commands.Bot"""

    def __init__(
        self,
        name: str,
        command_prefix,
        logging_url: str = None,
        loglevel: int = LogLevel.INFO,
        *args,
        **kwargs,
    ):
        self.name = name
        self.ltime = time()
        super().__init__(command_prefix=command_prefix, *args, **kwargs)

        self.logger = WebhookLogger(name=name, url=logging_url, level=loglevel)

    def load_initial_cogs(self, *cogs):
        """Loads the initial cogs"""

        success, failed = 0, 0

        cogs = set(cogs)
        cogs.add("templatebot.cogs.default")
        cogs.add("jishaku")

        for cog in cogs:
            try:
                super().load_extension(cog)
                success += 1
            except Exception as e:
                self.logger.error_s(
                    f"Cog {cog} experienced an error during loading: {e}"
                )
                failed += 1

        self.logger.info_s(
            f"Cog loading complete! (Total: {success + failed} | Loaded: {success} | Failed: {failed})"
        )
