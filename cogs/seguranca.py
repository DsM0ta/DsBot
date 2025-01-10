import discord
from discord.ext import commands
from cogs.variaveis import salvar_censuraverso

class Seguranca(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.censuraversoChat = None  # Inicializa a variável globalmente

    @commands.command()
    async def censuraversoC(self, ctx: commands.Context, chat: discord.TextChannel = None):
        if ctx.author.guild_permissions.manage_messages or ctx.author.id == 273182673021829120:
            if chat:
                # Define o canal de segurança
                self.censuraversoChat = chat.id
                salvar_censuraverso(self.censuraversoChat)  # Salva o ID do canal
                await ctx.send(f"Chat escolhido como sala de segurança: {chat.mention}.")
            else:
                await ctx.reply("Comando incompleto! Tente: ```;censuraversoC <canal>```")
        else:
            await ctx.send("Pare agora mesmo! Você não tem permissão para usar este comando!")

    @censuraversoC.error
    async def censuraversoC_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Por favor, mencione um canal válido.")

# Método para carregar o cog
async def setup(bot):
    await bot.add_cog(Seguranca(bot))
