from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('しらんわpingなんて。ping114514ぐらいあるんじゃないw')

    
    
 @bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

    
    
 @bot.command()
async def botver(ctx):
    await ctx.send('( ˘ω˘ )bot v1.0')

    
bot.run(token)
