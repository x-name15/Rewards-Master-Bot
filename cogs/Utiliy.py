import discord
import random, string, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.RED}Utility{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'The error is:\n```{error}```'))
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!\nThe latency is: {round(self.bot.latency * 1000)}ms')
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:  
            member = ctx.message.author  
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at, title=f"Information of the user: {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by: {ctx.author}")
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="NickName:", value=member.display_name)
        embed.add_field(name="Discriminator:",value=member.discriminator, inline=False)
        embed.add_field(name="Created account in day:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Join in day:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
        embed.add_field(name="Greater role with power:", value=member.top_role.mention)
        embed.add_field(name="Status:", value=str(member.status).title(), inline=False)
        embed.add_field(name="Bot?:", value=member.bot)
        await ctx.send(embed=embed)
    @commands.command()
    async def serverinfo(self, ctx):
        name = ctx.guild.name
        description = ctx.guild.description
        owner = ctx.guild.owner
        id = ctx.guild.id
        region = ctx.guild.region
        memberCount = ctx.guild.member_count
        icon = ctx.guild.icon_url
        embed = discord.Embed(title=name + " Server Information", description=description, color=discord.Color.blue())
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        await ctx.send(embed=embed)
    @commands.command()
    async def membercount(self, ctx):
        a = ctx.guild.member_count
        b = discord.Embed(title=f"Members in {ctx.guild.name}",description=f"There are: {a} members in the guild!",color=discord.Color((0xffff00)))
        await ctx.send(embed=b)
    @commands.command()
    async def servericon(self, ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}", color=discord.Color.blue())
        embed.set_image(url=f"{ctx.guild.icon_url}")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Utility(bot))