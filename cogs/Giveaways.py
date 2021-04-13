import discord, DiscordUtils
import random, time, asyncio, datetime
import string, os, colorama
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.WHITE}Giveaways{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'The error is:\n```{error}```'))
    @commands.command()
    async def giveaway(self, ctx, time: int, *, prize):
        giveawayembed = discord.Embed(
            title="🎉 New Giveaway! 🎉",
            colour=discord.Color.green()
            )
        giveawayembed.add_field(name="Prize", value="{}".format(prize), inline=False)
        giveawayembed.add_field(name="Hosted by", value=f"{ctx.author.mention}", inline=False)
        giveawayembed.add_field(name="Ends in", value="{}s".format(time))
        msg = await ctx.send(embed=giveawayembed)
        await msg.add_reaction("🎉")
        await asyncio.sleep(time)
        msg = await msg.channel.fetch_message(msg.id)
        winner = None  
        for reaction in msg.reactions:
            if reaction.emoji == "🎉":
                users = await reaction.users().flatten()
                users.remove(self.bot.user)
                winner = random.choice(users)
        if winner is not None:
            endembed = discord.Embed(
                title="Giveaway ended!",
                description="Prize: {}\nWinner: {}".format(prize, winner))
            await msg.edit(embed=endembed)
    @giveaway.error
    async def giveaway_error(self, ctx, error):
        print(error)
def setup(bot):
    bot.add_cog(Giveaway(bot))
