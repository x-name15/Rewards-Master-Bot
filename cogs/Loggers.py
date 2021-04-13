import discord
import random, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Loggers(commands.Cog):
    intents = discord.Intents.default()
    intents.members = True
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.RED}Loggers{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = discord.Embed(
        timestamp=message.created_at,
        title = "Deleted Message",
        colour = discord.Colour(0xff0000)
        ) 
        embed.set_author(name=f'{message.author.name}#{message.author.discriminator}', icon_url=message.author.avatar_url)
        embed.set_footer(text=f"ID of the Author: {message.author.id} • ID of the Message: {message.id}")
        embed.add_field(name="Content of the Message:", value=message.content)
        embed.add_field(name="Text Channel:", value=f"{message.channel.mention}")
        channel = self.bot.get_channel(803375369461825569)
        await channel.send(embed=embed)
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        embed = discord.Embed(
        timestamp=after.created_at,
        description = f"<@!{before.author.id}>**s message was edited in channel:** <#{before.channel.id}>",
        colour = discord.Colour(0x00FF00)
        ) 
        embed.set_author(name=f'{before.author.name}#{before.author.discriminator}', icon_url=before.author.avatar_url)
        embed.set_footer(text=f"ID of the Author: {before.author.id} • ID of the Message: {before.id}")
        embed.add_field(name='Before:', value=before.content, inline=False)
        embed.add_field(name="After:", value=after.content, inline=False)
        channel = self.bot.get_channel(803375369461825569)
        await channel.send(embed=embed)
    @commands.Cog.listener()
    async def on_message(self, message: str):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        with open("data/logs/message_logs.txt", "a") as text_file:
            print(f"<{st}> {message.content}", file=text_file)
def setup(bot):
    bot.add_cog(Loggers(bot))