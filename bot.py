import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

RESPOSTAS = {
    "!lori": "Oi! Deseja alguma coisa? Estou aqui pra ajudar!",
    "!dennie": "To online! O Dennie ta aqui pra ajudar!",
    "!ping": "Pong! To online!",
    "!online": "To online e pronta pra ajudar!",
    "!regras": "Aqui a gente preza pelo RESPEITO - sem xingamentos, sem brigas!",
    "!oi": "Oi oi! Bem-vindo(a)!",
    "!ola": "Ola! Tudo bem com voce?",
    "!boa": "Boa! Bora jogar?",
    "!ajuda": "Digita !comandos pra ver tudo que eu sei!",
    "!comandos": "Tenho 100 comandos! Tenta: !lori, !dennie, !ping, !regras, !loja, !cargo",
    "!loja": "A loja ainda ta fechada, fica de olho no #anuncios!",
    "!cargo": "Pra pegar cargo vai em #cargos!",
    "!cargos": "Vai em #cargos e pega o seu!",
    "!discord": "Chama a galera pra ca, quanto mais gente melhor!",
    "!server": "Esse server e o melhor! Xx00kidd na veia!",
    "!dono": "O dono do server e o brabo!",
    "!staff": "Precisa de ajuda? Chama a staff!",
    "!welcome": "Seja bem-vindo(a)! Leia as regras e se apresente!",
    "!jogar": "Bora jogar! Chama todo mundo no #geral!",
    "!tchau": "Tchau tchau! Volta logo!",
    "!teste": "Testando... FUNCIONANDO 100%!",
    "!bot": "Eu sou a Lori, a bot desse server!",
    "!versao": "Versao 2.0 - Lori com 100 comandos!",
    "!pix": "Quer ajudar o server? Fala com o dono!",
    "!evento": "Fica de olho em #anuncios, sempre tem evento novo!",
    "!sorteio": "Sorteio rolando? Corre pra #sorteios!",
    "!meme": "Manda um meme brabo no #memes!",
    "!musica": "Que musica voce quer ouvir?",
    "!filme": "Bora maratonar um filme hoje?",
    "!sorte": "Sua sorte hoje: VOCE VAI GANHAR MUITO!",
    "!amor": "O server te ama!",
    "!boa-noite": "Boa noite! Dorme bem!",
    "!bom-dia": "Bom dia! Bora pra mais um dia brabo!",
    "!boa-tarde": "Boa tarde! Bora jogar?",
    "!roblox": "Bora jogar Roblox!",
    "!freefire": "Bora um Free Fire?",
    "!mine": "Bora minerar no Minecraft?",
    "!fortnite": "Bora um Fortnite?",
    "!valorant": "Bora um Valorant?",
    "!lol": "Bora um LoL?",
    "!gta": "Bora um GTA?",
    "!brawl": "Bora um Brawl Stars?",
    "!stumble": "Bora um Stumble Guys?",
    "!among": "Bora um Among Us?",
    "!fifa": "Bora um FIFA?",
    "!pubg": "Bora um PUBG?",
    "!cod": "Bora um COD?",
    "!namoro": "Namoro? Aqui e server de amizade!",
    "!amigo": "Quer ser meu amigo? Bora!",
    "!amiga": "Quer ser minha amiga? Bora!",
    "!solteiro": "Solteiro sim, e o server e todo nosso!",
    "!casal": "Que fofos!",
    "!crush": "Conta pra gente quem e seu crush!",
    "!segredo": "Me conta seu segredo que eu guardo!",
    "!fofo": "Voce que e fofo(a)!",
    "!lindo": "Voce que e lindo(a)!",
    "!linda": "Voce que e linda!",
    "!brabo": "Voce que e brabo!",
    "!top": "Voce e top demais!",
    "!rei": "O rei do server chegou!",
    "!rainha": "A rainha do server chegou!",
    "!pro": "Voce e pro demais!",
    "!noob": "Todo mundo ja foi noob um dia!",
    "!hacker": "Sem hack aqui hein!",
    "!ban": "Sem banir ninguem, vamos resolver na paz!",
    "!mute": "Mutado por falar demais! Brincadeira!",
    "!kick": "Sem kick, bora conversar!",
    "!warn": "Warn dado com carinho!",
    "!denuncia": "Manda a denuncia pra staff no privado!",
    "!report": "Reporta pra staff que eles resolvem!",
    "!parceria": "Quer parceria? Fala com o dono!",
    "!divulgar": "Sem divulgar sem permissao, hein!",
    "!youtube": "Se inscreve no canal do dono!",
    "!tiktok": "Segue a gente no TikTok!",
    "!insta": "Segue a gente no Insta!",
    "!twitch": "Segue a gente na Twitch!",
    "!live": "Vai ter live hoje? Fica de olho!",
    "!horario": "O server ta aberto 24h!",
    "!clima": "Hoje ta clima de jogar muito!",
    "!fome": "Bora pedir um lanche?",
    "!sede": "Bebe uma agua!",
    "!sono": "Vai dormir que amanha tem mais!",
    "!escola": "Ja fez a tarefa? Depois bora jogar!",
    "!trabalho": "Trabalhou muito hoje? Descansa aqui!",
    "!prova": "Boa sorte na prova! Voce consegue!",
    "!estudo": "Estuda um pouco e depois bora jogar!",
    "!dinheiro": "Dinheiro nao traz felicidade, mas traz Robux!",
    "!robux": "Quem quer Robux levanta a mao!",
    "!vbucks": "Quem quer V-Bucks levanta a mao!",
    "!skin": "Qual sua skin favorita?",
    "!emote": "Manda seu emote favorito!",
    "!danca": "Bora dancar!",
    "!canta": "Canta uma musica pra gente!",
    "!piada": "Por que o computador foi ao medico? Porque estava com virus!",
    "!piada2": "Qual e o cumulo do azar? Ser atropelado pelo carro do Google!",
    "!adivinha": "O que e o que e? Te amo e voce nem sabe!",
    "!pergunta": "Pode perguntar que eu respondo!",
    "!sim": "Sim! Com certeza!",
    "!nao": "Nao! De jeito nenhum!",
    "!talvez": "Talvez... 50/50!",
    "!verdade": "Verdade! Pode acreditar!",
    "!mentira": "Mentira! To brincando!",
    "!coracao": "Meu coracao e todo do server!",
}

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    texto = message.content.lower().strip()
    if texto in RESPOSTAS:
        await message.channel.send(RESPOSTAS[texto])
        # Reacao da Lori
        try:
            await message.add_reaction("💜")
        except:
            pass
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    canal = discord.utils.get(member.guild.channels, name="welcome")
    if canal:
        await canal.send(f"SEJA BEM-VINDO(A) {member.mention}! Leia as regras em #regras e se apresente!")

bot.run("TOKEN")