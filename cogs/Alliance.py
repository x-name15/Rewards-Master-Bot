import discord, DiscordUtils
import aiofiles, aiohttp
import random, string, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Alliance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.YELLOW}Alliance{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'The error is:\n```{error}```'))
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def check_alliances(self, ctx):
        with open("data/alliance/alliances.txt", "r") as f:
            alliances = f.read().splitlines()
            check = '\n'.join(alliances[0:30])
        embed=discord.Embed(title=f"Alliances from: {ctx.guild.name}", description=check,color = 0x4CB54B)
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def alliance(self, ctx, message=None, ID=None, invite=None):
        if message is None:
            embed = discord.Embed(title="The command is: ```rm!alliance [Name of the server | ID | Invite ]```", colour=0xFF0000)
            await ctx.send(embed=embed)
            return
        if ID is None:
            embed2 = discord.Embed(title="The command is: ```rm!alliance [Name of the server | ID | Invite ]```", colour=0xFF0000)
            await ctx.send(embed=embed2)
            return
        if ID is None:
            embed3 = discord.Embed(title="The command is: ```rm!alliance [Name of the server | ID | Invite ]```", colour=0xFF0000)
            await ctx.send(embed=embed3)
            return
        else:
            with open("data/alliance/alliances.txt", "a") as file:
                file.write("Server: " + message + " | " + "ID: " + ID + " | " + "Invite: " + invite + "\n")
            print(f"{Fore.MAGENTA}A new friendship/alliance was forged{Fore.RESET}")
            await ctx.send(embed=discord.Embed(title="A new Frienship/Alliance was forged in the Server!", description="Take a cookie :cookie:\nYou can use check_alliances to see server alliances/friends", color=0x13d9e7))
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Alliance(bot))