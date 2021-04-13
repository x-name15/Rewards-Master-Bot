import discord
import random, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Premiun_Gen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.CYAN}Premiun Gen{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingRole):
            await ctx.send(embed=discord.Embed(title='Missing Required Role',description='You dont have the required role "Premiun Gen" to run this command.'))
        else:
            await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'The error is:\n```{error}```'))    
    @commands.command()
    @commands.has_role("Premiun Gen")
    @commands.cooldown(1, 8640, commands.BucketType.user)
    async def spotify(self, ctx):
        with open('data/accounts/premiun/spotify.txt', 'r') as (f):
            text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('data/accounts/premiun/spotify.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)
            break
        print(f"  > User {ctx.author} generated a Spotify Account at time {datetime.datetime.now()}")
        await ctx.author.send(f"Spotify Account: {User}:{PassFixed}\nThanks for using our premiun generator")
        await ctx.send(embed=discord.Embed(title='Your account has been generated.',description='Your account was successfully generated. You can run this command again for more.'))
    @commands.command()
    @commands.has_role("Premiun Gen")
    @commands.cooldown(1, 8640, commands.BucketType.user)
    async def netflix(self, ctx):
        with open('data/accounts/premiun/netflix.txt', 'r') as (f):
            text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('data/accounts/premiun/netflix.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)
            break
        print(f"  > User {ctx.author} generated a Netflix Account at time {datetime.datetime.now()}")
        await ctx.author.send(f"Netflix Account: {User}:{PassFixed}\nThanks for using our premiun generator")
        await ctx.send(embed=discord.Embed(title='Your account has been generated.',description='Your account was successfully generated. You can run this command again for more.'))

def setup(bot):
    bot.add_cog(Premiun_Gen(bot))