import discord, DiscordUtils
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.CYAN}Nuke{Fore.RESET} Loaded Correctly")
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        if channel == None: 
            await ctx.send("Pls mention the channel to nuke")
            return
        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Nuked!")
            await nuke_channel.delete()
            await new_channel.send("Cleaned and NUKED this Channel :D\nhttps://tenor.com/view/explosion-action-bird-run-running-gif-4877919")
            await ctx.send("Nuked the channel mentioned")
        else:
            await ctx.send(f"No channel named: {channel.name} was found")
def setup(bot):
    bot.add_cog(Nuke(bot))