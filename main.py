import discord
import os, asyncio, colorama
from discord.ext import commands
from discord import Game
from colorama import Fore
from colorama import init
init()

token = "Token-Here"
prefix = "rm!"
version = "1.0"
dev = "Chirimoya"
RPC = "The Rewards Master Bot"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("---------")
    print("Im ready bitch")
    print(f'Logued in: {Fore.RED}{bot.user.name}{Fore.RESET}')
    print(f"Prefix: {Fore.CYAN}{prefix}{Fore.RESET}")
    print(f"ID of the Bot: {Fore.LIGHTMAGENTA_EX}{bot.user.id}{Fore.RESET}")
    print(f"Bot version: {Fore.RED}{version}{Fore.RESET}")
    print(f"Developer: {Fore.YELLOW}{dev}{Fore.RESET}")
    print(f"Current RPC: {Fore.MAGENTA}{RPC}{Fore.RESET}")
    print(f"{Fore.BLUE}Discord Version: {discord.__version__}{Fore.RESET}")
    print("---------")
    print(f"--{Fore.GREEN}COGS{Fore.RESET}--")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(RPC))

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def cleancmd(ctx):
    os.system('cls')
    print(f"{Fore.RED}I cleaned all the cmd{Fore.RESET}")
    await ctx.send("Successfully")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(token)
