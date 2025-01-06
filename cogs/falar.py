import discord
from discord import app_commands
from discord.ext import commands
from cogs.funcoes import salaSeg


class Falar(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def falar(self, ctx: commands.Context, *, frase=None):
        """Comando para repetir a frase do usuário e enviar à sala de segurança."""
        if frase:
            usuario = ctx.author

            # Obter o canal de segurança
            
            salaSeg_enviar = self.bot.get_channel(salaSeg)
            salaSeg_mention = f'<#{salaSeg}>'

            if salaSeg_enviar:
                print(
                    f'Comando ";falar" utilizado por {usuario.global_name} ({usuario.mention}) e enviado para {salaSeg_mention}.'
                )
                await salaSeg_enviar.send(
                    f"{usuario.mention} me utilizou para falar: `{frase}`"
                )

            # Deletar a mensagem original
            await ctx.message.delete()

            # Palavras censuradas
            censuraWords = [
                "nigga", "nigger", "mama minha", "mama a", "9/11", "11/9", "onlyfans",
                "chupa meu", "chupa minha", "p3d0", "ped0", "pedo", "pedofilia", "pedofilo",
                "pedofelo", "rule34", "r34", "rule34.xxx", "xvideos", "x videos", "pornhub",
                "x video", "xvideo", "dalva", "porno", "porn"
            ]
            if any(word in frase.lower() for word in censuraWords):
                await ctx.send(
                    f'{usuario.mention}, me desculpe, tem algo nessa frase que sou proibido de dizer.'
                )
            else:
                if ctx.message.reference:
                    referenced_message = await ctx.channel.fetch_message(
                        ctx.message.reference.message_id
                    )
                    await referenced_message.reply(frase)
                else:
                    await ctx.send(frase)
        else:
            await ctx.reply("Preciso de algo para repetir. Tente: ```;falar <frase>```")

    @app_commands.command(description="Peça para o bot falar algo específico")
    async def falar_(self, interaction: discord.Interaction, frase: str):
        """Comando via Slash para o bot repetir algo."""
        await interaction.response.defer()  # Oculta a interação
        await interaction.channel.send(frase)  # Envia a mensagem para o canal
        await interaction.delete_original_response()  # Remove a resposta inicial

        from cogs.seguranca import salaSeg
        salaSeg_enviar = self.bot.get_channel(salaSeg)
        salaSeg_mention = f'<#{salaSeg}>'

        if salaSeg_enviar:
            print(
                f'Comando ";falar" utilizado por {interaction.user.global_name} ({interaction.user.mention}) e enviado para {salaSeg_mention}.'
            )
            await salaSeg_enviar.send(
                f"{interaction.user.mention} me utilizou para falar: `{frase}`"
            )


# Configuração para carregar o cog
async def setup(bot: commands.Bot):
    await bot.add_cog(Falar(bot))
