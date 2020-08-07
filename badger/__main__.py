from discord.ext.commands import when_mentioned_or
from settings import CONF
from badger import Badger

badger = Badger(
    command_prefix=when_mentioned_or(Badger.PREFIX),
)

extensions_to_load = [
    'cogs.rules',
    'cogs.status',
    'cogs.code_sharing',
]
for extension in extensions_to_load:
    badger.load_extension(extension)

badger.run(CONF.SECRETS.BOT_TOKEN)
