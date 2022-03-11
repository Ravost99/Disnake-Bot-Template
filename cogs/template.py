import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command

#LANGUAGES = ["Python", "JavaScript", "TypeScript", "Java", "Rust", "Lisp", "Elixir"]
# Define a simple View that gives us a counter button
class Counter(disnake.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.red)
    async def count(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = disnake.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)


class Template(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    # a slash command, add a custom name and description
    @slash_command(
      name="testcommand",
      description=None#add your description here
    )
    async def testcommand(self, inter):
        # remember to remove the 'pass' and add your own stuff here
        pass

    @slash_command()
    async def counter(inter):
        """Starts a counter for pressing."""
        await inter.send("Press!", view=Counter())


def setup(bot):
    bot.add_cog(Template(bot))
    print(f"> Extension {__name__} is ready")