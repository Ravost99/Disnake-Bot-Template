import disnake, config, traceback
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command

def fancy_traceback(exc: Exception) -> str:
    """May not fit the message content limit"""
    text = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    return f"```py\n{text[-4086:]}\n```"

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
      embed = disnake.Embed(
        title=f"Command `{ctx.command}` raised an error: `{error}`",
        description=fancy_traceback(error),
        color=config.error
      )
      await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.AppCmdInter, error: commands.CommandError):
      embed = disnake.Embed(
        title=f"Slash command `{inter.data.name}` failed due to `{error}`",
        description=fancy_traceback(error),
        color=config.error,
      )
      if inter.response._responded:
        send = inter.channel.send
      else:
        send = inter.response.send_message
      await send(embed=embed)

    @commands.Cog.listener()
    async def on_user_command_error(self, inter: disnake.AppCmdInter, error: commands.CommandError):
      embed = disnake.Embed(
        title=f"User command `{inter.data.name}` failed due to `{error}`",
        description=fancy_traceback(error),
        color=config.error,
      )
      if inter.response._responded:
        send = inter.channel.send
      else:
        send = inter.response.send_message
      await send(embed=embed)

    @commands.Cog.listener()
    async def on_message_command_error(self, inter: disnake.AppCmdInter, error: commands.CommandError):
      embed = disnake.Embed(
        title=f"Message command `{inter.data.name}` failed due to `{error}`",
        description=fancy_traceback(error),
        color=config.error,
      )
      if inter.response._responded:
        send = inter.channel.send
      else:
        send = inter.response.send_message
      await send(embed=embed)

def setup(bot):
    bot.add_cog(Events(bot))
    print(f"> Extension {__name__} is ready")