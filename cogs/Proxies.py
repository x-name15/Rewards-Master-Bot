import discord
import random, os, time
import colorama, datetime, requests
from discord import Embed, File
from discord.ext import commands
from colorama import Fore
from colorama import init
init()
class Proxies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"> Cog {Fore.BLUE}Proxies{Fore.RESET} Loaded Correctly")
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'The error is:\n```{error}```'))
    @commands.command()
    async def http(self,ctx):
        f = open("data/proxies/http-proxies.txt", "a+")
        f.truncate(0)
        r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=http&amp;timeout=10000&amp;country=all&amp;ssl=all&amp;anonymity=all')
        proxies = []
        for proxy in r.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            f.write((p)+"\n")
        await ctx.send("HTTP Proxies from ProxyScrape API")
        await ctx.send(file=File("data/proxies/http-proxies.txt"))
        print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scrapped some {Fore.CYAN}HTTP Proxies{Fore.RESET} in time {datetime.datetime.now()}")
    @commands.command()
    async def socks4(self,ctx):
        f = open("data/proxies/socks4-proxies.txt", "a+")
        f.truncate(0)
        r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=socks4&amp;timeout=10000&amp;country=all')
        proxies = []
        for proxy in r.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            f.write((p)+"\n")
        await ctx.send("Socks4 Proxies from ProxyScrape API")
        await ctx.send(file=File("data/proxies/socks4-proxies.txt"))
        print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scraped some {Fore.GREEN}Socks4 Proxies{Fore.RESET} in time {datetime.datetime.now()}")
    @commands.command()
    async def socks5(self,ctx):
        f = open("data/proxies/socks5-proxies.txt", "a+")
        f.truncate(0)
        r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=socks5&amp;timeout=10000&amp')
        proxies = []
        for proxy in r.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            f.write((p)+"\n")
        await ctx.send("Socks4 Proxies from ProxyScrape API")
        await ctx.send(file=File("data/proxies/socks5-proxies.txt"))
        print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scraped some {Fore.YELLOW}Socks5 Proxies{Fore.RESET} in time {datetime.datetime.now()}")
    @commands.command()
    async def mixed(self,ctx):
        f = open("data/proxies/all-proxies.txt", "a+")
        f.truncate(0)
        r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000')
        proxies = []
        for proxy in r.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            f.write((p)+"\n")
        await ctx.send("Mixed Proxies from ProxyScrape API")
        await ctx.send(file=File("data/proxies/all-proxies.txt"))
        print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scraped some {Fore.RED}Mixed Proxies{Fore.RESET} in time {datetime.datetime.now()}")

def setup(bot):
    bot.add_cog(Proxies(bot))