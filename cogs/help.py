import discord
from discord import app_commands
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def help(self, ctx):
        helpMessage = """
        Não sabe os comandos? relaxa, pelo o que eu me lembro tem esses daqui:
        Prefixo: ;

        **COMANDOS PÚBLICOS:**
        `help` - Mostra esta mensagem de ajuda
        `ola` - Dê um oi pro DsBot
        `dsopinioes` - DsBot da sua sincera opinião
        `falar <mensagem>` - Manda DsBot falar algo
        
        **COMANDOS PRO DS (e a administração):**
        `chataviso <chat>` - Define um chat para enviar avisos secretos ao público (não utilizar no pudimverso) :shushing_face: 
        `chatcontar <chat>` - Define um chat para ser o incrível chat de contagem
        `naocontar` - Desafaz o chat de contagem
        `proxn <numero>` - Define o próximo número da contagem
        `censuraversoC <chat>` - Define o chat para a sala de segurança :shushing_face: 
        """

        await ctx.send(helpMessage)

    @app_commands.command(description='Lista de comandos do bot')
    async def help_(self, interact:discord.Interaction):
        global helpMessage
        await interact.response.send_message(helpMessage)


async def setup(bot):
    await bot.add_cog(Help(bot))
