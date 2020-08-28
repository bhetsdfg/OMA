import discord 
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("iu.json" , "r" , encoding= "utf8") as jfile:
    jdata = json.load(jfile)
with open("se6.json" , "r" , encoding= "utf8") as jfile:
    jdataS = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def iu(self , ctx):
        pic = random.choice(jdata["iu"])
        await ctx.send(pic)

    @commands.command()
    async def 色圖(self , ctx):
        pic = random.choice(jdataS["sx"])
        await ctx.send(pic)

def setup(bot):
    bot.add_cog(React(bot))