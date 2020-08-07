import os
from ast import literal_eval
from utils import AttrDict


class ImproperlyConfigured(Exception):
    ...


def value(variable):
    return os.environ.get(variable)


def required_value(variable):
    val = os.environ.get(variable)
    if val is None:
        raise ImproperlyConfigured('Required environment variables could not be found.')
    return val


v, rv = value, required_value

CONF = AttrDict.from_data(
    {
        'DEBUG': literal_eval(rv('DEBUG')),  # Maybe use a config library here?
        'SECRETS': {
            'BOT_TOKEN': rv('SECRETS.BOT_TOKEN'),
        },
        'COGS': {
            'CODE_SHARING': {
                'HASTEBIN_SERVER': rv('COGS.CODE_SHARING.HASTEBIN_SERVER')
            }
        }
    }
)
