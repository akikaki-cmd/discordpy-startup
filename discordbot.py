from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!s')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('Bot is sleep.....')
   
client.run('NzM5ODA2NDcyMjU0MjU5Mjky.Xyf0dw.fDxx_Pyjj-NhOycCyl4LNil8T-c')
    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

 @bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
    
 @bot.command()
async def botver(ctx):
    await ctx.send('suyaxabot v1.1 beta')
    
  @bot.command()
async def a(ctx):
    await ctx.send('a')

bot.run(token)
