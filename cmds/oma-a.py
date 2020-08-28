import discord 
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("img.json" , "r" , encoding= "utf8") as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):

    @commands.command()
    async def ping(self , ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)")
    
    @commands.command()
    async def 嗨(self , ctx):
        await ctx.send("嗨！")

    @commands.command()
    async def 更多OMA(self , ctx):
        embed=discord.Embed(title="你好啊！我是OMA！", url="https://www.flaticon.com/free-icon/girl_2945303?term=girl&page=1&position=46", description="很高興認識你", color=0xf967f4)
        embed.set_author(name="🎇OMA🎇", url="", icon_url="https://imgur.com/JONksHW.png")
        embed.set_thumbnail(url="https://imgur.com/JONksHW.png")
        embed.add_field(name="生日", value="🎈2020/7🎈", inline=False)
        embed.add_field(name="來自", value="🎈台灣🎈", inline=False)
        embed.add_field(name="作者", value="🎈MANO🎈", inline=False)
        embed.set_footer(text="BY MANO")
        await ctx.send(embed=embed)

    @commands.command()
    async def 說(self , ctx ,*, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def 刪除(self , ctx , num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def 隨機組隊(self, ctx , a:int , b:int):
        online = []
        await ctx.send(f"組隊人數共{a}人" + f"   每個小隊有{b}人")
        r = int(a / b)
        await ctx.send(f"分成{r}個小隊") 
        for member in ctx.guild.members:
            if str(member.status) == "online":
                online.append(member.mention)

        random_online = random.sample(online, k = a)
        for sq in range(r):
            z = random.sample(random_online, k = b)
            await ctx.send(f"第{sq+1}小隊  " + str(z))
            for name in z:
                random_online.remove(name)

    @commands.command()
    async def 親一下(self , ctx ,msg):
        if msg == "OMA" or msg == "oma":
            oma = random.choice(jdata["oma"])
            await ctx.send("不行！不可以親我！😳")
            await ctx.send(oma)
        elif msg == "自己" or msg == ctx.author.mention:
            n = ctx.author.mention
            o = random.choice(jdata["myself"])
            await ctx.send(f"{n}\n 好可憐喔😕你好孤單🙁")
            await ctx.send(o)
        else:
            k = random.choice(jdata["kisses"])
            await ctx.send(f"你好色喔 居然親了{msg}")
            await ctx.send(k)
        


        

def setup(bot):
    bot.add_cog(Main(bot))