#imports and packages==
import disnake, config, os
from disnake.ext import commands, tasks

os.system('clear')

#setting up the bot
bot = commands.Bot(
  command_prefix="!",
  intents=disnake.Intents.all(),
  help_command=None,
  sync_commands_debug=True,
  sync_permissions=True,
  test_guilds=[929753074875125781],
)

#checking when the bot is ready
@bot.event
async def on_ready():
  print(f"Im logged in as {bot.user}")
  print(f"In {len(bot.guilds)} guilds")
  print(f"Disnake Version: {disnake.__version__}")
  print(f"Starting Status Task: {config.status_task}")
  print("-----------------------------")
  status_task.start()

# Setup the game status task of the bot
# change the minutes to what ever you want, remove if you want
@tasks.loop(minutes=5.0)
async def status_task():
    #change the 'ActivityType.playing' to listening, watching, streaming, playing, competing
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name=config.status_task))

#loading all extensions in the cogs folder
if __name__ in '__main__':
  py_path = f"cogs"
  folder = f"cogs"
  for name in os.listdir(folder):
    if name.endswith(".py") and os.path.isfile(f"cogs/{name}"):
      bot.load_extension(f"{py_path}.{name[:-3]}")

#running the bot with the token
bot.run(os.environ['TOKEN'])