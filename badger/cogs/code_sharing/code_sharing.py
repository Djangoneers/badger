from urllib.parse import urlparse

from discord.ext.commands import Cog
from urlextract import URLExtract

from .hastebin_convertor import Hastebin


class CodeSharingCog(Cog):
    """A meta cog to inform admins abouts bot's status."""

    _maybe_try = f'Maybe try {Hastebin.server} next time?\n'
    single_link_message = 'I see a paste link in your message. ' + _maybe_try
    multiple_links_message = 'I see multiple paste links in your message. ' + _maybe_try

    def __init__(self, bot):
        self.extractor = URLExtract()

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        hastebin_urls = []

        urls = self.extractor.find_urls(message.content)
        for url in urls:
            if urlparse(url).netloc in Hastebin.converters.keys():
                link = await Hastebin.from_link(url)
                hastebin_urls.append(link)
        if hastebin_urls:
            if len(hastebin_urls) == 1:
                msg = self.single_link_message + hastebin_urls[0]
            else:
                msg = self.multiple_links_message + '\n'.join(hastebin_urls)

            await message.channel.send(msg)


def setup(bot):
    Hastebin.http_session = bot.http_session  # Maybe find a better way to add session to utility classes?
    bot.add_cog(CodeSharingCog(bot))
