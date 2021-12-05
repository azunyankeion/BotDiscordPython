# Importações
import discord
import os
import asyncio
import datetime
from discord.ext import commands
from config import settings


intents=intents=discord.Intents.all()
intents.members = True


bot = commands.Bot(intents=intents, command_prefix =commands.when_mentioned_or(settings['prefix']), help_command=None)

bot.remove_command('help')
bot.load_extension('manager')
bot.load_extension('joguinhos')
bot.load_extension('member_join')


global now
now = datetime.datetime.now()
now = now.strftime("%d/%m/%Y | %H:%M")  


@bot.event
async def on_ready():
    try:
        version = "BETA"               
        print("=============COGS================\n")
        print("       " + now)
        print("\n=================================")
        print(f"Meu nome é: {bot.user}")
        print(f"Versão: {version}")
        print("Ligado e sem erros!")
        print("=================================")
        while True:
            prefix = (settings['prefix'])
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Estou sendo programado ainda!"))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=f'📢 | /help'))
            await asyncio.sleep(10)
    except Exception as erro:
        print(f"Erro: {erro}")


# Pegar Cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(settings['token'])