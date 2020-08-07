from discord.ext.commands import Cog, Context, command


class StatusCog(Cog):
    """A meta cog to inform admins abouts bot's status."""

    @command()
    async def echo(self, ctx: Context, msg: str):
        msg = f"Message:{msg}"
        await ctx.send(msg)

    @command()
    async def latency(self, ctx: Context):
        await ctx.send(self.bot.latency)


def setup(bot):
    bot.add_cog(StatusCog(bot))
