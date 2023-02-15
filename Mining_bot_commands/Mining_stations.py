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

#craft items + show recipies


@bot.command(name="craft")
async def craft(ctx: commands.Context):
  global Workbench
  if db[f"Workbench{ctx.message.author}"] >= 1:
    await ctx.send("Welcome to the crafting interface, these are the items you can craft: \n\n workshop_pickaxe | 15 wood + 7 iron | Gives + 12 minerals when you mine \n\n furnace | 75 stone | allows you to smelt down ores into bars \n\n anvil | 20 iron bar | allows you to create new tools and modifiers \n\n autominer | 10 cogs + drill bit + 100 stone + 15 iron bars | every minute gains 5 minerals for you \n\n Type make [item] in order to craft an item!")
    
  else:
    await ctx.send("You need to have a workbench before you can do this (Buy it in the shop)")

@bot.command(name="make")
async def make(ctx, item: str):
  global dirt, stone, iron, iron_bar, wood, ash, charcoal, coins, cog, pickaxe, axe, drill_bit, autominer, Area, Forest_card, wheel_upgrade, chopping, mining_cooldown, smelting, Workbench, furnace, fuel_amount, anvil, modifier, razor_edge, fortune
  if db[f"Workbench{ctx.message.author}"] >= 1:
    if item == "workshop_pickaxe":
      if db[f"pickaxe{ctx.message.author}"] >= 2:
        await ctx.send("You already have this pickaxe or a pickaxe much better, it would be a waste to craft this")
      else:
        if db[f"wood{ctx.message.author}"] >= 15:
          if db[f"iron{ctx.message.author}"] >= 7:
            await ctx.send("With this pickaxe you can gain + 12 minerals and mine at area 2!")
            db[f"wood{ctx.message.author}"] -= 15
            db[f"iron{ctx.message.author}"] -= 7
            db[f"pickaxe{ctx.message.author}"] = 2
          else:
            await ctx.send("You do not have the required materials to craft this item")
        else:
          await ctx.send("You do not have the required materials to craft this item")
  
    elif item == "furnace":
      if db[f"furnace{ctx.message.author}"] >= 1:
        await ctx.send("You already have a furnace... For some reason you cant craft a second one!")
      else:
        if db[f"stone{ctx.message.author}"] >= 75:
          await ctx.send("You have now unlocked >smelting! Use this to smelt down ores to bars as well as smelting wood to create ash and charcoal!")
          db[f"stone{ctx.message.author}"] -= 75
          db[f"furnace{ctx.message.author}"] += 1
        else:
          await ctx.send("You dont have enough stone for this!")
          
    elif item == "anvil":
      if db[f"anvil{ctx.message.author}"] >= 1:
        await ctx.send("You already have an anvil, it would be a waste to make a second!")
      else:
        if db[f"iron_bar{ctx.message.author}"] >= 20:
          await ctx.send("Anvil unlocked! type >anvil to use this and create new tools, modifiers or upgrade your furnace!")
          db[f"iron_bar{ctx.message.author}"] -= 20
          db[f"anvil{ctx.message.author}"] += 1
        else:
          await ctx.send("You dont have enough iron bars to buy this item")

    elif item == "autominer":
      if db[f"autominer{ctx.message.author}"] >= 1:
        await ctx.send("For some reason as you are crafting your second autominer you forget the recipe and move on")
      else:
        if db[f"cog{ctx.message.author}"] >= 10:
          if db[f"drill_bit{ctx.message.author}"] >= 1:
            if db[f"stone{ctx.message.author}"] >= 100:
              if db[f"iron_bar{ctx.message.author}"] >= 15:
                await ctx.send("Enjoy your auto miner, to start it type >automine after that it will work forever!")
                db[f"autominer{ctx.message.author}"] += 1
                db[f"cog{ctx.message.author}"] -= 10
                db[f"drill_bit{ctx.message.author}"] -= 1
                db[f"stone{ctx.message.author}"] -= 100
                db[f"iron_bar{ctx.message.author}"] -= 15
              else:
                await ctx.send("Sorry you dont have enough iron bars for this!")
            else:
              await ctx.send("Sorry you dont have enough stone for this!")
          else:
            await ctx.send("Sorry you dont have enough drill bits for this!")
        else:
          await ctx.send("Sorry you dont have enough cogs for this!")
      
      
    
  else:
    await ctx.send("You need to have a workbench to do this!")

#make bars and fuel


@bot.command(name="furnace")
async def furnace_(ctx):
  global furnace

  if db[f"furnace{ctx.message.author}"] >= 1:
    await ctx.send("This is the furnace! Type >fuel [item] in order to fuel the furnace (wood and charcoal can be used so far) \n\n Add ores such as iron in order to make bars (this takes 1 fuel per bar and 1 minuite for it to smelt) or put wood in to create charcoal and ash. \n Type >smelt to do this")
  else:
    await ctx.send("You need to have a furnace to use this!")





@bot.command(name="fuel")
async def fuel(ctx, item: str):
  global dirt, stone, iron, iron_bar, wood, ash, charcoal, coins, cog, pickaxe, axe, autominer, Area, Forest_card, wheel_upgrade, chopping, mining_cooldown, smelting, Workbench, furnace, fuel_amount, anvil, modifier, razor_edge, fortune
  if db[f"furnace{ctx.message.author}"] >= 1:
    if item == "wood":
      if db[f"wood{ctx.message.author}"] >= 1:
        await ctx.send("Fuel + wood = {0}".format(db[f"fuel_amount{ctx.message.author}"]+1))
        db[f"wood{ctx.message.author}"] -= 1
        db[f"fuel_amount{ctx.message.author}"] += 1
      else:
        await ctx.send("you have no wood, use chop to gain wood")
    elif item == "charcoal":
      if db[f"charcoal{ctx.message.author}"] >= 1:
        await ctx.send("Fuel + charcoal = {0}".format(db[f"fuel_amount{ctx.message.author}"]+5))
        db[f"charcoal{ctx.message.author}"] -= 1
        db[f"fuel_amount{ctx.message.author}"] += 5
      else:
        await ctx.send("you have no charcoal")
    if item == "coal":
      if db[f"coal{ctx.message.author}"] >= 1:
        db[f"coal{ctx.message.author}"] -= 1
        db[f"fuel_amount{ctx.message.author}"] += 3
        await ctx.send("Fuel + coal = {0}".format(db[f"fuel_amount{ctx.message.author}"]))

      else:
        await ctx.send("You have no coal")
        
    else:
      await ctx.send("This was not an option.. use charcoal, wood or coal for fuel")
  else:
    await ctx.send("You need to have a furnace to use this!")


#smelting    



@bot.command(name="smelt")
async def smelt(ctx, item: str):
  global dirt, stone, iron, iron_bar, wood, ash, charcoal, coins, cog, pickaxe, axe, autominer, Area, Forest_card, wheel_upgrade, chopping, mining_cooldown, smelting, Workbench, furnace, fuel_amount, anvil, modifier, razor_edge, fortune
  if db[f"furnace{ctx.message.author}"] == 1:
    if db[f"fuel_amount{ctx.message.author}"] >= 1:
      if item == "wood":
        if db[f"wood{ctx.message.author}"] >= 1:
          async def smelt_wood():
              global wood, charcoal, ash, fuel_amount, smelting
              db[f"wood{ctx.message.author}"] -= 1
              db[f"charcoal{ctx.message.author}"] += 1
              db[f"ash{ctx.message.author}"] += 1
              db[f"fuel_amount{ctx.message.author}"] -= 1
              await ctx.send("\n you have now got {0} charcoal and {1} ash ".format(db[f"charcoal{ctx.message.author}"], db[f"{ctx.message.author}ash"]))
              db[f"smelting{ctx.message.author}"] = False
  
          if db[f"smelting{ctx.message.author}"] == True:
              await ctx.send("smelting already, please wait!")
          else:
              db[f"smelting{ctx.message.author}"] = True
              await ctx.send("In 1 minute you will have 1 extra charcoal and ash!")
              await asyncio.sleep(60.0)
              await smelt_wood()
        else:
          await ctx.send("You have no wood and therfore can smelt this item!")
      elif item == "iron":
        if db[f"iron{ctx.message.author}"] >= 1:
          async def smelt_iron():
              global iron, iron_bar, fuel_amount, smelting
              db[f"iron{ctx.message.author}"] -= 1
              db[f"iron_bar{ctx.message.author}"] += 1
              db[f"fuel_amount{ctx.message.author}"] -= 1
              await ctx.send("\n you have now got {0} iron bars".format(db[f"iron_bar{ctx.message.author}"]))
              db[f"smelting{ctx.message.author}"] = False
  
          if db[f"smelting{ctx.message.author}"] == True:
              await ctx.send("smelting already, please wait!")
          else:
              db[f"smelting{ctx.message.author}"] = True
              await ctx.send(f"In 1 minute you will have 1 extra iron bar!")
              await asyncio.sleep(60.0)
              await smelt_iron()
        else:
          await ctx.send("You have no iron and therfore you cannot smelt this item!")
      else:
        await ctx.send("Sorry this was not an option.. so far you can smelt wood and iron")
    else:
      await ctx.send("You have no fuel! type >fuel [item(charcoal or wood)] to get fuel")


      
  elif db[f"furnace{ctx.message.author}"] == 2:

    if db[f"fuel_amount{ctx.message.author}"] >= 1:
      if item == "wood":
        if db[f"wood{ctx.message.author}"] >= 3:
          async def smelt_wood():
              global wood, charcoal, ash, fuel_amount, smelting
              db[f"wood{ctx.message.author}"] -= 3
              db[f"charcoal{ctx.message.author}"] += 3
              db[f"ash{ctx.message.author}"] += 3
              db[f"fuel_amount{ctx.message.author}"] -= 1
              await ctx.send("\n you have now got {0} charcoal and {0} ash ".format(db[f"charcoal{ctx.message.author}"], db[f"ash{ctx.message.author}"]))
              db[f"smelting{ctx.message.author}"] = False
  
          if db[f"smelting{ctx.message.author}"] == True:
              await ctx.send("smelting already, please wait!")
          else:
              db[f"smelting{ctx.message.author}"] = True
              await ctx.send("In 1 minute you will have 3 extra charcoal and ash!")
              await asyncio.sleep(60.0)
              await smelt_wood()
        else:
          await ctx.send("You have not got enough wood and therfore can smelt this item!")
          
      elif item == "iron":
        if db[f"iron{ctx.message.author}"] >= 3:
          async def smelt_iron():
              global iron, iron_bar, fuel_amount, smelting
              db[f"iron{ctx.message.author}"] -= 3
              db[f"iron_bar{ctx.message.author}"] += 3
              db[f"fuel_amount{ctx.message.author}"] -= 1
              await ctx.send("\n you have now got {0} iron bars".format(db[f"iron_bar{ctx.message.author}"]))
              db[f"smelting{ctx.message.author}"] = False
  
          if db[f"smelting{ctx.message.author}"] == True:
              await ctx.send("smelting already, please wait!")
          else:
              db[f"smelting{ctx.message.author}"] = True
              await ctx.send(f"In 1 minute you will have 3 extra iron bars!")
              await asyncio.sleep(60.0)
              await smelt_iron()
        else:
          await ctx.send("You have no iron and therfore you cannot smelt this item!")
      else:
        await ctx.send("Sorry this was not an option.. so far you can smelt wood and iron")
    else:
      await ctx.send("You have no fuel! type >fuel [item(charcoal or wood)] to get fuel")
  else:
    await ctx.send("You need to have a furnace to use this!")

  




#anvil + forging items

    

@bot.command(name="anvil")
async def anvil_(ctx:commands.Context):
  global dirt, stone, iron, iron_bar, wood, ash, charcoal, coins, cog, pickaxe, axe, autominer, Area, Forest_card, wheel_upgrade, chopping, mining_cooldown, smelting, Workbench, furnace, fuel_amount, anvil, modifier, razor_edge, fortune

  if db[f"anvil{ctx.message.author}"] >= 1:
    
    await ctx.send("This is the anvil GUI, here you can use the anvil to create new tools, modifiers and machinery! Here are the possible items:\n\n Sharp_axe | 5 Iron bars + 12 wood | gives 3 wood per chop \n\n effciency axe modifier (type effciency to buy) | 20 wood + 100 stone | reduces the waiting time by 5% \n\n cog | 7 iron bars + workshop pickaxe (does not consume pickaxe) | can be used for more advanced machinery \n\n fortune pickaxe modifier (type fortune to buy) | 100 dirt + 50 stone + 25 iron + 10 wood | adds + 25% minerals per mine \n\n drill_bit | 15 iron bars + 150 stone | used to make more advanced machinery \n\n blast furnace (type furnace2 to craft) | 2 cogs + 200 stone + furnace | smelts 3 items at once with 1 fuel\n\n To make an item type >forge [item]!")
    
  else:
    await ctx.send("You need to have an anvil to use this!")





@bot.command(name="forge")
async def forge(ctx, item: str):
  global dirt, stone, iron, iron_bar, wood, ash, charcoal, coins, cog, pickaxe, axe, drill_bit, autominer, Area, Forest_card, wheel_upgrade, chopping, mining_cooldown, smelting, Workbench, furnace, fuel_amount, anvil, modifier, razor_edge, fortune, fortune_level, effciency, effciency_level

  if item == "sharp_axe":
    if db[f"axe{ctx.message.author}"] < 2:
      if db[f"iron_bar{ctx.message.author}"] >= 5:
        if db[f"wood{ctx.message.author}"] >= 12:
          await ctx.send("Enjoy your new axe! each chop you now gain 3 wood + modifiers!")
          db[f"axe{ctx.message.author}"] = 2
          db[f"iron_bar{ctx.message.author}"] -= 5
          db[f"wood{ctx.message.author}"] -= 12
        else:
          await ctx.send("You do not have enough wood for this item!")
      else:
        await ctx.send("You do not have enough iron bars for this item!")
    else:
      await ctx.send("You already have an axe better than this, it would be a waste to craft it")

  elif item == "effciency":
    if db[f"effciency_level{ctx.message.author}"] >= 1:
      await ctx.send("You already have effciency 1 or higher, you cannot craft this again")
    else:
      if db[f"wood{ctx.message.author}"] >= 20:
        if db[f"stone{ctx.message.author}"] >= 100:
          await ctx.send("You now have effciency 1 added on your axe (-5% waiting time)")
          db[f"wood{ctx.message.author}"] -= 20
          db[f"stone{ctx.message.author}"] -= 100
          db[f"effciency{ctx.message.author}"] -= 0.05
          db[f"effciency_level{ctx.message.author}"] = 1
        
        else:
          await ctx.send("You do not have enough stone for this item!")
      else:
        await ctx.send("You do not have enough wood for this item!")

  elif item == "cog":
    if db[f"iron_bar{ctx.message.author}"] >= 7:
      if db[f"pickaxe{ctx.message.author}"] >= 2:
        await ctx.send("You have made a cog, these are used to make machinery such as an autominer (recipie in >craft)")
        db[f"iron_bar{ctx.message.author}"] -= 7
        db[f"cog{ctx.message.author}"] += 1
      else:
        await ctx.send("You must have the workbench pickaxe unlocked to make a cog!")
    else:
      await ctx.send("You dont have enough iron bars for this!")
      
  elif item == "fortune":
    if db[f"fortune_level{ctx.message.author}"] >= 1:
      await ctx.send("Your fortune level is higher than 1 so you cannot craft this")
    else:
      if db[f"dirt{ctx.message.author}"] >= 100:
        if db[f"stone{ctx.message.author}"] >= 50:
          if db[f"iron{ctx.message.author}"] >= 25:
            if db[f"wood{ctx.message.author}"] >= 10:
              await ctx.send("You have now got fortune 1 on your pickaxe (+25% materials)")
              db[f"fortune_level{ctx.message.author}"] = 1
              db[f"fortune{ctx.message.author}"] += 0.25
              db[f"dirt{ctx.message.author}"] -= 100
              db[f"stone{ctx.message.author}"] -= 50
              db[f"iron{ctx.message.author}"] -= 25
              db[f"wood{ctx.message.author}"] -= 10
            else:
              await ctx.send("You dont have enough wood for this")
          else:
            await ctx.send("You dont have enough iron for this")
        else:
          await ctx.send("You do not have enough stone for this")
      else:
        await ctx.send("You dont have enough dirt for this")
      

  elif item == "drill_bit":
    if db[f"iron_bar{ctx.message.author}"] >= 15:
      if db[f"stone{ctx.message.author}"] >= 150:
        await ctx.send("You now have a drill bit, this can be used for crafting drills or an auto miner!")
        db[f"drill_bit{ctx.message.author}"] += 1
        db[f"iron_bar{ctx.message.author}"] -= 15
        db[f"stone{ctx.message.author}"] -= 150
      else:
        await ctx.send("You dont have enough stone for this item!")
    else:
      await ctx.send("You dont have enough iron bars for this item!")

  elif item == "furnace2":
    if db[f"furnace{ctx.message.author}"] >= 2:
      await ctx.send("You already have a furnace upgrade better than this or the same, it would be a waste to make a second")
    else:
      if db[f"cog{ctx.message.author}"] >= 2:
        if db[f"stone{ctx.message.author}"] >= 200:
          await ctx.send("Enjoy your new furnace upgrade, now you will smelt 3 items per smelt!")
          db[f"cog{ctx.message.author}"] -= 2
          db[f"stone{ctx.message.author}"] -= 200
          db[f"furnace{ctx.message.author}"] = 2
        else:
          await ctx.send("You do not have enough stone for this")
      else:
        await ctx.send("You do not have enough cogs for this")





@bot.command(name="garage")
async def garage(ctx):
  if db[f"garage{ctx.message.author}"] >= 1:
    await ctx.send("welcome to the garage! Here you can make vehicles and drills: \n Vehicles: \n\n Wheel chair (Type wheel_chair to buy) | 30 iron bars + 3 cogs | Lets you travel to the second area \n\n Bike (Type bike to buy) | 50 iron bars + 5 cogs + 10 copper | Lets you travel to the third area \n\n horse cart (Type horse_cart to buy| 2 hourses + 120 wood + 2 cogs + 20 copper | Lets you travel to the fourth area \n\n Drills: \n Iron Drill (Type iron to buy) | 1 drill bit + 60 iron ore + 45 iron bars | Lets you mine in area 3 \n\n Copper Drill (Type copper to buy) | 1 drill bit + 45 copper + 20 iron bars | Lets you mine in area 4 \n\n To create these items type >manufacture [item]")
  else:
    await ctx.send("You need to have a garage to use this!")


@bot.command(name="manufacture")
async def manufacture(ctx, item: str):
  if db[f"garage{ctx.message.author}"] >= 1:
    
    if item == "wheel_chair":
      if db[f"iron_bar{ctx.message.author}"] >= 30:
        if db[f"cog{ctx.message.author}"] >= 3:
          db[f"iron_bar{ctx.message.author}"] -= 30
          db[f"cog{ctx.message.author}"] -= 3
          db[f"wheel_chair{ctx.message.author}"] = 1
          await ctx.send("You now have a wheelchair! Type >travel 2 to go to the next area!")
        else:
          await ctx.send("You do not have enough cogs for this!")
      else:
        await ctx.send("You do not have enough iron bars for this!")
        
    elif item == "bike":
      if db[f"iron_bar{ctx.message.author}"] >= 50:
        if db[f"cog{ctx.message.author}"] >= 5:
          if db[f"copper{ctx.message.author}"] >= 10:
            db[f"iron_bar{ctx.message.author}"] -= 50
            db[f"cog{ctx.message.author}"] -= 5
            db[f"copper{ctx.message.author}"] -= 10
            db[f"bike{ctx.message.author}"] = 1
            await ctx.send("You now have a bike! Type >travel 3 to go to the next area")
          else:
            await ctx.send("You dont have enough copper for this!")
        else:
          await ctx.send("You dont have enough cogs for this!")
      else:
        await ctx.send("You dont have enough iron bars for this!")

    elif item == "horse cart":
      if db[f"horse{ctx.message.author}"] >= 2:
        if db[f"wood{ctx.message.author}"] >= 120:
          if db[f"cog{ctx.message.author}"] >= 2:
            if db[f"copper{ctx.message.author}"] >= 20:
              db[f"horse{ctx.message.author}"] -= 2
              db[f"wood{ctx.message.author}"] -= 120
              db[f"cog{ctx.message.author}"] -= 2
              db[f"copper{ctx.message.author}"] -= 20
              db[f"horse_cart{ctx.message.author}"] = 1
              await ctx.send("You now have a horse cart! Type >travel 4 to go to the next area!")
            else:
              await ctx.send("You dont have enough copper for this!")
          else:
            await ctx.send("You dont have enough cogs for this!")
        else:
          await ctx.send("You dont have enough wood for this!")
      else:
        await ctx.send("You dont have enough horses for this!")

    elif item == "iron":
      if db[f"drill_bit{ctx.message.author}"] >= 1:
        if db[f"iron{ctx.message.author}"] >= 60:
          if db[f"iron_bar{ctx.message.author}"] >= 45:
            db[f"drill_bit{ctx.message.author}"] -= 1
            db[f"iron{ctx.message.author}"] -= 60
            db[f"iron_bar{ctx.message.author}"] -= 45
            db[f"pickaxe{ctx.message.author}"] = 3
            await ctx.send("You can now mine in the third area!")
          else:
            await ctx.send("You dont have enough iron bars for this")
        else:
          await ctx.send("You dont have enough iron for this")
      else:
        await ctx.send("You dont have enough drill bits for this")
      
      
  else:
    await ctx.send("You need a garage to use this command")


def setup(bot):
  bot.add_command(craft)
  bot.add_command(make)
  bot.add_command(furnace_)
  bot.add_command(fuel)
  bot.add_command(smelt)
  bot.add_command(anvil_)
  bot.add_command(forge)
  bot.add_command(garage)
  bot.add_command(manufacture)