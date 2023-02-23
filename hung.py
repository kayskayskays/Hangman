
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='h!')

# tracks the channels that the bot is being used in
bot.current_channels = set()


@bot.event
async def on_ready() -> None:
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")


@bot.tree.command
async def hang(interaction: discord.Interaction, word: str = " ") -> None:

    if interaction.channel not in bot.current_channels:

        bot.current_channels.add(interaction.channel)
        interaction.response.send_message(f'You chose {word}', ephemeral=True)
        bot.current_channels.remove(interaction.channel)

