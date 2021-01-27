# vcokltfre/template-bot-v2

## A rewrite of [TemplateBot](https://github.com/vcokltfre/TemplateBot) with improvements

Usage:
```py
from templatebot import Bot

bot = Bot(name="MyBot", command_prefix="!")
bot.load_initial_cogs() # Required, even when empty, to load the default cog and jishaku
bot.run("token")
```