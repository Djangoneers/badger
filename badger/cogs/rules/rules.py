from discord.ext.commands import Cog


class RulesCog(Cog):
    ...


def setup(bot):
    bot.add_cog(RulesCog(bot))
