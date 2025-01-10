import discord
from discord.ext import commands
from cogs.variaveis import salvar_c, salvar_n


class ChatContar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- Definir chat de CONTAR ---
    @commands.command()
    async def chatcontar(self, ctx, canal_nome: discord.TextChannel = None):
        if ctx.author.guild_permissions.administrator or ctx.author.id == 273182673021829120:
            if canal_nome:
                salvar_c(canal_nome.id)  # Salva diretamente o ID do canal
                await ctx.send(f"Canal escolhido para contar: {canal_nome.mention}.")
            else:
                await ctx.reply("Comando incompleto! Tente: ```;chatcontar <canal>```")
        else:
            await ctx.send("Pare agora mesmo! Você não tem permissão para usar este comando!")

    @chatcontar.error
    async def chatcontar_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Por favor, mencione um chat válido.")
        else:
            await ctx.send(f"Ocorreu um erro: {error}")

    # --- Resetar canal de contar ---
    @commands.command()
    async def naocontar(self, ctx):
        if ctx.author.guild_permissions.administrator or ctx.author.id == 273182673021829120:
            salvar_c(0)  # Define o ID do canal como 0 (ou seja, nenhum canal)
            await ctx.send("Chat de contar desfeito :(")
        else:
            await ctx.send("Pare agora mesmo! Você não tem permissão para usar este comando!")

    # --- Redefinir número ---
    @commands.command()
    async def proxn(self, ctx, nextn: int = None):
        if ctx.author.guild_permissions.administrator or ctx.author.id == 273182673021829120:
            if nextn is not None:
                salvar_n(nextn)  # Salva o próximo número
                await ctx.send(f"Próximo número definido para: {nextn}.")
            else:
                await ctx.send("Por favor, forneça um número válido.")
        else:
            await ctx.send("Pare agora mesmo! Você não tem permissão para usar este comando!")


# Setup do cog
async def setup(bot):
    await bot.add_cog(ChatContar(bot))
