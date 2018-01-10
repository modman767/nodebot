import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix=config.COMMAND_PREFIX)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

@bot.command()
async def add(left:int, right:int):
    """Adds two numbers together"""
    await bot.say(left + right)

if __name__ == "__main__":
    bot.run(config.TOKEN, bot=True, reconnect=True)