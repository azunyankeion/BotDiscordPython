import discord
import asyncio
import datetime
from os import error
from discord.ext import commands, tasks
from discord.ext.commands.errors import MissingPermissions, MissingRequiredArgument
from discord.ext.commands import has_permissions
from config import config

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["prefix"]))
tempo = datetime.date.today()


@bot.event
async def on_ready():
    print("==============MENU==============")
    print(f"Acabo de ser conectado em: {bot.user}")
    print(f"Prefix: {config['prefix']}")
    print("==============MENU==============")

    watching = "O que seu bot mostrará como se estivesse assistindo algo"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Assistindo {watching}"))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game(name=f"📢 | {config['prefix']}help"))
    await asyncio.sleep(10)


@bot.command()
async def hora(ctx):
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y | %H:%M")
    await ctx.channel.send("Data atual: " + now)


@bot.command(name="ban")
@commands.guild_only()
@has_permissions(ban_members=True)
async def banir(ctx, member: discord.Member, *, motivo = None):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("Faltam permissões para o bot!")
    if isinstance(error, MissingRequiredArgument):
        await ctx.channel.send("Faltam os argumentos do comando")

    if motivo == None:
        motivo = "Sem Motivo"
        member.ban(reason=motivo)
        await ctx.channel.send(f"O membro {member} foi banido por: {motivo}")
    else:
        member.ban(reason=motivo)
        await ctx.channel.send(f"O membro {member} foi banido por: {motivo}")


@bot.command(name="kick")
@commands.guild_only()
@has_permissions(kick_members=True)
async def kick_member(ctx, member: discord.Member, *, motivo = None):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("Faltam permissões para o bot!")
    if isinstance(error, MissingRequiredArgument):
        await ctx.channel.send("Faltam os argumentos do comando")

    if motivo == None:
        motivo = "Sem Motivo"
        member.kick(reaon=motivo)
        await ctx.channel.send(f"O membro {member} foi kickado por: {motivo}")
    else:
        member.kick(reason=motivo)
        await ctx.channel.send(f"O membro {member} foi kickado por: {motivo}")


@bot.event
async def on_message(ctx):
    palavroes = ["cu", "piru", "pênis", "pau", "vadia", "vagina", "buceta", "bucetinha", "xereca", "arrombado", "fudeu", "fodeu", "fodido", "fodida", "puta", "pica", "rola", "rolona", "picona", "gay", "viado", "guei", "caralho", "puta que pariu", "porra", "filho da puta", "corno", "retardado", "doente", "duente", "chupa"]
    if ctx.author == bot.user:
        return
    
    for palavrao in palavroes:
        if palavrao.lower() in ctx.content:
            await ctx.delete()
            print(f"Mensagem: {ctx.content} │ Usuário: {ctx.author}")

        elif palavrao.upper() in ctx.content:
            await ctx.delete()
            print(f"Mensagem: {ctx.content}, Usuário: {ctx.author}") 
        
        sites = ["https://", "http://", ".com", ".net", ".io", ".xyz", ".net", ".gov.br", ".ru"]
        for site in sites:
            site = site.lower()
            if site in ctx.content:
                await ctx.delete()
                print(f"Mensagem: {ctx.content} │ Usuário: {ctx.author}")


    await bot.process_commands(ctx)


@bot.command(name="info")
async def botinfo(ctx):
    criador = "𝒁SŦȺɌŦ叛#7359"
    embed = discord.Embed(title=":information_source: | Informações", color=0xff0000)
    embed.add_field(name="👤 | Criador:", value=f"{criador}", inline=False)
    embed.add_field(name="👤 │ Linguagem:", value=f"Python │ Biblioteca: PyCord")
    embed.add_field(name="👤 │ Intuito", value=f"Este bot foi criado, para que quem não sabe programar nada, consiga ter seu próprio bot!")
    await ctx.channel.send(embed=embed)


@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Menu | Ajuda", color=0xff0000)
    embed.add_field(name=":computer: | banir", value=f"Bane uma pessoa", inline=False)
    embed.add_field(name=":computer: | kickar", value=f"Kicka uma pessoa", inline=False)
    embed.add_field(name=":computer: | info", value=f"Informações do BOT", inline=False)
    embed.add_field(name=":computer: | hora", value=f"Mostra dia e hora", inline=False)
    await ctx.channel.send(embed=embed)



bot.run(config['token'])
