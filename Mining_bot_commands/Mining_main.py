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

# mine command

@bot.command(name="mine")
async def mine(ctx):
  try:
    global pickaxe, Area, dirt, stone, iron, mining_cooldown, modifier, mines, mining_level
  
    def Gains():
      gain = 0
  
      if db[f"mining_level{ctx.message.author}"] < 10:
        pass
      
      elif 10 <= db[f"mining_level{ctx.message.author}"] < 20:
        gain += 5
        
      elif 20 <= db[f"mining_level{ctx.message.author}"] < 30:
        gain += 10
  
      elif 30 <= db[f"mining_level{ctx.message.author}"] < 40:
        gain += 15
  
      elif 40 <= db[f"mining_level{ctx.message.author}"] < 50:
        gain += 20
  
      elif 50 <= db[f"mining_level{ctx.message.author}"] < 60:
        gain += 25
  
      elif 60 <= db[f"mining_level{ctx.message.author}"] < 70:
        gain += 30
  
      elif 70 <= db[f"mining_level{ctx.message.author}"] < 80:
        gain += 35
  
      elif 80 <= db[f"mining_level{ctx.message.author}"] < 90:
        gain += 40
  
      elif 90 <= db[f"mining_level{ctx.message.author}"] < 100:
        gain += 45
  
      else:
        gain += 50
        gain = gain*2
  
    def mineingcooldown():
        global mining_cooldown
        db[f"mining_cooldown{ctx.message.author}"] = False
  
    if db[f"mining_cooldown{ctx.message.author}"]:
        await ctx.send("sorry, this command is still on cooldown!")
    else:
      db[f"mines{ctx.message.author}"] += 1
      if db[f"mining_level{ctx.message.author}"] == 0:
        if db[f"mines{ctx.message.author}"] >= 10:
          await ctx.send("Mining Level up! For each mining level you get you gain an extra resource, for every 10 levels you gain an extra 5 on top (level 100 gives a secret bonus!)")
          db[f"mining_level{ctx.message.author}"] += 1
        else:
          pass
      else:
        amount_for_level = (db[f"mining_level{ctx.message.author}"] ** 2) + 10
        if db[f"mines{ctx.message.author}"] >= amount_for_level:
          await ctx.send("Mining level up!")
          db[f"mining_level{ctx.message.author}"] += 1
          if db[f"mining_level{ctx.message.author}"] == 100:
            await ctx.send("WOW.. minging level 100 unlocked! the resources gained from every mine is now doubled!")
          else:
            pass
        else:
          pass
  
      if db[f"Area{ctx.message.author}"] == 1:
  
        Gains()
  
          
        if db[f"pickaxe{ctx.message.author}"] == 1:
          db[f"mining_cooldown{ctx.message.author}"] = True
  
          gain = (25 * db[f"fortune{ctx.message.author}"]) + db[f"mining_level{ctx.message.author}"]
          
          gain = gain // 1
          gain = int(gain)
          await ctx.send(f"You will get {gain} minerals from this mine")
          for i in range(gain):
            chance = [i for i in range(100)]
            material = random.choice(chance)
  
            if material <= 60:
                db[f"dirt{ctx.message.author}"] += 1
            elif 60 < material <= 90:
                db[f"stone{ctx.message.author}"] += 1
            elif material > 90:
                db[f"iron{ctx.message.author}"] += 1
  
          await ctx.send("You now have:\n {0} dirt \n {1} stone\n {2} iron".format(db[f"dirt{ctx.message.author}"], db[f"stone{ctx.message.author}"], db[f"iron{ctx.message.author}"]))
          threading.Timer(60.0, mineingcooldown).start()
          await ctx.send("You can use this command again in 1 minutes!")
  
        elif db[f"pickaxe{ctx.message.author}"] >= 2:
          db[f"mining_cooldown{ctx.message.author}"] = True
          gain = (37 * db[f"fortune{ctx.message.author}"]) + db[f"mining_level{ctx.message.author}"]
          gain = gain // 1
          gain = int(gain)
          
          await ctx.send("You will get {0} minerals from this mine".format(gain))
          for i in range(gain):
            chance = [i for i in range(100)]
            material = random.choice(chance)
  
            if material <= 60:
                db[f"dirt{ctx.message.author}"] += 1
            elif 60 < material <= 90:
                db[f"stone{ctx.message.author}"] += 1
            elif material > 90:
                db[f"iron{ctx.message.author}"] += 1
  
          await ctx.send("You now have:\n {0} dirt \n {1} stone\n {2} iron".format(db[f"dirt{ctx.message.author}"], db[f"stone{ctx.message.author}"], db[f"iron{ctx.message.author}"]))
          threading.Timer(60.0, mineingcooldown).start()
          await ctx.send("You can use this command again in 1 minutes!")
  
        else:
          await ctx.send("To be able to use this command you must have a pickaxe.. "
                    "go to the shop for the starter pickaxe (broken pickaxe)")
  
      #AREA 2
          
      elif db[f"Area{ctx.message.author}"] == 2 or db[f"Area{ctx.message.author}"] == 3:
  
        Gains()
  
          
        if db[f"pickaxe{ctx.message.author}"] <= 1:
          await ctx.send("You need to have a workshop pickaxe in order to mine here!")
  
        else:
          db[f"mining_cooldown{ctx.message.author}"] = True
          gain = (37 * db[f"fortune{ctx.message.author}"]) + db[f"mining_level{ctx.message.author}"]
          gain = gain // 1
          gain = int(gain)
          
          await ctx.send("You will get {0} minerals from this mine".format(gain))
          for i in range(gain):
            chance = [i for i in range(100)]
            material = random.choice(chance)
  
            if material <= 60:
                db[f"stone{ctx.message.author}"] += 1
            elif 60 < material <= 90:
                db[f"brick{ctx.message.author}"] += 1
            elif material > 90:
                db[f"copper{ctx.message.author}"] += 1
  
          await ctx.send("You now have:\n {0} stone \n {1} brick\n {2} copper".format( db[f"stone{ctx.message.author}"], db[f"brick{ctx.message.author}"], db[f"copper{ctx.message.author}"]))
          threading.Timer(60.0, mineingcooldown).start()
          await ctx.send("You can use this command again in 1 minutes!")
  
      elif db[f"Area{ctx.message.author}"] == 4:
        if db[f"pickaxe{ctx.message.author}"] >= 4:
          Gains()
          db[f"mining_cooldown{ctx.message.author}"] = True
          gain = (37 * db[f"fortune{ctx.message.author}"]) + db[f"mining_level{ctx.message.author}"]
          gain = gain // 1
          gain = int(gain)
          
          await ctx.send("You will get {0} minerals from this mine".format(gain))
          for i in range(gain):
            chance = [i for i in range(100)]
            material = random.choice(chance)
  
            if material <= 85:
                db[f"stone{ctx.message.author}"] += 1
            elif material > 85:
                try:
                  db[f"coal{ctx.message.author}"] += 1
                except:
                  db[f"coal{ctx.message.author}"] = 1
  
          await ctx.send("You now have:\n {0} stone \n {1} coal".format( db[f"stone{ctx.message.author}"], db[f"coal{ctx.message.author}"]))
          threading.Timer(60.0, mineingcooldown).start()
          await ctx.send("You can use this command again in 1 minutes!")
  
  
        
  
      
      else:
        await ctx.send("error")
  except:
    await ctx.send("Hello! Please type start to begin using me :smiley:")




@bot.command(name="sell")
async def sell(ctx, mineral: str, amount: str):
  global dirt, iron, stone, coins
  try:
      amount = int(amount)
      if mineral == "dirt":
        if amount < 1:
          await ctx.send("NO, NO BREAK BOT, NOT AGAIN")
        else:
          if db[f"dirt{ctx.message.author}"] >= amount:
              dirt_coins = amount * 1
              await ctx.send(f"Selling {amount} dirt for {dirt_coins} coins")
              db[f"coins{ctx.message.author}"] += dirt_coins
              await ctx.send("Coins + {0} = {1}".format(dirt_coins, db[f"coins{ctx.message.author}"]))
              db[f"dirt{ctx.message.author}"] -= amount
          else:
              await ctx.send("You dont have enough dirt to sell that much! You have {0} dirt".format(db[f"dirt{ctx.message.author}"]))
    
      elif mineral == "stone":
        if amount < 1:
          await ctx.send("NO, NO BREAK BOT, NOT AGAIN")
        else:
          if db[f"stone{ctx.message.author}"] >= amount:
              stone_coins = amount * 3
              await ctx.send(f"Selling {amount} stone for {stone_coins} coins")
              db[f"coins{ctx.message.author}"] += stone_coins
              await ctx.send("Coins + {0} = {1}".format(stone_coins, db[f"coins{ctx.message.author}"]))
              db[f"stone{ctx.message.author}"] -= amount
          else:
              await ctx.send(f"You dont have enough stone to sell that much! You have {stone} stone")
      
      elif mineral == "iron":
        if amount < 1:
          await ctx.send("NO, NO BREAK BOT, NOT AGAIN")
        else:
          if db[f"iron{ctx.message.author}"] >= amount:
              iron_coins = amount * 15
              await ctx.send(f"Selling {amount} iron for {iron_coins} coins")
              db[f"coins{ctx.message.author}"] += iron_coins
              await ctx.send("Coins + {0} = {1}".format(iron_coins, db[f"coins{ctx.message.author}"]))
              db[f"iron{ctx.message.author}"] -= amount
          else:
              await ctx.send("You dont have enough iron to sell that much! You have {0} iron".format(db[f"iron{ctx.message.author}"]))

      else:
        await ctx.send("This is not a mineral!")

  except:
    if amount == "all":
      if mineral == "dirt":
        dirt_coins = db[f"dirt{ctx.message.author}"] * 1
        await ctx.send("Selling {0} dirt for {1} coins".format(db[f"dirt{ctx.message.author}"], dirt_coins))
        db[f"coins{ctx.message.author}"] += dirt_coins
        await ctx.send("Coins + {0} = {1}".format(dirt_coins, db[f"coins{ctx.message.author}"]))
        db[f"dirt{ctx.message.author}"] = 0

      elif mineral == "stone":
        stone_coins = db[f"stone{ctx.message.author}"] * 1
        await ctx.send("Selling {0} stone for {1} coins".format(db[f"stone{ctx.message.author}"], stone_coins))
        db[f"coins{ctx.message.author}"] += stone_coins
        await ctx.send("Coins + {0} = {1}".format(stone_coins, db[f"coins{ctx.message.author}"]))
        db[f"stone{ctx.message.author}"] = 0

      elif mineral == "iron":
        iron_coins = db[f"iron{ctx.message.author}"] * 1
        await ctx.send("Selling {0} iron for {1} coins".format(db[f"iron{ctx.message.author}"], iron_coins))
        db[f"coins{ctx.message.author}"] += iron_coins
        await ctx.send("Coins + {0} = {1}".format(iron_coins, db[f"coins{ctx.message.author}"]))
        db[f"iron{ctx.message.author}"] = 0

      else:
        await ctx.send("This is not a mineral!")

    else:
      await ctx.send("This is not an amount. Please type 'all' or a whole number")
        





@bot.command(name="sellall")
async def sellall(ctx):
  global dirt, iron, stone, coins


  await ctx.send("selling")
  dirt_coins = db[f"dirt{ctx.message.author}"] * 1
  stone_coins = db[f"stone{ctx.message.author}"] * 3
  iron_coins = db[f"iron{ctx.message.author}"] * 15
  db[f"dirt{ctx.message.author}"] = 0
  db[f"stone{ctx.message.author}"] = 0
  db[f"iron{ctx.message.author}"] = 0
  db[f"coins{ctx.message.author}"] += dirt_coins + stone_coins + iron_coins
  await ctx.send("You now have {0} coins".format(db[f"coins{ctx.message.author}"]))





@bot.command(name="chop")
async def chop(ctx):
  global chopping, wood, effciency, chopping_level, chops
  
  if db[f"Forest_card{ctx.message.author}"] == 1 and db[f"axe{ctx.message.author}"] >= 1:
      amount_gained = 0
      if db[f"chopping_level{ctx.message.author}"] < 10:
        pass
      
      elif 10 <= db[f"chopping_level{ctx.message.author}"] < 20:
        amount_gained += 5
        
      elif 20 <= db[f"chopping_level{ctx.message.author}"] < 30:
        amount_gained += 10

      elif 30 <= db[f"chopping_level{ctx.message.author}"] < 40:
        amount_gained += 15

      elif 40 <= db[f"chopping_level{ctx.message.author}"] < 50:
        amount_gained += 20

      elif 50 <= db[f"chopping_level{ctx.message.author}"] < 60:
        amount_gained += 25

      elif 60 <= db[f"chopping_level{ctx.message.author}"] < 70:
        amount_gained += 30

      elif 70 <= db[f"chopping_level{ctx.message.author}"] < 80:
        amount_gained += 35

      elif 80 <= db[f"chopping_level{ctx.message.author}"] < 90:
        amount_gained += 40

      elif 90 <= db[f"chopping_level{ctx.message.author}"] < 100:
        amount_gained += 45

      else:
        amount_gained += 350

      async def get_wood():
          global wood, razor_edge, chopping
          amount_gained = 0

          if db[f"chopping_level{ctx.message.author}"] < 10:
            pass
          
          elif 10 <= db[f"chopping_level{ctx.message.author}"] < 20:
            db[f"wood{ctx.message.author}"] += 5
            amount_gained += 5
            
          elif 20 <= db[f"chopping_level{ctx.message.author}"] < 30:
            db[f"wood{ctx.message.author}"] += 10
            amount_gained += 10

          elif 30 <= db[f"chopping_level{ctx.message.author}"] < 40:
            db[f"wood{ctx.message.author}"] += 15
            amount_gained += 15

          elif 40 <= db[f"chopping_level{ctx.message.author}"] < 50:
            db[f"wood{ctx.message.author}"] += 20
            amount_gained += 20

          elif 50 <= db[f"chopping_level{ctx.message.author}"] < 60:
            db[f"wood{ctx.message.author}"] += 25
            amount_gained += 25

          elif 60 <= db[f"chopping_level{ctx.message.author}"] < 70:
            db[f"wood{ctx.message.author}"] += 30
            amount_gained += 30

          elif 70 <= db[f"chopping_level{ctx.message.author}"] < 80:
            db[f"wood{ctx.message.author}"] += 35
            amount_gained += 35

          elif 80 <= db[f"chopping_level{ctx.message.author}"] < 90:
            db[f"wood{ctx.message.author}"] += 40
            amount_gained += 40

          elif 90 <= db[f"chopping_level{ctx.message.author}"] < 100:
            db[f"wood{ctx.message.author}"] += 45
            amount_gained += 45

          else:
            db[f"wood{ctx.message.author}"] += 50
            db[f"wood{ctx.message.author}"] += 150*2
            amount_gained += 350
        
          if db[f"axe{ctx.message.author}"] == 1:
            db[f"wood{ctx.message.author}"] += 1 + db[f"razor_edge{ctx.message.author}"] + db[f"chopping_level{ctx.message.author}"]
          elif db[f"axe{ctx.message.author}"] == 2:
            db[f"wood{ctx.message.author}"] += 3 + db[f"razor_edge{ctx.message.author}"] + db[f"chopping_level{ctx.message.author}"]
          await ctx.send("\n you have now got {0} oak wood".format(db[f"wood{ctx.message.author}"]))
          db[f"chopping{ctx.message.author}"] = False

      if db[f"chopping{ctx.message.author}"]:
          await ctx.send("chopping wood already, please wait!")
        
      else:
          db[f"chops{ctx.message.author}"] += 1
          if db[f"chopping_level{ctx.message.author}"] == 0:
            if db[f"chops{ctx.message.author}"] >= 5:
              await ctx.send("Chopping Level up! For each chopping level you get you gain an extra wood, for every 10 levels you gain an extra 5 on top (level 100 gives a secret bonus!)")
              db[f"chopping_level{ctx.message.author}"] += 1
            else:
              pass
          else:
            amount_for_level = (db[f"chopping_level{ctx.message.author}"] ** 2) + 5
            if db[f"chops{ctx.message.author}"] >= amount_for_level:
              await ctx.send("Chopping level up!")
              db[f"chopping_level{ctx.message.author}"] += 1
              if db[f"chopping_level{ctx.message.author}"] == 100:
                await ctx.send("WOW.. chopping level 100 unlocked! The wood gained from every chop is now doubled!")
              else:
                pass
            else:
              pass
                    
          db[f"chopping{ctx.message.author}"] = True
          time = 90.0*db[f"effciency{ctx.message.author}"]
          if db[f"axe{ctx.message.author}"] == 1:
            await ctx.send("In {0} seconds you will have {1} extra oak wood!".format(time, 1 + db[f"razor_edge{ctx.message.author}"] + amount_gained + db[f"chopping_level{ctx.message.author}"]))
          elif db[f"axe{ctx.message.author}"] == 2:
            await ctx.send("In {0} seconds you will have {1} extra oak wood!".format(time, 3 + db[f"razor_edge{ctx.message.author}"] + amount_gained + db[f"chopping_level{ctx.message.author}"]))
          await asyncio.sleep(90.0*db[f"effciency{ctx.message.author}"])
          await get_wood()

  elif db[f"Forest_card{ctx.message.author}"] <= 0:
      await ctx.send("You have not unlocked this yet. Hint: buy a Forest pass in the shop")
  elif db[f"axe{ctx.message.author}"] < 1:
      await ctx.send("You need to have an axe in order to chop trees")
  else:
      await ctx.send("error")

#autominer

@bot.command(name="automine")
async def automine(ctx: commands.Context):

  if db[f"autominer{ctx.message.author}"] >= 1:
    await ctx.send("You will now gain 10 materials every 4 minutes")
    async def automine_():
      amount = 10
      i = 0
      for i in range(amount):
        i += 1
        chance = [i for i in range(100)]
        material = random.choice(chance)
        if material <= 60:
          db[f"dirt{ctx.message.author}"] += 1
        elif 60 < material <= 90:
          db[f"stone{ctx.message.author}"] += 1
        elif material > 90:
          db[f"iron{ctx.message.author}"] += 1
          
      await asyncio.sleep(240.0)
      await automine_()
    
    await asyncio.sleep(240.0)
    await automine_()
  else:
    await ctx.send("You need to have an auto miner to do this!")


@bot.command(name="daily")
async def daily(ctx):
  global wait_for_daily
  
  async def daily_cooldown():
    db[f"dirt{ctx.message.author}"] += 250
    db[f"stone{ctx.message.author}"] += 125
    db[f"iron{ctx.message.author}"] += 62
    db[f"wood{ctx.message.author}"] += 50
    amount_bars = random.randint(10, 15)
    db[f"iron_bar{ctx.message.author}"] += amount_bars
    await ctx.send("+250 dirt \n +125 stone \n +62 iron \n +50 wood \n +{0} iron bars \n".format(amount_bars))
    await ctx.send("You can use this command again in 24 hours!")
    db[f"wait_for_daily{ctx.message.author}"] = True
    await asyncio.sleep(86400.0)
    db[f"wait_for_daily{ctx.message.author}"] == False
    

  if db[f"wait_for_daily{ctx.message.author}"] == True:
    await ctx.send("It has not been 24 hours yet!")
  else:
    await daily_cooldown()




def setup(bot):
  bot.add_command(mine)
  bot.add_command(sell)
  bot.add_command(sellall)
  bot.add_command(chop)
  bot.add_command(automine)
  bot.add_command(daily)
