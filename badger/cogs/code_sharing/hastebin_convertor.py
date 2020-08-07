from urllib.parse import urlparse, urljoin
from settings import CONF

class Hastebin:
    server = CONF.COGS.CODE_SHARING.HASTEBIN_SERVER
    server_api_link = urljoin(server, 'documents')
    converters = {}

    @classmethod
    async def from_link(cls, link):
        return await cls.convert(link)

    @classmethod
    async def convert(cls, link):
        """Turn link into code,code into hastebin link"""
        code = await cls.code_from_link(link)
        link = await cls.hastebin_from_code(code)
        return link

    @classmethod
    async def hastebin_from_code(cls, code):
        """Upload the code to hastebin"""

        response = await cls.http_session.post(cls.server_api_link, data=code)
        rjson = await response.json()
        link = urljoin(cls.server, rjson['key'])
        return link

    @classmethod
    async def code_from_link(cls, link):
        host = urlparse(link).netloc
        code = await cls.converters[host](link, cls.http_session)
        return code

    @classmethod
    def register_converter(cls, name):
        def decorator(f):
            cls.converters[name] = f
            return f

        return decorator


@Hastebin.register_converter('pastebin.com')
async def pastebin(link, http_session):
    path = urlparse(link).path
    r = await http_session.get(urljoin('http://pastebin.com', path))
    code = await r.text()
    return code


# We really should stop tossing the http_session around so much somehow, maybe some metaclass magic