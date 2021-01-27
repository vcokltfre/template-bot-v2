# vcokltfre/template-bot-v2

## A rewrite of [TemplateBot](https://github.com/vcokltfre/TemplateBot) with improvements

Usage:
```py
from templatebot import Bot

bot = Bot(name="MyBot", command_prefix="!")
bot.load_initial_cogs() # Required, even when empty, to load the default cog and jishaku
bot.run("token")
```

### Logging

The bot has two types of logging, synchronoush and asynchronous. Generally speaking you will want to use async logging, since it won't block while you're running the bot, however if you're logging something before running the bot, you may want to use the sync methods. These methods can be accessed through `templatebot.Bot.logger`

```py
class WebhookLogger:
    ...

    ## Synchronous methods

    def debug_s(self, content):
        self.send("debug", content)

    def info_s(self, content):
        self.send("info", content)

    def warn_s(self, content):
        self.send("warn", content)

    def error_s(self, content):
        self.send("error", content)

    def critical_s(self, content):
        self.send("critical", content)

    ## Asynchronous methods

    async def debug(self, content):
        await self.send_async("debug", content)

    async def info(self, content):
        await self.send_async("info", content)

    async def warn(self, content):
        await self.send_async("warn", content)

    async def error(self, content):
        await self.send_async("error", content)

    async def critical(self, content):
        await self.send_async("critical", content)
```