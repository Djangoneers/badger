import datetime

from aiohttp import ClientSession
from discord.ext.commands import Bot
from tortoise import Tortoise


class Badger(Bot):
    PREFIX = '/'
    http_session = ClientSession()

    async def on_error(self, event, *args, **kwargs):
        await super().on_error(event, *args, **kwargs)
        # We will use this hook to log the errors

    async def on_ready(self):
        print('Connecting to the database and generating the schemas(if not exists): ', datetime.datetime.now())
        await self.init()
        print('Starting bot at:', datetime.datetime.now())

    @staticmethod
    async def init():
        # Here we connect to a SQLite DB file.
        # also specify the app name of "models"
        # which contain models from "app.models"
        await Tortoise.init(
            db_url='sqlite://db.sqlite3',
            modules={'models': ['db.models']}
        )
        # Generate the schema
        await Tortoise.generate_schemas()
