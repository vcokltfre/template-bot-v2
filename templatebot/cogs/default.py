import time
from datetime import timedelta
from discord.ext import commands

from templatebot import Bot


class Default(commands.Cog):
    """A general purpose cog for tasks like cog loading, reloading, and unloading."""

    def __init__(self, bot: Bot):
        self.bot = bot
        self.ltime = time.time()

    @commands.group(name="cogs")
    @commands.is_owner()
    async def cogs_group(self, ctx: commands.Context):
        """Perform actions such as reloading cogs"""
        if ctx.invoked_subcommand is None:
            await ctx.send(f"Usage: `!cogs <load | reload | unload> [list of cogs]`")

    @cogs_group.command(name="load")
    async def load_cogs(self, ctx: commands.Context, *cognames):
        """Load a set of cogs"""
        log = ""
        for cog in cognames:
            cog = "bot.cogs." + cog
            try:
                self.bot.load_extension(cog)
                log += f"Successfully loaded cog {cog}\n"
            except Exception as e:
                log += f"Failed to load cog {cog}: {e}\n"
                self.bot.logger.error(f"Cog loading: failed to load {cog}: {e}")

        self.bot.logger.info(f"Loaded cog(s):\n{log}")
        await ctx.send(log)

    @cogs_group.command(name="reload")
    async def reload_cogs(self, ctx: commands.Context, *cognames):
        """Reload a set of cogs"""
        log = ""
        for cog in cognames:
            cog = "bot.cogs." + cog
            try:
                self.bot.reload_extension(cog)
                log += f"Successfully reloaded cog {cog}\n"
            except Exception as e:
                log += f"Failed to reload cog {cog}: {e}\n"
                self.bot.logger.error(f"Cog reloading: failed to reload {cog}: {e}")

        self.bot.logger.info(f"Reloaded cog(s):\n{log}")
        await ctx.send(log)

    @cogs_group.command(name="unload")
    async def unload_cogs(self, ctx: commands.Context, *cognames):
        """Unload a set of cogs"""
        log = ""
        for cog in cognames:
            cog = "bot.cogs." + cog
            try:
                self.bot.unload_extension(cog)
                log += f"Successfully unloaded cog {cog}\n"
            except Exception as e:
                log += f"Failed to unload cog {cog}: {e}\n"
                self.bot.logger.error(f"Cog unloading: failed to unload {cog}: {e}")

        self.bot.logger.info(f"Unloaded cog(s):\n{log}")
        await ctx.send(log)

    @commands.command(name="restart", aliases=["reboot", "shutdown"])
    @commands.is_owner()
    async def restart(self, ctx: commands.Context):
        """Make the bot logout"""
        await ctx.send("Restarting...")
        self.bot.logger.info(f"Shutting down {self.bot.name}")
        await self.bot.close()

    @commands.command(name="ping")
    @commands.is_owner()
    async def ping(self, ctx: commands.Context):
        """Get the bot's current API ping and websocket latency"""
        t_start = time.time()
        m = await ctx.channel.send("Testing RTT for message editing.")
        await m.edit(content="Testing...")
        rtt = time.time() - t_start
        await m.edit(
            content=f"Pong!\nMessage edit RTT: {round(rtt * 1000, 2)}ms\nWebsocket Latency: {round(self.bot.latency * 1000, 2)}ms"
        )

    @commands.command(name="uptime")
    @commands.is_owner()
    async def uptime(self, ctx: commands.Context):
        """Get the bot's current uptime"""
        bot_uptime = timedelta(seconds=round(time.time() - self.bot.ltime))
        cog_uptime = timedelta(seconds=round(time.time() - self.ltime))
        await ctx.send(f"Bot uptime: {bot_uptime}\nCog load uptime: {cog_uptime}")

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.logger.info(
            f"{self.bot.name} has received READY event, logged in as {self.bot.user} ({self.bot.user.id})"
        )


def setup(bot: Bot):
    bot.add_cog(Default(bot))
