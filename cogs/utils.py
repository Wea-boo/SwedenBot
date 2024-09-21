import discord
from discord.ext import commands
from discord import app_commands
import random

class UtilityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Show the server's latency in ms")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")

    @app_commands.command(name="scramble", description="Scramble a given word")
    @app_commands.describe(word="Which word to scramble")
    async def scramble(self, interaction: discord.Interaction, word: str):
        word = list(word)
        random.shuffle(word)
        await interaction.response.send_message("".join(word))

# Required setup function for loading the cog
async def setup(bot):
    await bot.add_cog(UtilityCog(bot))