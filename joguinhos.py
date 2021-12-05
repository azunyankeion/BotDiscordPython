import asyncio
import discord
from discord.ext import commands
import random
from main import bot
class Jogos(commands.Cog):
    """Jogos"""

    def __init__(self, bot):
        self.bot = bot

    
    @commands.slash_command(name="jokenpo", description="O famoso pedra, papel ou tesoura")
    @commands.guild_only()
    async def jokenpo(self, ctx, escolha: str):
        list_bot = ["pedra", "papel", "tesoura"]
        escolha_bot = random.choice(list_bot)
        embed=discord.Embed(title="JO KEN PO", color=0xff0000)
        
        embed.add_field(name=f"Você escolheu:", value=f"{escolha}", inline=False)
        
        embed.add_field(name=f"Eu escolhi:", value=f"{escolha_bot}", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")

        if escolha == "papel".lower() and escolha_bot == "pedra".lower():
                embed.add_field(name="Resultado:", value="Você ganhou!", inline=False)

        elif escolha == "pedra".lower() and escolha_bot == "papel".lower():
                embed.add_field(name="Resultado:", value="Eu ganhei!", inline=False)

        elif escolha == "tesoura".lower() and escolha_bot == "pedra".lower():
                embed.add_field(name="Resultado:", value="Eu ganhei!", inline=False)

        elif escolha == "pedra".lower() and escolha_bot == "tesoura".lower():
                embed.add_field(name="Resultado:", value="Você ganhou!", inline=False)

        elif escolha == "papel".lower() and escolha_bot == "tesoura".lower():
                embed.add_field(name="Resultado:", value="Eu ganhei!", inline=False)

        elif escolha == "tesoura".lower() and escolha_bot == "papel".lower():
                embed.add_field(name="Resultado:", value="Você Ganhou!", inline=False)

        elif escolha_bot.lower() == escolha.lower():
            embed.add_field(name="Resultado:", value="Deu Empate", inline=False)
        
        else:
            embed.add_field(name="ERRO!", value="Por favor, escolha uma das três opções!", inline=False)

        await ctx.respond(embed=embed)


    @commands.slash_command(name="impar", description="Par ou Ímpar!")
    @commands.guild_only()
    async def par_impar(self, ctx, escolha: int, escolher_par: int):
        escolha_bot = random.randint(0, 11)
        embed=discord.Embed(title="PAR OU ÍMPAR", color=0xff0000)
        embed.add_field(name="Qual você quer? 1 para PAR, 2 para ÍMPAR", value=f"{escolher_par}", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        while True:
            if escolha > 10:
                await ctx.respond(f"Por favor, escolha de 0 a 10, {ctx.author.mention}")
                break
            
            if escolher_par >= 3:
                await ctx.respond(f"Escolha de 1 a 2, {ctx.author.mention}")
                break

            else:
                if escolha % 2 == 0:
                    embed.add_field(name="Meu Número é:", value=f"{escolha_bot}", inline=False)
                    embed.add_field(name="Resultado:", value="Eu Ganhei!", inline=False)
                    await ctx.respond(embed=embed)
                    break
                elif escolha % 2 == 1:
                    embed.add_field(name="Meu Número é:", value=f"{escolha_bot}", inline=False)
                    embed.add_field(name="Resultado:", value="Você Ganhou!", inline=False)
                    await ctx.respond(embed=embed)
                    break


    @commands.slash_command(name="chute_numero", description="Você tenta adivinhar que número estou pensando de 0 a 50!")
    @commands.guild_only()
    async def chutar_numero(self, ctx, numero: int):
        numero_pensativo = random.randint(0, 50)
        await ctx.respond("Pensando...")
        await asyncio.sleep(5)
        if numero == numero_pensativo:
            embed=discord.Embed(title="CHUTE O NÚMERO", color=0xff0000)
            embed.add_field(name="Resultado:", value="Você Ganhou!", inline=False)
            embed.set_footer(text=f"Todos os direitos reservados à: ...")
            await ctx.respond(embed=embed)
        elif numero != numero_pensativo:
            embed=discord.Embed(title="CHUTE O NÚMERO", color=0xff0000)
            embed.add_field(name="Resultado:", value=f"Você Perdeu! O Número era: {numero_pensativo}", inline=False)
            embed.set_footer(text=f"Todos os direitos reservados à: ...")
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Jogos(bot))
    print("Jogos | Carregado!")
