import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = 'c!', intents = discord.Intents.all())
#make sure to enable all intents in the discord dev portal. I use all intents to make things simple.

@bot.command()
async def xp(ctx):
	authorid = ctx.message.author
	uname = bot.get_user(str(authorid).replace("<@", "").replace(">",""))
	try:
		with open("@" + str(authorid), encoding="utf-8") as f:
			xp = f.read()
			await ctx.reply(str(xp).replace("\n","") + " XP")
	except:
		await ctx.reply("0 XP")

@bot.command()
@commands.has_permissions(administrator = True)
async def setxp(ctx, userid, amt):
	try:
		uname = bot.get_user(userid)
		f = open("@" + str(uname), 'w', encoding="utf-8")
		f.write(amt)
		f.close()
		await ctx.reply("OK")
	except:
		await ctx.reply("Error")

@bot.command()
async def ping(ctx):
	await ctx.reply('Pong!')



intents = discord.Intents.default()
intents.message_content = True
bot.run('token')
