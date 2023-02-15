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



@bot.command(name="start")
async def start(ctx):
  try:
    if db[f"tutorial{ctx.message.author}"] == 1:
      await ctx.send("Type >commands to see what to do next")
  except:
    await ctx.send("Welcome to the world of mining!!\n"
                     "The commands to use are:\n"
                     "command_list - brings up this menu\n"
                     "mine - Gain more resources\n"
                     "sell [material] [amount] / sellall -"
                     " sell a specific type of materials or just sell them all for money!\n"
                     "Craft - use a workbench and craft new items inculding a better pickaxe and new workstations"
                     "areas - Join different areas for more resource gain and see what areas are available\n"
                     "items - shows all items held by you!\n\n"
                     "To begin your journey type shop and buy the free semi-broken pickaxe\n")
    
    #minerals
    db[f"dirt{ctx.message.author}"] = 0
    db[f"stone{ctx.message.author}"] = 0
    db[f"iron{ctx.message.author}"] = 0
    db[f"iron_bar{ctx.message.author}"] = 0
    db[f"wood{ctx.message.author}"] = 0
    db[f"ash{ctx.message.author}"] = 0
    db[f"charcoal{ctx.message.author}"] = 0
    db[f"coins{ctx.message.author}"] = 0
    db[f"cog{ctx.message.author}"] = 0
    db[f"copper{ctx.message.author}"] = 0
    db[f"brick{ctx.message.author}"] = 0

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
    db[f"Workbench{ctx.message.author}"] = 0
    db[f"furnace{ctx.message.author}"] = 0
    db[f"fuel_amount{ctx.message.author}"] = 0
    db[f"anvil{ctx.message.author}"] = 0
    
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
    db[f"garage{ctx.message.author}"] = 0
    db[f"garage_wall{ctx.message.author}"] = 0

    #animals
    db[f"pig{ctx.message.author}"] = 0
    db[f"cow{ctx.message.author}"] = 0
    db[f"horse{ctx.message.author}"] = 0
    db[f"unicorn{ctx.message.author}"] = 0
    db[f"frog{ctx.message.author}"] = 0
    
    #tutorial
    db[f"tutorial{ctx.message.author}"] = 1

@bot.command(name="commands")
async def commands(ctx):
  await ctx.send("The commands to use are:\n"
                     "support - brings up this menu\n"
                     "mine - Gain more resources\n"
                     "sell [material] [amount] / sellall -"
                     " sell a specific type of materials or just sell them all for money!\n"
                     "Craft - use a workbench and craft new items inculding a better pickaxe and new workstations"
                     "areas - Join different areas for more resource gain and see what areas are available\n"
                     "items - shows all items held by you!\n"
                     "shelter_shop - lets you buy buildings \n\n")






@bot.command(name="areas")
async def areas(ctx):
  await ctx.send("Area 1 - Backyard (requires broken pickaxe to mine here) \n\n Area 2 - Building site (requires workshop pickaxe to mine here and wheelchair to go here) \n\n Area 3 - Random field (requires iron drill to mine here and bike to go here) \n\n Area 4 - Coal mine (requires Copper drill to mine her and horse cart to go here \n\n Type >travel 1.2.3 to go here")


@bot.command(name="travel")
async def travel(ctx, area: int):
  if area == 1:
    if db[f"Area{ctx.message.author}"] != 1:
      db[f"Area{ctx.message.author}"] = 1
      await ctx.send("You are now in your backyard")
    else:
      await ctx.send("You are already in this area")
  elif area == 2:
    if db[f"wheel_chair{ctx.message.author}"] >= 1:
      if db[f"pickaxe{ctx.message.author}"] >= 2:
        await ctx.send("You are now in the building site and the workers dont look happy....")
        db[f"Area{ctx.message.author}"] = 2
      else:
        await ctx.send("You need a workshop pickaxe to go here")
    else:
      await ctx.send("You need a wheel chair to travel here (you can make this in the garage)")
  elif area == 3:
    if db[f"bike{ctx.message.author}"] >= 1:
      if db[f"pickaxe{ctx.message.author}"] >= 3:
        await ctx.send("you are now in a random field.. there seems to be a sign that says no access... oh well \n you can now access >animals, here you can buy animals for coins.. even if the farmer wasnt planning to sell them")
        db[f"Area{ctx.message.author}"] = 3
      else:
        await ctx.send("You need an iron drill for this (you can make this in the garage)")
    else:
      await ctx.send("You need a bike to go here (you can make this in the garage)")
  elif area == 4:
    if db[f"horse_cart{ctx.message.author}"] >= 1:
      if db[f"pickaxe{ctx.message.author}"]  >= 4:
        await ctx.send("You are now in the coal mine. This would be a great place to get fuel.. and maybe a better furnace type >smeltery_shop to go here!")
        db[f"Area{ctx.message.author}"] = 4
  
  elif area == 8:
    if db[f"unicorn{ctx.message.author}"] >= 1:
      await ctx.send("Well hello there mortal, so far my dialog hasnt been added in.. lets just say for now in the future you can come here to rebirth :O \n\n you travel back to the area you were in to begin with and continue your journey.")

    else:
      await ctx.send("You havent found the secret to unlock this yet :)")

  else:
    await ctx.send("This was not an option (Type >areas to see where you can go)")

def setup(bot):
    bot.add_command(start)
    bot.add_command(commands)
    bot.add_command(areas)
    bot.add_command(travel)













