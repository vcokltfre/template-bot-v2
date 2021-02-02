import asyncio
from aiohttp import ClientSession
from requests import post
from datetime import datetime
from termcolor import colored
from logging import debug, info, warn, error, critical

termc = {
    "debug": "white",
    "info": "green",
    "warn": "yellow",
    "error": "red",
    "critical": "red",
}


class LogLevel:
    DEBUG = 5
    INFO = 4
    WARNING = 3
    ERROR = 2
    CRITICAL = 1


class WebhookLogger:
    def __init__(
        self,
        name: str,
        url: str = None,
        level: int = LogLevel.INFO,
        loop=asyncio.get_event_loop(),
    ):
        self.name = name
        self.url = url
        self.level = level
        self.sess = ClientSession()
        self.loop = loop

    def create_content(self, logtype: str, content: str):
        timestamp = str(datetime.now()).split(".")[0]
        content = f"__**{logtype}**__ @ {timestamp}:\n{content}"
        data = {
            "username": self.name,
            "avatar_url": "https://vcokltfre.github.io/static/img/service.png",
            "content": content,
            "allowed_mentions": {"users": False, "roles": False, "everyone": False},
        }
        return data

    def send(self, logtype: str, content: str):
        print(colored(f"[{logtype}] {content}", termc[logtype.lower()]))
        if not self.url:
            return
        data = self.create_content(logtype, content)
        post(self.url, json=data)

    async def send_async(self, logtype: str, content: str):
        print(colored(f"[{logtype}] {content}", termc[logtype.lower()]))
        if not self.url:
            return
        data = self.create_content(logtype, content)
        if self.sess.closed:
            self.sess = ClientSession()

        task = self.loop.create_task(self.sess.post(self.url, json=data))
        task

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
