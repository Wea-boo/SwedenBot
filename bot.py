import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")  # Loads each cog file

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        await load_cogs()  # Load the cogs when the bot is ready
        synced = await bot.tree.sync()  # Sync the slash commands
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"An error occurred: {e}")

bot.run(TOKEN)