import discord
import random, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Free_Generator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.GREEN}Free Generator{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("On cooldown bitch")
        else:
            await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'The error is:\n```{error}```'))
    @commands.command(aliases=["gen disney", "disney+", "get disney"])
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def disney(self, ctx):
        with open('data/accounts/free/disney.txt', 'r') as (f):
            text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('data/accounts/free/disney.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)
            break
        print(f"  > User {ctx.author} generated a Disney + Account at time {datetime.datetime.now()}")
        await ctx.author.send(f"Disney Account: {User}:{PassFixed}\nThanks for using our free generator")
        await ctx.send(embed=discord.Embed(title='Your account has been generated.',description='Your account was successfully generated. You can run this command again for more.'))
    @commands.command(aliases=["gen crunchyroll", "crunchy", "get crunchyroll"])
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def crunchyroll(self, ctx):
        with open('data/accounts/free/crunchyroll.txt', 'r') as (f):
            text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('data/accounts/free/crunchyroll', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)
            break
        print(f"  > User {ctx.author} generated a Crunchyroll Account at time {datetime.datetime.now()}")
        await ctx.author.send(f"Crunchyroll Account Account: {User}:{PassFixed}\nThanks for using our free generator")
        await ctx.send(embed=discord.Embed(title='Your account has been generated.',description='Your account was successfully generated. You can run this command again for more.'))
def setup(bot):
    bot.add_cog(Free_Generator(bot))