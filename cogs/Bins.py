import discord
import random, string, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Bins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.RED}BINS{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'The error is:\n```{error}```'))
    @commands.command()
    async def livebins(self, ctx):
        with open("data/bins/list/live_bins.txt", "r") as f:
            bins = f.read().splitlines()
            live = '\n'.join(bins[0:20])
        embed=discord.Embed(title="Live Bins", description=live,color = 0xF1C40F)
        await ctx.send(embed=embed)
    @commands.command()
    async def deadbins(self, ctx):
        with open("data/bins/list/coal_bins.txt", "r") as f:
            deadbins = f.read().splitlines()
            dead = '\n'.join(deadbins[0:20])
        embed=discord.Embed(title="Dead Bins", description=dead,color = 0x875050)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Bins(bot))