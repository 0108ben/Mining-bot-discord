import asyncio

import os
import discord
from discord.ext import commands
from Keep_alive import keep_alive

bot = commands.Bot(command_prefix=">")


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hello!")


@bot.command(name="points")
async def points(ctx, name: str):
    await ctx.send(
        f'Use this link to see peoples points in DDraceNetwork! https://ddnet.tw/players/{name}/'
    )


@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.command(name="subscribe")
async def subscribe(ctx):
    embed = discord.Embed(
        title="Subscribe to 0108ben!",
        description="I make ddracenetwork videos",
        url="https://www.youtube.com/channel/UCicNSbn32fjhAilk50z4vVA",
        color=582812)
    msg = await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(hello)
    bot.add_command(points)
    bot.add_command(ping)
    bot.add_command(subscribe)
