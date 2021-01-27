from discord.ext import commands
from typing import List


class Bot(commands.Bot):
    """A subclassed version of commands.Bot"""

    def __init__(self, name: str, command_prefix, *args, **kwargs):
        self.name = name
        super().__init__(command_prefix=command_prefix, *args, **kwargs)

        # TODO: Logging initialisation

    def load_initial_cogs(self, cogs: List[str]):
        """Loads the initial cogs"""

        success, failed = 0, 0

        for cog in cogs:
            try:
                super().load_extension(cog)
                success += 1
            except Exception as e:
                # TODO: Log error
                failed += 1

        # TODO: Log cog load stats
