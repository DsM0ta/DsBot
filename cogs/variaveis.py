import discord
from discord.ext import commands


class Variaveis(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        super().__init__()


#Ler txt do chat
def ler_censuraverso():
    try:
        with open('censuraverso.txt', 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return
        
#Salvar id do chat
def salvar_censuraverso(chat):
    with open('censuraverso.txt','w') as file:
        file.write(str(chat))

salaSeg = ler_censuraverso()

#---------txt chat contar------------
#Ler txt com o id do chat
def ler_c():
    try:
        with open('chat_c.txt', 'r') as file:
            return int(file.read())
            #return [int(line.strip()) for line in file]
    except FileNotFoundError:
        return
    
#Salvar id do chat
def salvar_c(chat):
    with open('chat_c.txt', 'w') as file:
        file.write(str(chat))
    

#----------txt números------------
#Ler txt com número do contador
def ler_n():
    try:
        with open('contador.txt', 'r') as file:
            return int (file.read())
    except FileNotFoundError:
        return 1

#Salvar número no txt do contador
def salvar_n(numero):
    with open ('contador.txt','w') as file:
        file.write(str(numero))


prox_n = ler_n()
print(prox_n)
canal_cont = ler_c()



async def setup(bot):
    await bot.add_cog(Variaveis(bot))