import asyncio
import datetime
import discord
from discord.ext import commands


class Moderator(commands.Cog):
    """Comandos Moderação"""

    def __init__(self, bot):
        self.bot = bot
        
    global now
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y | %H:%M") 


    @commands.slash_command(name="limpar", description="Limpa o chat")
    @commands.guild_only()
    async def clear(self, ctx):
        await ctx.channel.purge()
        embed=discord.Embed(title="🗑 | Chat Limpo!", color=0xff0000)
        embed.add_field(name="📥 | Limpado por:", value=f"{ctx.author.mention}", inline=True)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await ctx.respond(embed=embed, delete_after=3)
    

    @commands.slash_command(name="banir", description=" Bane um player")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, pessoa: discord.Member, *, motivo = None):
        if motivo == None:
            motivo = "Sem motivo"
        await pessoa.ban(reason=motivo)
        embed=discord.Embed(title="❌ | BANIDO!", color=0xff0000)
        embed.add_field(name="👤 | STAFF:", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="🤕 | BANIDO:", value=f"{pessoa}", inline=False)
        embed.add_field(name="📜 | MOTIVO:", value=f"`{motivo}`", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await ctx.respond(embed=embed)


    @commands.slash_command(name="kickar", description=" Kicka um player")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, pessoa: discord.Member, *, motivo = None):
        if motivo == None:
            motivo = "Sem motivo"
        await pessoa.kick(reason=motivo)
        embed=discord.Embed(title="❌ | Expulso!", color=0xff0000)
        embed.add_field(name="👤 | STAFF:", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="🤕 | EXPULSO:", value=f"{pessoa}", inline=False)
        embed.add_field(name="📜 | MOTIVO:", value=f"`{motivo}`", inline=False)
        embed.set_footer(text=f"Todos os direitos reservados à: ...")
        await ctx.respond(embed=embed)
    
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        sites = ["https://www", "http://www", "https://", "http://", "youtube.com", "google.com", "github.com", "linkedin.com", ".net"]
        for site in sites:
            if site in ctx.content:
                await ctx.delete()
                await ctx.channel.send(f"{ctx.author.mention}, por favor, não envie links")
                with open("links.txt", "a", encoding='utf-8') as abrindo_links:
                    abrindo_links.writelines(f"Link: {ctx.content} │ Usuário: {ctx.author.name}{'#'}{ctx.author.discriminator}\n")
                print(f"Quem enviou link: {ctx.author} │ Link: {ctx.content} │ Dia e Hora: {now}")


def setup(bot):
    bot.add_cog(Moderator(bot))
    print("Moderação | Carregado!")