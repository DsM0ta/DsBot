from typing import List, Mapping
from discord.ext import commands
from discord import app_commands
import discord
import random
import os
import json
import asyncio
perms = discord.Intents.default()
perms.message_content = True
perms.members = True
bot = commands.Bot(command_prefix = ";", intents=perms, help_command=None)

#importando cogs
async def carregar_cogs():
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            try:
                await bot.load_extension(f"cogs.{arquivo[:-3]}")
            except Exception as e:
                print(f"Erro ao carregar {arquivo}: {e}")


@bot.event
async def on_ready():
    await carregar_cogs()
    print("Tudo pronto.")


    
@bot.command()
async def sinc(ctx:commands.Context):
    if ctx.author.id == 273182673021829120:
        sincs = await bot.tree.sync()
        await ctx.reply(f"{len(sincs)} comando(s) sincronizados")
    else:
        await ctx.reply('O que está tentando fazer? apenas o Ds pode usar este comando!')

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
    

#---------txt avisos------------
#Ler txt com o id do chat
def ler_cAviso():
    try:
        with open('chat_aviso.txt', 'r') as file:
            return int(file.read())
            #return [int(line.strip()) for line in file]
    except FileNotFoundError:
        return
    
#Salvar id do chat
def salvar_cAviso(chat):
    with open('chat_aviso.txt', 'w') as file:
        file.write(str(chat))
    

#----------txt chat censuraverso---------
# #Ler txt do chat
# def ler_censuraverso():
#     try:
#         with open('censuraverso.txt', 'r') as file:
#             return int(file.read())
#     except FileNotFoundError:
#         return
    
# #Salvar id do chat
# def salvar_censuraverso(chat):
#     with open('censuraverso.txt','w') as file:
#         file.write(str(chat))
        

#função com as respostas aleátórias
def respostas():
    mensagens = ['Ta.',
                 'Interessante',
                'Se quiser sim mano', 
                 'Talvez mas...', 
                 'Pior que é',
                 'Viajou mano',
                 'Talvez',
                 'Acho que sim',
                 'Se tu diz...',
                 'Negativo',
                 'Verdade',
                 'Não, nd ver isso daí',
                 'É oq mano?',
                 'Papo reto',
                 'Nah id win',
                 'NUH UH!',
                 ':)',
                 'Talvez exista a possibilidade de quem sabe possivelmente se Deus quiser provavelmente aconteça que por acaso possa ser que seja verdade...']
    # variável peso dando a probabilidade de cada uma das frases do vetor
    pesos = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,2,0.5,1]
    # variavel  é uma escolha aleatória tendo em mente as mensagens e o peso de cada
    # k=1 define que queremos apenas um elemento aleatório, e [0] nos dá esse único elemento
    mensagem_escolhida = random.choices(mensagens, weights=pesos, k=1)[0]
    return mensagem_escolhida


# variáveis
prox_n = ler_n()
# print(prox_n)
canal_av = ler_cAviso()
canal_cont = ler_c()
# salaSeg = ler_censuraverso()






#===============================================





@bot.tree.command(description='Dê boas vindas de volta ao DsBot :D')
async def welcomeback(interact:discord.Interaction):
    await interact.response.send_message(f'Obrigado, {interact.user.mention}')
    await interact.followup.send(f'É um prazer estar de volta :)')



# #-------- Sala de segurança 
# @bot.command()
# async def censuraversoC(ctx=commands.context, chat:discord.TextChannel = None):
#     if ctx.author.guild_permissions.manage_messages or ctx.message.author.id == 273182673021829120:
#         global censuraversoChat
#         if chat:
#             _censuraversoChat = discord.utils.get(ctx.guild.channels, id=chat.id)
#             if _censuraversoChat:
#                 censuraversoChat = _censuraversoChat.id
#                 salvar_censuraverso(censuraversoChat)
#                 await ctx.send(f"Chat escolhido como sala de segurança: {_censuraversoChat.mention}.")

#             else: 
#                 await ctx.send(f"Não foi possível encontrar o chat '{_censuraversoChat}'.")
#         else:
#             await ctx.reply("Comando incompleto! Tente: ```;censuraversoC <canal>```")
#     else:
#         await ctx.send("Pare agora mesmo! você não tem permissão para usar este comando!")

# @censuraversoC.error
# async def censuraversoC_error(ctx, error):
#     if isinstance(error, commands.BadArgument):
#         await ctx.send("Por favor, mencione um canal válido.")


# # ------ falar -------
# @bot.command()
# # Comando assíncrono definido como "falar", com o parâmetro de contexto (ctx)
# # "*, frase" quer dizer que após o comando ele espera uma frase aceitando espaços e várias palavras
# async def falar(ctx:commands.Context, *, frase = None):
#     # Se a frase não estiver vazia
#     if (frase != None):
#         usuario = ctx.author

#         #--Enviando mensagem para sala de segurança--
#         salaSeg_mention = f'<#{salaSeg}>'
#         salaSeg_enviar = bot.get_channel(salaSeg)
#         print (f'Comando ";falar" utilizado pelo {usuario.global_name}({usuario.mention}) e enviado para {salaSeg_enviar}({salaSeg_mention})')
#         # await salaSeg_enviar.send(f" {usuario.mention} me utilizou para falar: ` {ctx.message.content} `")
#         await salaSeg_enviar.send(f" {usuario.mention} me utilizou para falar: ` {frase} `")
#         #await salaSeg_enviar.send(ctx.author.avatar)

        
#         # Tendo o contexto, ele deleta a mensagem original da pessoa
#         await ctx.message.delete()
#         # censurar palavras ruins
#         censuraWords = ["nigga", "nigger", "mama minha", "mama a", "9/11", "11/9", "onlyfans", "chupa meu", "chupa minha", "p3d0", "ped0", "pedo", "pedofilia","pedofilo","pedofelo","rule34","r34","rule34.xxx","xvideos", "x videos", "pornhub", "x video", "xvideo", "dalva","porno", "porn"]
#         if any(word in frase.lower() for word in censuraWords):
#             await ctx.send(f'{usuario.mention}, me desculpe, tem algo nessa frase que sou proibido de dizer.')            
#         else:
#             if ctx.message.reference:
#                 referenced_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
#                 await referenced_message.reply(frase)
#             else:
#                 await ctx.send(frase)
#     else:
#         await ctx.reply("Preciso de algo para repetir. Tente: ```;falar <frase>```")


# @bot.tree.command(description='Peça para Dszin falar algo específico')
# async def falar(interact: discord.Interaction, frase: str):
#     await interact.response.defer()  # Oculta a interação para não mostrar que você usou o comando
#     await interact.channel.send(frase)  # Envia a mensagem para o canal
#     await interact.delete_original_response()  # Remove a resposta inicial do "carregando"
    
#     salaSeg_mention = f'<#{salaSeg}>'
#     salaSeg_enviar = bot.get_channel(salaSeg)
#     print (f'Comando ";falar" utilizado pelo {interact.user.global_name}({interact.user.mention}) e enviado para {salaSeg_enviar}({salaSeg_mention})')
#     await salaSeg_enviar.send(f" {interact.user.mention} me utilizou para falar: ` {frase} `")



# --- definir canal aviso ---
#Definir canal de aviso
@bot.command()
async def chataviso(ctx, canal_nome: discord.TextChannel = None):
    #Se o autor da mensagem tiver permissão de cargo de administrador
    if ctx.author.guild_permissions.administrator:
        if canal_nome:
            global canal_av
            # Cria variável que obtém o canal pelo nome
            canal = discord.utils.get(ctx.guild.channels, id=canal_nome.id)
            if canal:
                canal_av = canal.id
                salvar_cAviso(canal_av)
                await ctx.send(f"Canal escolhido para avisos: {canal.mention}")
            else:
                await ctx.send(f"Não foi possível encontrar o canal '{canal_nome}'.")
        else:
            await ctx.reply("Comando incompleto! Tente: ```;chataviso <canal>```")
    else:
        await ctx.send("Pare agora mesmo! você não tem permissão para usar este comando!")

@chataviso.error
async def censuraversoC_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Por favor, mencione um canal válido.")



# # --- Definir chat de CONTAR ---
# @bot.command()
# async def chatcontar(ctx, canal_nome: discord.TextChannel = None):
    
#     if ctx.author.guild_permissions.administrator or ctx.message.author.id == 273182673021829120:
#         if canal_nome:
#             global canal_cont
#             canal_c = discord.utils.get(ctx.guild.channels, id=canal_nome.id)
#             if canal_c:
#                 canal_cont = canal_c.id
#                 salvar_c(canal_cont)
#                 await ctx.send(f"Canal escolhido para contar: {canal_c.mention}.")
#             else:
#                 await ctx.send(f"Não foi possível encontrar o canal '{canal_nome}'.")
#         else:
#             await ctx.reply("Comando incompleto! Tente: ```;chatcontar <canal>```")
#     else:
#         await ctx.send("Pare agora mesmo! você não tem permissão para usar este comando!")

# @chatcontar.error
# async def censuraversoC_error(ctx, error):
#     if isinstance(error, commands.BadArgument):
#         await ctx.send("Por favor, mencione um chat válido.")


# #--- Resetar canal de contar
# @bot.command()
# async def naocontar(ctx):
#     if ctx.author.guild_permissions.administrator or ctx.message.author.id == 273182673021829120:
        
#         global canal_cont
#         canal_cont = 0
#         salvar_c(canal_cont)
#         #print(canal_cont)

#         await ctx.send("Chat de contar desfeito :(")
#     else:
#         await ctx.send("Pare agora mesmo! você não tem permissão para usar este comando!")

# #--- Redefinir número
# @bot.command()
# async def proxn(ctx, nextn = prox_n):
#     if ctx.author.guild_permissions.administrator or ctx.message.author.id == 273182673021829120:
#         global prox_n
#         await ctx.send(f"Próximo número definido para: {nextn}.")
#         prox_n = nextn
#         salvar_n(prox_n)



#----------------EVENTOS-----------------


#--- Avisar no canal_av ao criar e deletar um chat ---
@bot.event
async def on_guild_channel_create(channel):
        avisar = bot.get_channel(canal_av)
        if avisar:
            match channel.type:
                case discord.ChannelType.text:
                    await avisar.send(f"CUIDADO! O chat '{channel.mention}' foi criado!")
                case discord.ChannelType.voice:
                    await avisar.send(f"CUIDADO! O canal de voz '{channel.mention}' foi criado!")


#-- Aviso ao deletar um canal -- 
@bot.event
async def on_guild_channel_delete(channel):
    avisar = bot.get_channel(canal_av)
    if avisar:
        match channel.type:
            case discord.ChannelType.text:
                await avisar.send(f"Eita, o chat `{channel.name}` foi deletado!")
            case discord.ChannelType.voice:
                await avisar.send(f"Eita, canal de voz `{channel.name}` foi deletado!")
    else:
        return



#--- CONTAGENS ---
@bot.event
async def on_message(message):
    global canal_cont
    #print(f"canal_cont: {canal_cont}, message.channel.id: {message.channel.id}")  # Depuração
    if canal_cont != 0 and canal_cont == message.channel.id:
        global prox_n

        if message.content.isdigit() or message.author == bot:
            numero = int (message.content)
            if numero == prox_n:
                prox_n += 1
                salvar_n(prox_n)
                canal_cont = canal_cont
            else:
                await message.delete()
                await message.channel.send("# NÚMERO ERRADO")
                await message.channel.send(prox_n)
                canal_cont = canal_cont
        else:
            await message.delete()
            canal_cont = canal_cont
            return
        

    #---- CENSURAVERSO ----
    channel_id = 1236740302375485530

    if message.channel.id == channel_id:
        if "https://" in message.content:
            return
        if any(attachment.filename.lower().endswith('.gif') for attachment in message.attachments):
            return
    
        # Ignora mensagens com links de GIFs do Discord
        if 'cdn.discordapp.com' in message.content and message.content.lower().endswith('.gif'):
            return
        
        censuraNum = ["59","60","61","62","63","64" ,"65","66","67","68","69","70","71","72","73","74","75", "76","77","78","79","80","81","82","83","84","85","86","87","88","89","90", "quinhentos", "kinhentos", "quinhento", "quinentos", "quinento", "kinhento", "qinhentos", "seiscentos"]
        if any(char in message.content for char in censuraNum):
            await message.delete()
            print("Número enviado no slowmode:",message.content)

            # image_folder = r'D:\DISCO D\dsrm gamer jogos\Imagens\meme e emotes'
            # if os.path.exists(image_folder):
            #     images = [file for file in os.listdir(image_folder) if file.endswith('.png') or file.endswith('.jpg')]
            #     if images:
            #         random_image = random.choice(images)
            #         image_path = os.path.join(image_folder, random_image)
            #         await message.channel.send(file=discord.File(image_path))
            #     else:
            #         return


    #---- Resposta automática ----
    #Verifica se o bot foi mencionado
    if bot.user.mentioned_in(message):
        # Se marcar a mensagem do bot:
        if message.reference:
            referenced_message = await message.channel.fetch_message(message.reference.message_id)
            mensagem_escolhida=respostas()
            await message.reply(mensagem_escolhida)
            
        # Se for uma mensagem apenas mencionando o bot:
        elif len(message.content.split()) == 1:
            olas = ['Oi', 'Ola', 'Chamou?', 'Fala']
            pesos = [5,5,5,5]
            ola_escolhida = random.choices(olas, weights = pesos, k=1)[0]
            await message.reply(ola_escolhida)
            
        # Se não for uma mensagem apenas mencionando o bot:
        else:
            respostas()
            mensagem_escolhida=respostas()
            await message.reply(mensagem_escolhida)
            
        
    
    respostas_secret = {
        'cazum9': '🤫 🧏‍♂️',
        'dsbota': 'Esse não.',
        'oi dsmota': 'e eu?',
        'oi dsbot': 'ola :]'
    }
    #No 'for' cria a variavel 'palavra' e 'resposta' para separar os itens na variavel 'respostas'
    for palavra, resposta in respostas_secret.items():
        #Verifica se a mensagem tem uma das palavra-chave
        if palavra in message.content.lower():
            chance = random.random()
            if chance < 0.5:
                #emite a resposta, respondendo o usuário
                await message.reply(resposta)
                break

             
            
    
    await bot.process_commands(message)



async def main():
    await carregar_cogs()

# pegando chave no arquivo key.json
with open('key.json') as key_file:
    key = json.load(key_file)
token = key['token']

bot.run(token)