import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
CANAL_ID = 123456789012345678  # COLOQUE O ID DO CANAL
CARGO_ID = 987654321098765432  # COLOQUE O ID DO CARGO

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id == CANAL_ID and not message.author.bot:
        cargo = message.guild.get_role(CARGO_ID)

        for membro in cargo.members:
            try:
                await membro.send(
                    f"📢 Nova mensagem no servidor:\n\n{message.content}"
                )
            except:
                pass

    await bot.process_commands(message)

bot.run(TOKEN)
