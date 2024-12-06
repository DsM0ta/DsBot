import discord
from discord import app_commands
from discord.ext import commands
import random

class Ola(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    #comando assíncrono definido como "ola". ctx definido como contexto. self definido como bot (pro cogs)
    async def oi(self, ctx):
        usuario = ctx.author
        olas = ['Oi, ',
                'Ola, ']
        pesos = [5,5]
        mensagem_escolhida = random.choices(olas, weights = pesos, k=1)[0]
        if (usuario.display_name == usuario.global_name):
            await ctx.reply(f"{mensagem_escolhida + usuario.display_name}")
        else:
            await ctx.reply(f"{mensagem_escolhida + usuario.display_name}/{usuario.global_name}")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("pong")

    #slash command
    @app_commands.command(description='Responde o usuario com um ola')
    async def ola(self, interact:discord.Interaction):
        olas=['Oi, ',
              'Ola, ']
        pesos=[5,5]
        mensagem_escolhida = random.choices(olas, weights = pesos, k=1)[0]
        
        if(interact.user.display_name == interact.user.global_name):
            await interact.response.send_message(f'Ola, {interact.user.mention}')
        else:
            await interact.response.send_message(f'{mensagem_escolhida + interact.user.display_name}/{interact.user.global_name}')


async def setup(bot):
    await bot.add_cog(Ola(bot))