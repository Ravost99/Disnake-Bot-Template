import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class General(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(
      name="delete",
      description="Delete message by id"
    )
    async def delete(self, inter, msgID=929773637563719680):
        msg = await inter.fetch_message(msgID)
        await inter.send(msg)

    @slash_command(
      name="ping",
      description="Check if the bot is alive"
    )
    async def ping(self, inter):
        embed = disnake.Embed(
          title=":ping_pong: Pong!",
          description="I'm alive!",
          color=disnake.Color.green()
        )
        await inter.response.send_message(embed=embed)
    
    @slash_command(
      name="poll",
      description="Create a poll that users can react to"
    )
    async def poll(self, inter, emoji_1, emoji_2, emoji_3, title):
        embed = disnake.Embed(
          title=title,
          color=disnake.Color.green()
        )
        message = await inter.send(embed=embed)
        message.add_reaction(emoji_1)
        message.add_reaction(emoji_2)
        message.add_reaction(emoji_3)


def setup(bot):
    bot.add_cog(General(bot))
    print(f"> Extension {__name__} is ready")