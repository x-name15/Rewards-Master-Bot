import discord
import random, string, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Rewards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.GREEN}Perks{Fore.RESET} Loaded Correctly")
    @commands.command()
    async def rewards(self, ctx):
        with open("data/rewards/boost_perks.txt", "r") as f:
            perks = f.read().splitlines()
            lawea2 = '\n'.join(perks[0:50])
        embed=discord.Embed(title=f"Boost Perks from: {ctx.guild.name}", description=lawea2,color = 0x03E300)
        await ctx.author.send(embed=embed)
        await ctx.send("Check ur DMs, I send you the Boost Perks")
def setup(bot):
    bot.add_cog(Rewards(bot))