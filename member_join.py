import asyncio
import discord
from discord import channel
from discord.ext import commands
import random
from main import bot

class member_joining(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = bot.get_channel(912380810995335271)
        embed=discord.Embed(title=":white_check_mark: │ Um novo membro entrou!", color=0xff0000)
        embed.add_field(name=f"Temos um novo membro em nossa comunidade: ", value=f"{member.mention}", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = bot.get_channel(912380810995335271)
        embed=discord.Embed(title=":x: │ Um membro saiu ;(", color=0xff0000)
        embed.add_field(name=f"Um membro saiu de nossa comunidade: ", value=f"{member.mention}", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await channel.send(embed=embed)
def setup(bot):
    bot.add_cog(member_joining(bot))
    print("Member | Carregado!")