import discord
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.MAGENTA}Crypto{Fore.RESET} Loaded Correctly")
    @commands.command()
    async def btc(self, ctx):
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`', colour=0xFFD700)
        em.set_author(name='BTC Price', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
        await ctx.send(embed=em)
    @commands.command()
    async def eth(self, ctx):
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
        em.set_author(name='Etherum Price', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
        await ctx.send(embed=em)
def setup(bot):
    bot.add_cog(Crypto(bot))