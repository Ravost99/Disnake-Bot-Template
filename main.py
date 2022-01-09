import disnake, config, os
from disnake.ext import commands

bot = commands.Bot(
  command_prefix="!",
  intents=disnake.Intents.all(),
  sync_permissions=True
)

@bot.event
async def on_ready():
  print(
    f"Im logged in as {bot.user}\n",
    f"Disnake version: {disnake.__version__}"
  )

@bot.slash_command(name="ping", description="Check if the bot is alive")
async def ping(inter):
    await inter.response.send_message("Pong!")

bot.run(os.environ['TOKEN'])
