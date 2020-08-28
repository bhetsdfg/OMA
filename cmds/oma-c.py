import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json 
import random
import os

with open("setting.json" , "r" , encoding= "utf8") as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self , member):
        channel = self.bot.get_channel(jdata["channel"])
        await channel.send(f"歡迎 {member} 的加入 !🎉")

    @commands.Cog.listener()
    async def on_member_remove(self , member):
        channel = self.bot.get_channel(jdata["channel"])
        await channel.send(f"什麼？！ {member} 居然走了 !😕")

    @commands.Cog.listener()
    async def  on_message(self , msg):
        if msg.content in jdata["msg_key"] and msg.author != self.bot.user:
            await msg.channel.send("(✿◠‿◠) 我也愛你 😘")


def setup(bot):
    bot.add_cog(Event(bot))