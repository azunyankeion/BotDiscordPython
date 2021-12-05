from asyncio import tasks
from os import error
import random
from discord import Activity, ActivityType, activity
from discord.enums import Status
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument, MissingPermissions
from discord.ext import commands, tasks
from itertools import cycle
import discord
import asyncio
import datetime
import time
import requests
from main import bot
from PIL import Image, ImageDraw, ImageFont

class Manager(commands.Cog):
    """Gerencia o bot"""

    def __init__(self, bot):
        self.bot = bot


    global now
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y | %H:%M") 

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Utilize / ao invés de !, {ctx.author.mention}")
        if isinstance(error, MissingRequiredArgument):
            await ctx.channel.send(f"Você não informou o argumento requerido, {ctx.author.mention}")
        if isinstance(error, MissingPermissions):
            await ctx.channel.send(f"Faltam permissões para o bot, {ctx.author.mention}")

        palavroes = ["cu", "piru", "pênis", "pau", "vadia", "vagina", "buceta", "bucetinha", "xereca", "arrombado", "fudeu", "fodeu", "fodido", "fodida", "puta", "pica", "rola", "rolona", "picona", "gay", "viado", "guei", "caralho", "puta que pariu", "porra", "filho da puta", "corno", "retardado", "doente", "duente", "chupa"]
            
        for palavrao in palavroes:
            if palavrao.lower() == ctx.content:
                await ctx.delete()  
                print(f"Mensagem: {ctx.content} │ Usuário: {ctx.author}")
                with open("mensagens_excluidas.txt", "a", encoding='utf-8') as message_excluded:
                    message_excluded.writelines(f"Mensagem: {ctx.content} │ Usuário: {ctx.author} │ Hora: {now}\n")
            elif palavrao.upper() in ctx.content:
                await ctx.delete()  
                print(f"Mensagem: {ctx.content} │ Usuário: {ctx.author}")
                with open("mensagens_excluidas.txt", "a", encoding='utf-8') as message_excluded:
                    message_excluded.writelines(f"Mensagem: {ctx.content} │ Usuário: {ctx.author} │ Hora: {now}\n")


        await self.bot.process_commands(ctx)

    @commands.slash_command(name="hora", description="Dia e hora no horário de Brasília")
    @commands.guild_only()
    async def hora(self, ctx):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M")
        embed=discord.Embed(title=":clock: | Veja detalhes do dia!", color=0xff0000)
        embed.add_field(name=":sun_with_face: | DIA", value=f"{now}", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await ctx.respond(embed=embed)

    @commands.slash_command(name="info", description="Informações do bot")
    @commands.guild_only()
    async def info(self, ctx):
        embed=discord.Embed(title=":computer: | Informações do BOT", color=0xff0000)
        embed.add_field(name=":bust_in_silhouette: | Criadores", value=f"𝒁SŦȺɌŦ叛#7359 │ Roycy#6768", inline=False)
        embed.add_field(name=":computer: | Iniciado", value=f"Fui começado a ser programado em 28/11", inline=False)
        embed.add_field(name=":white_check_mark: | STATUS", value=f"ONLINE", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await ctx.respond(embed=embed)
    

    @commands.slash_command(name="ping", description="Ping do BOT")
    @commands.guild_only()
    async def ping(self, ctx):
        latencia = bot.latency
        embed=discord.Embed(title="PONG :ping_pong: ", color=0xff0000)
        embed.add_field(name=f"Meu Ping é:", value=f"{latencia}", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await ctx.respond(embed=embed)


    @commands.slash_command(name="bolsonaro", description="Adicione textos na imagem do Bolsonaro")
    @commands.guild_only()
    async def bolsonaro(self, ctx, text: str):
        img = Image.open('bolsomito.jpg')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("SansSerif.ttf", 130)
        draw.text((280, 280), text, (255,255,255), font=font)
        arquivo = f"file{time.time()}.jpg"
        salvando = img.save(arquivo)
        await ctx.respond(file=discord.File(arquivo))


    @commands.slash_command(name="nickset", description="Sete o nick de alguém!", pass_context=True)
    @commands.guild_only()
    async def changenick(self, ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        embed=discord.Embed(title="NICKSET", color=0xff0000)
        embed.add_field(name=f"Novo Nick:", value=f"{member.display_name}", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await ctx.respond(embed=embed)

    @commands.slash_command(name="tapa", description="Dê um tapa em alguém", pass_context=True)
    @commands.guild_only()
    async def tapa(self, ctx, member: discord.Member):
        req = requests.get("https://nekos.life/api/v2/img/slap")
        data = req.json()
        embed=discord.Embed(title="TAPAS E MAIS TAPAS", color=0xff0000)
        embed.add_field(name="CARAMBA!", value=f"{ctx.author.mention} deu um bofetada em {member.display_name}", inline=False)
        embed.set_image(url=data["url"])
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await ctx.respond(embed=embed)
    

    @commands.slash_command(name="beijar", description="Beije Alguém!", pass_context=True)
    @commands.guild_only()
    async def beijo(self, ctx, member: discord.Member):
        req = requests.get("https://nekos.life/api/v2/img/kiss")
        data = req.json()
        embed=discord.Embed(title="BEIJOQUEROS AQUI", color=0xff0000)
        embed.add_field(name="CARAMBA!", value=f"{ctx.author.mention} Beijou {member.mention}", inline=False)
        embed.set_image(url=data["url"])
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await ctx.respond(embed=embed)

    
    @commands.slash_command(name="sortear", description="O Sorteio está no ar no mundo discorddd de prêmios!")
    @commands.guild_only()
    async def giveaway(self, ctx, tempo, *, premio):   

        def convert(tempo):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

            unit = tempo[-1]

            if unit not in pos:
                return -1
            try:
                val = int(tempo[:-1])
            except:
                return -2

            return val * time_dict[unit]

        converted_time = convert(tempo)

        if converted_time == -1:
            embed=discord.Embed(title="💁‍♂️ | Erro!", description=f"{ctx.author}, Acredito que tenha cometido um crime interminável", color=0xfa0000)
            embed.add_field(name="Erro:", value="Você tem que digitar o argumento corretamente!", inline=True)
            embed.add_field(name="Explicação:", value="s = Segundos | m = Minutos | h = Horas | d = Dias", inline=False)
            embed.add_field(name="Exemplo:", value="`/sortear 60m Notebook`", inline=False)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=f"Todos os direitos reservados à: ...")
            await ctx.respond(embed=embed, delete_after=15)

        if converted_time == -2:
            embed=discord.Embed(title="💁‍♂️ | Erro!", description=f"{ctx.author}, Acredito que tenha cometido um crime interminável", color=0xfa0000)
            embed.add_field(name="Erro:", value="Você tem que digitar o argumento corretamente!", inline=True)
            embed.add_field(name="Explicação:", value="s = Segundos | m = Minutos | h = Horas | d = Dias", inline=False)
            embed.add_field(name="Exemplo:", value="`/sortear 60m Notebook`", inline=False)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=f"Todos os direitos reservados à: ...")
            await ctx.respond(embed=embed, delete_after=15)


        embed=discord.Embed(title="O SORTEIO ESTÁ NO AR, NO MUNDO DISCORDDD DE PRÊMIOS!", description="Sorteio rolando!!", color=0xfa0000)
        embed.add_field(name=f"{ctx.author}, estou carregando...", value=f"TENHA PACIÊNCIA, PELO AMOR!")
        await ctx.respond(embed=embed)
        await asyncio.sleep(5)
        await ctx.delete()

        embedgive=discord.Embed(title="O Sorteio está no ar, no mundo discorddd de prêmios!!", description="Basta reagir, para participar!", color=0xff0000)
        embedgive.add_field(name="Quem Sorteou:", value=f"{ctx.author.mention}", inline=False)
        embedgive.add_field(name="Premiação:", value=f"{premio}", inline=False)
        embedgive.add_field(name="Termina em:", value=f"{tempo}", inline=True)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=f"Todos os direitos reservados à: ...")

        msg = await ctx.send(embed=embedgive)
        await msg.add_reaction("🎉")
        await asyncio.sleep(converted_time)
        msg = await msg.channel.fetch_message(msg.id)
        winner = None
        
        for reaction in msg.reactions:
            if reaction.emoji == "🎉":
                users = await reaction.users().flatten()
                users.remove(self.bot.user)
                winner = random.choice(users)

        if winner is not None:
            embed=discord.Embed(title="🎉 | Acabou!", color=0xff0000)
            embed.add_field(name="Quem sorteou:", value=f"{ctx.author.mention}", inline=False)
            embed.add_field(name="Premiação:", value=f"{premio}", inline=False)
            embed.add_field(name="Quem Ganhou:", value=f"{winner.mention}", inline=True)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=f"Todos os direitos reservados à: ...")
            await msg.edit(embed=embed)


    @commands.slash_command(name="shippar", description="Shippa uma pessoa com outra!")
    @commands.guild_only()
    async def shipp(self, ctx, membro: discord.Member, membro2: discord.Member):
        req = requests.get("https://nekos.life/api/v2/img/kiss")
        data = req.json()
        choices = ["Sem chance de dar certo", "Se quiserem...", "Talvez um dia!", "que casal lindo", "Não vejo defeito", "Juntos até a morte"],
        for item in choices:
            aleatoria = random.choice(item)
            embed=discord.Embed(title="Os shippados foram: ", description=f"{membro.mention} foi shippado com {membro2.mention}", color=0xff0000)
            embed.add_field(name="Resultado: ", value=f"{aleatoria}", inline=False)
            embed.set_image(url=data["url"])
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=f"Todos os direitos reservados à: ...")
            await ctx.respond(embed=embed)



def setup(bot):
    bot.add_cog(Manager(bot))
    print("=============COGS================")
    print("Manager | Carregado!")