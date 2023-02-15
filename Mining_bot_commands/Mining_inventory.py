# Imports Required

import asyncio
import os
import discord
from discord.ext import commands
from Keep_alive import keep_alive
import threading
import random
from replit import db

# Bot Prefix

bot = commands.Bot(command_prefix=">")

# variables used

##materials
global dirt, stone, iron, iron_bar, wood, ash, charcoal, coins, cog

##tools
global pickaxe, axe, autominer

##areas
global Area, Forest_card, wheel_upgrade

##cooldowns
global chopping, mining_cooldown, smelting

##workstations + fuel
global Workbench, furnace, fuel_amount, anvil

##modifiers
global modifier, razor_edge, fortune, fortune_level, effciency, effciency_level

'''
## all variables
global dirt, stone, iron, iron_bar, wood, ash, charcoal, coins, cog, pickaxe, axe, drill_bit, autominer, Area, Forest_card, wheel_upgrade, chopping, mining_cooldown, smelting, Workbench, furnace, fuel_amount, anvil, modifier, razor_edge, fortune, effciency

##materials
dirt = 414 #0
stone = 94 #0
iron = 41 #0
iron_bar = 8 #0
wood = 18 #0
ash = 0 #0
charcoal = 0 #0
coins = 289 #0
cog = 0 #0

##tools
pickaxe = 2 #0
axe = 1 #0
drill_bit = 0
autominer = 0


##areas
Area = 1
Forest_card = 1 #0
wheel_upgrade = 1

##cooldowns
chopping = False
mining_cooldown = False
smelting = False

##workstations + fuel
Workbench = 1 #0
furnace = 1 #0
fuel_amount = 1
anvil = 0

##modifiers
modifier = 1
razor_edge = 1 #0
fortune = 1
fortune_level = 1
effciency = 1
effciency_level = 0
'''

"""
#minerals
db["dirt"] = 0
db["stone"] = 0
db["iron"] = 0
db["iron_bar"] = 0
db["wood"] = 0
db["ash"] = 0
db["charcoal"] = 0
db["coins"] = 0
db["cog"] = 0

#tools
db["pickaxe"] = 0
db["axe"] = 0
db["drill_bit"] = 0
db["autominer"] = 0

#areas
db["Area"] = 1
db["Forest_card"] = 0
db["wheel_upgrade"] = 1

#workstations
db["Workbench"] = 0
db["furnace"] = 0
db["fuel_amount"] = 0
db["anvil"] = 0

#modifiers
db["modifier"] = 1
db["razor_edge"] = 0
db["fortune"] = 1
db["fortune_level"] = 0
db["effciency"] = 1
db["effciency_level"] = 0

#levels
db["mines"] = 0
db["mining_level"] = 0
db["chops"] = 0
db["chopping_level"] = 0

#cooldowns
db["chopping"] = False
db["mining_cooldown"] = False
db["smelting"] = False
db["wait_for_daily"] = False

db["Start"] = False

"""


#reset cooldowns if bot goes offline

db["chopping"] = False
db["mining_cooldown"] = False
db["smelting"] = False
db["wait_for_daily"] = False

@bot.command(name="items")
async def items(ctx):
  global dirt, stone, iron, iron_bar, wood, ash, charcoal, coins, cog, pickaxe, axe, autominer, Area, Forest_card, wheel_upgrade, chopping, mining_cooldown, smelting, Workbench, furnace, fuel_amount, anvil, modifier, razor_edge, fortune

  await ctx.send("dirt | {0} \n stone | {1} \n iron | {2} \n iron_bar | {3} \n wood | {4} \n ash | {5} \n charcoal | {6} \n coin | {7} \n cog | {8} \n area | {9} \n Forest card | {10} \n workbench | {11} \n furnace | {12} \n Fuel | {13} \n anvil | {14} \n razor edge | Level {15} \n fortune | Level {16} \n efficiency | level {17} \n".format(db[f"dirt{ctx.message.author}"], db[f"stone{ctx.message.author}"], db[f"iron{ctx.message.author}"], db[f"iron_bar{ctx.message.author}"], db[f"wood{ctx.message.author}"], db[f"ash{ctx.message.author}"], db[f"charcoal{ctx.message.author}"], db[f"coins{ctx.message.author}"], db[f"cog{ctx.message.author}"], db[f"Area{ctx.message.author}"], db[f"Forest_card{ctx.message.author}"], db[f"Workbench{ctx.message.author}"], db[f"furnace{ctx.message.author}"], db[f"fuel_amount{ctx.message.author}"], db[f"anvil{ctx.message.author}"], db[f"razor_edge{ctx.message.author}"], db[f"fortune_level{ctx.message.author}"], db[f"effciency_level{ctx.message.author}"]))


@bot.command(name="levels")
async def levels(ctx):
  global mining_level, chopping_level
  await ctx.send("mining level | {0} \nchopping level | {1}".format(db[f"mining_level{ctx.message.author}"], db[f"chopping_level{ctx.message.author}"]))

@bot.command(name="tools")
async def tools(ctx):
  await ctx.send(" Pickaxe | Level {0} \nAxe | Level {1} \n".format(db[f"pickaxe{ctx.message.author}"], db[f"axe{ctx.message.author}"]))

@bot.command(name="buildings")
async def buildings(ctx):
  await ctx.send("bedroom | {0} \n bathroom | {1} \n garage | {2} \n livingroom | {3} \n bedroom wall | {4} \n bathroom wall | {5} \n garage wall | {6} \n livingroom wall | {7}".format(db[f"bedroom{ctx.message.author}"], db[f"bathroom{ctx.message.author}"], db[f"garage{ctx.message.author}"], db[f"livingroom{ctx.message.author}"], db[f"bedroom_wall{ctx.message.author}"], db[f"bathroom_wall{ctx.message.author}"], db[f"garage_wall{ctx.message.author}"], db[f"livingroom_wall{ctx.message.author}"]))


def setup(bot):
  bot.add_command(items)
  bot.add_command(levels)
  bot.add_command(tools)
  bot.add_command(buildings)
