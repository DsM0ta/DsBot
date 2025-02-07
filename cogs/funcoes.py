import random
import os
from discord.ext import commands

class Respostas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @staticmethod
    def respostas():
        mensagens = [
            'Ta.','É muito é massa','É','Sim','Não', 'Interessante', 'Se quiser sim mano', 
            'Talvez mas...', 'Pior que é', 'Viajou mano', 
            'Talvez', 'Acho que sim', 'Se tu diz...', 
            'Negativo', 'Verdade', 'Não, nd ver isso daí', 
            'É oq mano?', 'Papo reto', 'Nah id win', 
            'NUH UH!', ':)', 
            'Talvez exista a possibilidade de quem sabe possivelmente se Deus quiser provavelmente aconteça que por acaso possa ser que seja verdade...'
        ]
        pesos = [5,5,5,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 0.5, 1]
        mensagem_escolhida = random.choices(mensagens, weights=pesos, k=1)[0]
        return mensagem_escolhida
    

async def setup(bot):
    await bot.add_cog(Respostas(bot))
