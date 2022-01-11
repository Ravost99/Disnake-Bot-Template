import disnake, config, os
from disnake.ext import commands

os.system('clear')

bot = commands.Bot(
  command_prefix="!",
  intents=disnake.Intents.all(),
  help_command=None,
  sync_commands_debug=True,
  sync_permissions=True,
  test_guilds=[929753074875125781],
)

@bot.event
async def on_ready():
  print(f"Im logged in as {bot.user}")
  print(f"In {len(bot.guilds)} guilds")
  print(f"Disnake Version: {disnake.__version__}")
  print("-----------------------------")

def load_all_extensions(folder: str) -> None:
  py_path = f"{folder}"
  folder = f"{folder}"
  for name in os.listdir(folder):
    if name.endswith(".py") and os.path.isfile(f"{folder}/{name}"):
      bot.load_extension(f"{py_path}.{name[:-3]}")

load_all_extensions("cogs")
bot.run(os.environ['TOKEN'])
