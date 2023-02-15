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

@bot.command(name="reset_timer")
async def reset_timer(ctx):
  db[f"chopping{ctx.message.author}"] = False
  db[f"mining_cooldown{ctx.message.author}"] = False
  db[f"smelting{ctx.message.author}"] = False
  db[f"wait_for_daily{ctx.message.author}"] = False

@bot.command(name="cheat_0108ben")
async def cheat_0108ben(ctx):
    await ctx.send("1")
    #minerals
    db[f"dirt{ctx.message.author}"] = 1000000000
    db[f"stone{ctx.message.author}"] = 1000000000
    db[f"iron{ctx.message.author}"] = 1000000000
    db[f"iron_bar{ctx.message.author}"] = 1000000000
    db[f"wood{ctx.message.author}"] = 1000000000
    db[f"ash{ctx.message.author}"] = 10000000000
    db[f"charcoal{ctx.message.author}"] = 1000000000
    db[f"coins{ctx.message.author}"] = 1000000000
    db[f"cog{ctx.message.author}"] = 10000000000
    db[f"copper{ctx.message.author}"] = 1000000000
    db[f"brick{ctx.message.author}"] = 1000000000

    #tools
    db[f"pickaxe{ctx.message.author}"] = 0
    db[f"axe{ctx.message.author}"] = 0
    db[f"drill_bit{ctx.message.author}"] = 0
    db[f"autominer{ctx.message.author}"] = 0
    
    #areas
    db[f"Area{ctx.message.author}"] = 1
    db[f"Forest_card{ctx.message.author}"] = 0
    db[f"wheel_chair{ctx.message.author}"] = 0 #(area 2)
    db[f"bike{ctx.message.author}"] = 0 #(area 3)
    db[f"horse_cart{ctx.message.author}"] = 0 #(area 4)
    
    #workstations
    db[f"Workbench{ctx.message.author}"] = 1
    db[f"furnace{ctx.message.author}"] = 1
    db[f"fuel_amount{ctx.message.author}"] = 1
    db[f"anvil{ctx.message.author}"] = 1
    
    #modifiers
    db[f"modifier{ctx.message.author}"] = 1
    db[f"razor_edge{ctx.message.author}"] = 0
    db[f"fortune{ctx.message.author}"] = 1
    db[f"fortune_level{ctx.message.author}"] = 0
    db[f"effciency{ctx.message.author}"] = 1
    db[f"effciency_level{ctx.message.author}"] = 0
    
    #levels
    db[f"mines{ctx.message.author}"] = 0
    db[f"mining_level{ctx.message.author}"] = 0
    db[f"chops{ctx.message.author}"] = 0
    db[f"chopping_level{ctx.message.author}"] = 0
    
    #cooldowns
    db[f"chopping{ctx.message.author}"] = False
    db[f"mining_cooldown{ctx.message.author}"] = False
    db[f"smelting{ctx.message.author}"] = False
    db[f"wait_for_daily{ctx.message.author}"] = False

    #buildings
    db[f"bedroom{ctx.message.author}"] = 0
    db[f"bedroom_wall{ctx.message.author}"] = 0
    db[f"bathroom{ctx.message.author}"] = 0
    db[f"bathroom_wall{ctx.message.author}"] = 0
    db[f"livingroom{ctx.message.author}"] = 0
    db[f"livingroom_wall{ctx.message.author}"] = 0
    db[f"garage{ctx.message.author}"] = 1
    db[f"garage_wall{ctx.message.author}"] = 0

    #animals
    db[f"pig{ctx.message.author}"] = 0
    db[f"cow{ctx.message.author}"] = 0
    db[f"horse{ctx.message.author}"] = 0
    db[f"unicorn{ctx.message.author}"] = 0 #(area 8)
    db[f"frog{ctx.message.author}"] = 0


    #tutorial
    db[f"tutorial{ctx.message.author}"] = 1

@bot.command(name="reset")
@commands.has_permissions(administrator=True)
async def reset(ctx):
  await ctx.send("Resetting...")
  db.clear()
  await ctx.send("Reset!")

def setup(bot):
    bot.add_command(reset_timer)
    bot.add_command(cheat_0108ben)
    bot.add_command(reset)