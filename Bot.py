import os
import threading
from flask import Flask
import discord
from discord.ext import commands

# Mini site pro Render nao achar que falhou
app = Flask(__name__)
@app.route('/')
def home():
    return "Lori online!"

def rodar_site():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=rodar_site, daemon=True).start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

RESPOSTAS = {
    "lori": "Oi! Deseja alguma coisa? 💜",
    "oi": "Oiii! 💜",
    "ola": "Olá! Tudo bem?",
    "bomdia": "Bom dia! 💜",
    "boanoite": "Boa noite! Dorme bem! 💜",
    "ping": "Pong! 🏓",
    "regras": "1. Respeito sempre! 2. Sem xingar! 3. Sem toxicidade! 💜",
    "ajuda": "Meus comandos: !lori, !oi, !ping, !regras, !ajuda",
    "dennie": "Estou online! 💜",
    "tchau": "Tchau! Volta logo! 💜",
}

@bot.event
async def on_ready():
    print(f"Lori logada como {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    texto = message.content.lower().strip()
    if texto.startswith("!"):
        chave = texto[1:].split()[0]
        if chave in RESPOSTAS:
            await message.channel.send(RESPOSTAS[chave])
            return
    await bot.process_commands(message)

@bot.command()
async def lori(ctx):
    await ctx.send("Oi! Deseja alguma coisa? 💜")

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    print("ERRO: TOKEN nao encontrado nas Environment Variables!")
else:
    bot.run(TOKEN)
