import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class Template(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(
      name="testcommand",
      description=None
    )
    async def testcommand(self, inter):
        await inter.send(inter.command)


def setup(bot):
    bot.add_cog(Template(bot))
    print(f"> Extension {__name__} is ready")