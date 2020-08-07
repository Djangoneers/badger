from discord.ext.commands import command as _command


def command(name, cls, **attrs):
    def wrapper(function):
        return _command(name or function.__name__, cls, **attrs)
    return wrapper
