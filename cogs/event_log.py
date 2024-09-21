import discord
from discord.ext import commands
from discord import app_commands
from typing import List
from typing import Literal

class EventLoggerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="log_event", description="Logs an event with host, co-host, and attendees.")
    @app_commands.describe(host="The host of the event (Officer)", co_host="The co-host of the event (NCO/Officer)", server="In which server did the event unfold?", map="In which map was the event happening?", team="Which team did the clan members join during the event?",attendees="The list of attendees")
    async def log_event(self, interaction: discord.Interaction, host: discord.User, co_host: discord.User | None, server: str, map: Literal['Runespire', 'Stonetonas'], team: Literal['Redcliff', 'Empyrean', 'Overseer', 'Korblox'], attendees : str | None = None):
        co_host_mention = f"<@{co_host.id}>" if co_host else "No one"
        # supposedly only valid mentions are parsed
        if attendees:
            valid_attendees = [
                attendee for attendee in attendees.split()
                if attendee.startswith("<@") and attendee.endswith(">")
            ]

            attendee_ids = [attendee.strip('<@!>') for attendee in valid_attendees]
        else:
            valid_attendees = []
            attendee_ids = []

        attendee_mentions = " ".join(valid_attendees) if valid_attendees else "No one"
        print(attendee_ids)
        log_message = (
            "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
            ":Potato: Win Logs :Potato:\n"
            f"Host: <@{host.id}>\n"
            f"Co-Host: {co_host_mention}\n"
            f"Server: {server}\n"  # will become parameter
            f"Map: {map}\n"  # will become parameter
            f"Team: {team}\n"  # will become parameter
            f"Attendees: {attendee_mentions}\n"
            "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
        )

        await interaction.response.send_message(log_message)

async def setup(bot):
    await bot.add_cog(EventLoggerCog(bot))