import disnake, config, json
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class Reactrole(commands.Cog):
    def __init__(self, bot):
      self.bot: commands.Bot = bot

    # reactrole command
    @slash_command(
      name="reactrole",
      description="Create a reactrole"
    )
    @commands.has_permissions(administrator=True)
    async def reactrole(self, inter, emoji, role: disnake.Role, message: str):

      embed = disnake.Embed(
        description=message
      )
      msg = await inter.send(embed=embed)
      await msg.add_reaction(emoji)

      with open('reactrole.json') as react_file:
        data = json.load(react_file)

        new_react_role = {
          'role_name': role.name,
          'role_id': role.id,
          'emoji': emoji,
          'message_id': msg.id
        }

        data.append(new_react_role)

      with open('reactrole.json', 'w') as file:
        json.dump(data, file, indent=4)


    # when a user adds a reaction
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
      if payload.member.bot:
        pass
      else:
        with open('reactrole.json') as react_file:
          data = json.load(react_file)
          for item in data:
            if item['emoji'] == payload.emoji.name:
              role = disnake.utils.get(self.bot.get_guild(payload.guild_id).roles, id=item['role_id'])
              
              await payload.member.add_roles(role)
    # when a user removes a reaction
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
      with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for item in data:
          if item['emoji'] == payload.emoji.name:
            role = disnake.utils.get(self.bot.get_guild(payload.guild_id).roles, id=item['role_id'])

            await self.bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

def setup(bot):
    bot.add_cog(Reactrole(bot))
    print(f"> Extension {__name__} is ready")