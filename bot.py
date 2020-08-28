import discord
from discord.ext import commands
import json 
import random
import os

with open("setting.json" , "r" , encoding= "utf8") as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = "/")
bot.remove_command("help")
@bot.event
async def on_ready():
    print("⩥  OMA 上線了!! ⩤")
    

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="HELP", description="OMA的指令", color=0xfbd446)
    embed.set_thumbnail(url="https://i.imgur.com/JONksHW.png")
    embed.add_field(name="/ping ", value="檢查網路延遲 ", inline=False)
    embed.add_field(name="/嗨 ", value="嗨 你好 ", inline=False)
    embed.add_field(name="/說 ", value="讓OMA幫你說 ( /說 訊息 ) ", inline=False)
    embed.add_field(name="/刪除 ", value="刪除訊息 ( /刪除 數量 ) ", inline=False)
    embed.add_field(name="/色圖 ", value="無論何人何時何地 都需要色圖 ", inline=False)
    embed.add_field(name="/iu ", value="MANO私心放一下 我的BOT我做主!", inline=False)
    embed.add_field(name="/親親 ", value="不能亂親別人喔 ( /親親 XX ) ", inline=False)
    embed.add_field(name="/現在時間 ", value="嘿 OMA！現在幾點？ ", inline=False)
    embed.add_field(name="/更多OMA ", value="誰不喜歡更多OMA？讓OMA介紹自己!", inline=False)
    embed.add_field(name="/隨機組隊 ", value="需要分隊嗎?OMA幫你 ( /隨機組隊 組隊總人數 每組人數 )", inline=False)
    embed.set_footer(text="by MANO")
    await ctx.send(embed=embed)


@bot.command()
async def 載入(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"載入 {extension} 完成！")

@bot.command()
async def 卸載(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"卸載 {extension} 完成！")

@bot.command()
async def 重載(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"重載 {extension} 完成")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata["token"])