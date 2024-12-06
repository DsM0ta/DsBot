import discord
from discord import app_commands
from discord.ext import commands
from cogs.funcoes import Respostas

class DsOpinioes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def dsopinioes(self, ctx: commands.Context):
        mensagem_escolhida = Respostas.respostas()  # Chama o método estático
        if ctx.message.reference:
            referenced_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            await referenced_message.reply(mensagem_escolhida)
            await ctx.message.delete()
        else:
            await ctx.send(mensagem_escolhida)
            await ctx.message.delete()


    @app_commands.command(description="Peça a opinião de Dszin sobre algo.")
    async def dsopinioes(self, interact: discord.Interaction, message_id: str = None):
        mensagem_escolhida = Respostas.respostas()  # Chama o método estático
        if message_id:
            try:
                ref_message = await interact.channel.fetch_message(int(message_id))
                if ref_message.author.id != self.bot.user.id:
                    await ref_message.reply(mensagem_escolhida)
                else:
                    await interact.response.send_message("Oxi, eu não vou responder a mim mesmo", ephemeral=True)
                await interact.response.send_message("Não tenho permissão para responder a essa mensagem.", ephemeral=True)
            except Exception as e:
                await interact.response.send_message(f"Ocorreu um erro: {e}", ephemeral=True)
        else:
            await interact.response.send_message(mensagem_escolhida)

async def setup(bot):
    await bot.add_cog(DsOpinioes(bot))
