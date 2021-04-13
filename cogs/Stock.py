import discord
import random, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Stock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.YELLOW}Stock{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingRole):
            await ctx.send(embed=discord.Embed(title='Missing Required Role',description='You dont have the required role "Premiun Gen" to run this command.'))
        else:
            await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'The error is:\n```{error}```'))
    @commands.command(pass_context=True)
    @commands.has_role("Premiun Gen")
    async def premiunstock(self, ctx):
        premiun_num_lines = sum(1 for line in open('data/accounts/premiun/spotify.txt'))
        premiun_num_lines2 = sum(1 for line in open('data/accounts/premiun/netflix.txt'))
        await ctx.send('--------------------------------------')
        await ctx.send('The current **Spotify** Stock is: ' + str(premiun_num_lines))
        await ctx.send('The current **Netflix** Stock is: ' + str(premiun_num_lines2))
        await ctx.send('--------------------------------------')
    @commands.command(pass_context=True)
    async def freestock(self, ctx):
        free_num_lines = sum(1 for line in open('data/accounts/premiun/spotify.txt'))
        free_num_lines2 = sum(1 for line in open('data/accounts/premiun/netflix.txt'))
        await ctx.send('--------------------------------------')
        await ctx.send('The current **Disney +** Stock is: ' + str(free_num_lines))
        await ctx.send('The current **Crunchyroll** Stock is: ' + str(free_num_lines2))
        await ctx.send('--------------------------------------')

def setup(bot):
    bot.add_cog(Stock(bot))