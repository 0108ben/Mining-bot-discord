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

# MAIN SHOP

@bot.command(name="shop")
async def shop(ctx):
  await ctx.send("Welcome to the shop! \n\n Broken_pickaxe | Free | the starter pickaxe, I would work for a new one quick! \n\n Forest area1 (to buy type Forest) | 40 coins | allows you to access the forest \n\n Workbench | 150 coins + 15 wood | lets you craft different workstations such as an anvil or Furnace \n\n axe | 250 coins + 3 iron | use this to cut down trees \n\n razor edge modifier (to buy type razoredge) | 500 coins + 7 wood | buy this to put it on your axe | gives + 1 wood per chop \n\n Type >buy [item] in order to buy an item")




@bot.command(name="buy")
async def buy(ctx, item: str):
  global dirt, stone, iron, iron_bar, wood, ash, charcoal, coins, cog, pickaxe, axe, autominer, Area, Forest_card, wheel_upgrade, chopping, mining_cooldown, smelting, Workbench, furnace, fuel_amount, anvil, modifier, razor_edge, fortune
  if item == "broken_pickaxe"or item == "Broken_pickaxe":
      if db[f"pickaxe{ctx.message.author}"] >= 1:
          await ctx.send("You already have a pickaxe better than this.. why would you even want this??")
      else:
          await ctx.send("Good luck with mining!!")
          db[f"pickaxe{ctx.message.author}"] = 1
  elif item == "Forest" or item == "forest":
      if db[f"Forest_card{ctx.message.author}"] >= 1:
          await ctx.send("You already have a forest card that lets you access this area!")
      else:
          if db[f"coins{ctx.message.author}"] >= 40:
              await ctx.send("Congratulations!! You have gained your first forest card, type chop to gain some wood once you get an axe!")
              db[f"coins{ctx.message.author}"] -= 40
              db[f"Forest_card{ctx.message.author}"] = 1
          else:
              await ctx.send("Sorry but you cant afford this right now. "
                             "To make money use the mine and the sell command to make money")
  elif item == "Workbench" or item == "workbench":
      if db[f"Workbench{ctx.message.author}"] >= 1:
          await ctx.send("You already have a working workbench")
      else:
          if db[f"coins{ctx.message.author}"] >= 150:
              if db[f"wood{ctx.message.author}"] >= 15:
                  await ctx.send("Enjoy your new workbench use the command >craft to use it!!")
                  db[f"wood{ctx.message.author}"] -= 15
                  db[f"coins{ctx.message.author}"] -= 150
                  db[f"Workbench{ctx.message.author}"] = 1
              else:
                  await ctx.send("Sorry you dont have enough wood to buy this item!")
          else:
              await ctx.send("sorry you dont have enough coins to buy this item")

  elif item == "axe":
    if db[f"axe{ctx.message.author}"] >= 1:
      await ctx.send("You already have an axe, I doubt you need another")
    else:
      if db[f"coins{ctx.message.author}"] >= 250:
        if db[f"iron{ctx.message.author}"] >= 3:
          await ctx.send("Have fun creating global warming!")
          db[f"coins{ctx.message.author}"] -= 250
          db[f"iron{ctx.message.author}"] -= 3
          db[f"axe{ctx.message.author}"] = 1
        else:
          await ctx.send("Sorry you dont have enough iron for this item")
      else:
        await ctx.send("Sorry you dont have enough coins for this item")

  elif item == "razoredge":
    if db[f"razor_edge{ctx.message.author}"] >= 1:
      await ctx.send("You have already got this level of this modifer or an even better one, why would you want a worse modifier?")
    else:
      if db[f"coins{ctx.message.author}"] >= 500:
        if db[f"wood{ctx.message.author}"] >= 7:
          if db[f"axe{ctx.message.author}"] >= 1:
            await ctx.send("Good job!! *razor edge has been applied to your axe, you now get 1 extra wood per chop*")
            db[f"razor_edge{ctx.message.author}"] += 1
            db[f"coins{ctx.message.author}"] -= 500
            db[f"wood{ctx.message.author}"] -= 7
          else:
            await ctx.send("You dont have an axe yet... How did you get wood???")
        else:
          await ctx.send("Sorry you dont have enough wood for this item")
      else:
        await ctx.send("Sorry you dont have enough coins for this item")
  
  else:
    await ctx.send("sorry this wasnt an option!")


    

@bot.command(name="shelter_shop")
async def shelter_shop(ctx):
  await ctx.send("Welcome to Walls R Us, what type of wall would you like to buy today? \n\n Living room walls (type livingroom_wall to buy) | 60 wood | Once 4 walls have been bought use the >build command to create a livingroom (this room is required to buy other walls) \n\n Garage walls (type garage_wall to buy) | 40 wood + 130 stone | Once 4 walls have been bought use the >build command to create a garage (once all 4 have been bought type >garage for more info) \n\n Bathroom walls (type bathroom_wall to buy) | 100 stone | Once 4 walls have been bought use the >build command to create a bathroom. This is for some wierd people that requested >poop.. so strange \n\n Bedroom walls (type bedroom_wall to buy) | 140 wood + 50 stone | Who knew a bedroom was required to beat a discord game.. Once 4 walls have been bought use the >build command to create a bedroom \n\n type >buywall [wall name]")


@bot.command(name="buywall")
async def buywall(ctx, item: str):
  if item == "livingroom_wall":
    if db[f"livingroom_wall{ctx.message.author}"] >= 4:
      await ctx.send("You already have 4 walls.. why would you want more?")
    else:
      if db[f"wood{ctx.message.author}"] >= 60:
        db[f"livingroom_wall{ctx.message.author}"] += 1
        db[f"wood{ctx.message.author}"] -= 60
        await ctx.send("Enjoy your wall! you need {0} walls to make a living room".format(4 - db[f"livingroom_wall{ctx.message.author}"]))
        if db[f"livingroom_wall{ctx.message.author}"] >= 4:
          await ctx.send("You have enough walls to make a living room! type >build [room name] (this will cost you 450 coins per room)")
        else:
          pass
      else:
        await ctx.send("You dont have enough wood to buy this!")

        
  elif item == "garage_wall":
    if db[f"livingroom{ctx.message.author}"] < 1:
      await ctx.send("You need to have a living room before you can buy this!")
    else:
      if db[f"wood{ctx.message.author}"] >= 40:
        if db[f"stone{ctx.message.author}"] >= 130:
          db[f"garage_wall{ctx.message.author}"] += 1
          db[f"wood{ctx.message.author}"] -= 40
          db[f"stone{ctx.message.author}"] -= 130
          await ctx.send("Enjoy your wall! you need {0} walls to make a garage".format(4 - db[f"garage_wall{ctx.message.author}"]))
          if db[f"garage_wall{ctx.message.author}"] >= 4:
            await ctx.send("You have enough walls to make a garage! type >build [room name] (this will cost you 450 coins per room)")
          else:
            pass
        else:
          await ctx.send("You dont have enough stone to buy this")
      else:
        await ctx.send("You dont have enough wood to buy this")

  
  elif item == "bathroom_wall":
    if db[f"livingroom{ctx.message.author}"] < 1:
      await ctx.send("You need to have a living room before you can buy this!")
    else:
      if db[f"stone{ctx.message.author}"] >= 100:
        db[f"stone{ctx.message.author}"] -= 100
        db[f"bathroom_wall{ctx.message.author}"] += 1
        await ctx.send("Enjoy your wall! you need {0} walls to make a bathroom".format(4 - db[f"bathroom_wall{ctx.message.author}"]))
        if db[f"bathroom_wall{ctx.message.author}"] >= 4:
          await ctx.send("You have enough walls to make a bathroom! type >build [room name] (this will cost you 450 coins per room)")
        else:
          pass
      else:
        await ctx.send("You dont have enough stone to make this item")

  elif item == "bedroom_wall":
    if db[f"livingroom{ctx.message.author}"] < 1:
      await ctx.send("You need to have a living room before you can buy this!")
    else:
      if db[f"wood{ctx.message.author}"] >= 140:
        if db[f"stone{ctx.message.author}"] >= 50:
          db[f"bedroom_wall{ctx.message.author}"] += 1
          db[f"wood{ctx.message.author}"] -= 40
          db[f"stone{ctx.message.author}"] -= 130
          await ctx.send("Enjoy your wall! you need {0} walls to make a bedroom".format(4 - db[f"bedroom_wall{ctx.message.author}"]))
          if db[f"bedroom_wall{ctx.message.author}"] >= 4:
            await ctx.send("You have enough walls to make a bedroom! type >build [room name] (this will cost you 450 coins per room)")
          else:
            pass
        else:
          await ctx.send("You do not have enough stone for this item")
      else:
        await ctx.send("You do not have enough wood for this item")

  else:
    await ctx.send("This was not an option!")


@bot.command(name="build")
async def build(ctx, item: str):
  if item == "livingroom":
    if db[f"livingroom_wall{ctx.message.author}"] >= 4:
      if db[f"livingroom{ctx.message.author}"] < 1:
        if db[f"coins{ctx.message.author}"] >= 450:
          db[f"livingroom_wall{ctx.message.author}"] -=4
          db[f"livingroom{ctx.message.author}"] += 1
          db[f"coins{ctx.message.author}"] -= 450
          await ctx.send("*insert building noises here* The livingroom has been built! You can now buy all other walls in the shelter_shop")
        else:
          await ctx.send("You dont have enough coins for this")
      else:
        await ctx.send("You already have a living room!!")
    else:
      await ctx.send("You need 4 walls in order to do this")

      
  elif item == "garage":
    if db[f"garage_wall{ctx.message.author}"] >= 4:
      if db[f"garage{ctx.message.author}"] < 1:
        if db[f"coins{ctx.message.author}"] >= 450:
          db[f"garage_wall{ctx.message.author}"] -=4
          db[f"garage{ctx.message.author}"] += 1
          db[f"coins{ctx.message.author}"] -= 450
          await ctx.send("*insert building noises here* The garage has been built! You can now use >garage")
        else:
          await ctx.send("You dont have enough coins for this")
      else:
        await ctx.send("You already have a garage!!")
    else:
      await ctx.send("You need 4 walls in order to do this") 

  elif item == "bathroom":
    if db[f"bathroom_wall{ctx.message.author}"] >= 4:
      if db[f"bathroom{ctx.message.author}"] < 1:
        if db[f"coins{ctx.message.author}"] >= 450:
          db[f"bathroom_wall{ctx.message.author}"] -=4
          db[f"bathroom{ctx.message.author}"] += 1
          db[f"coins{ctx.message.author}"] -= 450
          await ctx.send("*insert building noises here* The bathroom has been built! You can now use >poop, I dont even know why thats a command")
        else:
          await ctx.send("You dont have enough coins for this")
      else:
        await ctx.send("You already have a bathroom!!")
    else:
      await ctx.send("You need 4 walls in order to do this")

      
  elif item == "bedroom":
    if db[f"bedroom_wall{ctx.message.author}"] >= 4:
      if db[f"bedroom{ctx.message.author}"] < 1:
        if db[f"coins{ctx.message.author}"] >= 450:
          db[f"bedroom_wall{ctx.message.author}"] -=4
          db[f"bedroom{ctx.message.author}"] += 1
          db[f"coins{ctx.message.author}"] -= 450
          await ctx.send("*insert building noises here* The bedroom has been built! There is no use for a bed in a discord game.. Why would you even buy this")
        else:
          await ctx.send("You dont have enough coins for this")
      else:
        await ctx.send("You already have a bathroom!!")
    else:
      await ctx.send("You need 4 walls in order to do this")

  else:
    await ctx.send("This is not an option, you can use bedroom, bathroom, garage, livingroom")







@bot.command(name="animals")
async def animals(ctx):
  if db[f"Area{ctx.message.author}"] == 3:
    await ctx.send("You look into the shed on the field and see: \n\n cow (100 coins) \n\n pig (75 coins) \n\n horse (230 coins) \n\n ??? (5000 coins) \n\n to buy an animal type >farm [animal]")
  else:
    await ctx.send("You need to get to a different area to use this!")


@bot.command(name="farm")
async def farm(ctx, animal: str):
  if db[f"Area{ctx.message.author}"] == 3:
    if animal == "cow":
      if db[f"coins{ctx.message.author}"] >= 100:
        await ctx.send("You leave the coins on a barrel of hay and somehow carry the cow out of the shed")
        db[f"cow{ctx.message.author}"] += 1
        db[f"coins{ctx.message.author}"] -= 100
      else:
        await ctx.send("You dont have enough coins for this!")
    elif animal == "pig":
      if db[f"coins{ctx.message.author}"] >= 75:
        await ctx.send("You leave the coins on a barrel of hay and somehow carry the pig out of the shed")
        db[f"pig{ctx.message.author}"] += 1
        db[f"coins{ctx.message.author}"] -= 75
      else:
        await ctx.send("You dont have enough coins for this!")
    elif animal == "horse":
      if db[f"coins{ctx.message.author}"] >= 230:
        await ctx.send("You leave the coins on a barrel of hay and ride the horse out of the shed")
        db[f"horse{ctx.message.author}"] += 1
        db[f"coins{ctx.message.author}"] -= 230
      else:
        await ctx.send("You dont have enough coins for this!")
  
    elif animal == "???":
      if db[f"coins{ctx.message.author}"] >= 5000:
        animal_choice = random.randint(1, 100)
        if animal_choice >= 90:
          await ctx.send("You leave the coins on a barrel of hay and and run inside of the shed, you look around and find a unicorn!!?! You jump on its back and it flys you back home. \n Area 8 unlocked!!")
          db[f"unicorn{ctx.message.author}"] += 1
          db[f"coins{ctx.message.author}"] -= 5000
        elif 60 <= animal_choice < 90:
          await ctx.send("You leave the coins on a barrel of hay and and run inside of the shed, you look around and find a box of iron and copper. You push the box out and take 150 copper and 200 iron")
          db[f"iron{ctx.message.author}"] += 200
          db[f"copper{ctx.message.author}"] += 150
  
        else:
          await ctx.send("You leave the coins on a barrel of hay and run inside of the shed, you look around and find a frog?! you put him in your pocket and run off")
        db[f"frog{ctx.message.author}"] += 1
        db[f"coins{ctx.message.author}"] -= 5000
          
      else:
        await ctx.send("You dont have enough coins for this!")
  else:
    await ctx.send("You need to get to a different area to use this!")

@bot.command(name="smeltery_shop")
async def smeltery_shop(ctx):
  await ctx.send("Work in progress")



def setup(bot):
  bot.add_command(shop)
  bot.add_command(buy)
  bot.add_command(shelter_shop)
  bot.add_command(buywall)
  bot.add_command(build)
  bot.add_command(animals)
  bot.add_command(farm)