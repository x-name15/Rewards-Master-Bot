import discord, DiscordUtils
import random, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Welcome(commands.Cog):
    intents = discord.Intents.default()
    intents.members = True
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.BLUE}Welcome{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        if channel:
            embed = discord.Embed(description="Welcome to the guild!", color=0x27FF00)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.set_footer(text=member.guild, icon_url=member.guild.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=embed)
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="goodbye")
        if channel:
            embed = discord.Embed(
                description="So, you are leaving :C seeya",
                color=0x27FF00,
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.set_footer(text=member.guild, icon_url=member.guild.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=embed)
def setup(bot):
    bot.add_cog(Welcome(bot))