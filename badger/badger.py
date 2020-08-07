import datetime

from aiohttp import ClientSession
from discord.ext.commands import Bot


class Badger(Bot):
    PREFIX = '/'
    http_session = ClientSession()

    async def on_error(self, event, *args, **kwargs):
        await super().on_error(event, *args, **kwargs)
        # We will use this hook to log the errors

    async def on_ready(self):
        print('Starting bot at:', datetime.datetime.now())
