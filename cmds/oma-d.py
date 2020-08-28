import discord 
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio , datetime




class Task(Cog_Extension):
    @commands.command()
    async def 現在時間(self , ctx):
        await ctx.send(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"))
"""
    def __init__(self , *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.counter = 0

        async def time_task():
            await self.bot.wait_until_ready()
           

            while not self.bot.is_closed():
                nt = datetime.datetime.now().strftime("%m%d%H%M") 
                with open("setting.json" , "r" , encoding= "utf8") as jfile:
                    jdata = json.load(jfile)            
                self.channel = self.bot.get_channel(jdata["channel"])
                if nt == jdata["time"] and self.counter == 0:
                    await self.channel.send("時間到了喔喔喔")
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def 現在時間(self , ctx):
        await ctx.send(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"))

    @commands.command()
    async def 設定頻道(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        with open("setting.json" , "r" , encoding= "utf8") as jfile:
            jdata = json.load(jfile)
        jdata["channel"] = ch
        with open("setting.json" , "w" , encoding= "utf8") as jfile:
            json.dump(jdata , jfile , indent=4)
        await ctx.send(f"設定頻道在 {self.channel.mention}")
    
    @commands.command()
    async def 設定時間(self,ctx,time):
        self.counter = 0
        with open("setting.json" , "r" , encoding= "utf8") as jfile:
            jdata = json.load(jfile)
        jdata["time"] = time
        with open("setting.json" , "w" , encoding= "utf8") as jfile:
            json.dump(jdata , jfile , indent=4)
        await ctx.send(f"設定時間 {time}") and await ctx.send("時間到了再提醒你")
"""        



def setup(bot):
    bot.add_cog(Task(bot))