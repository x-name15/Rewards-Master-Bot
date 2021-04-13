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
        print(f"> Cog {Fore.GREEN}Rewards{Fore.RESET} Loaded Correctly")
    @commands.command()
    async def rewards(self, ctx):
        with open("data/rewards/rewards.txt", "r") as f:
            rewards = f.read().splitlines()
            lawea = '\n'.join(rewards[0:50])
        embed=discord.Embed(title=f"Rewards from: {ctx.guild.name}", description=lawea,color = 0x03E300)
        await ctx.author.send(embed=embed)
        await ctx.send("Check ur DMs, I send you the rewards")
def setup(bot):
    bot.add_cog(Rewards(bot))