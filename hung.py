import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import linecache
import random

from likeAHorse import generateDisplay, drawHangman

load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='h!')

# tracks the channels that the bot is being used in
bot.current_channels = set()


# function that chooses a word from the dictionary
def choose_word() -> str:
    word = linecache.getline('dictionary.txt', random.randint(1, 37105))
    return word


@bot.event
async def on_ready() -> None:
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")


# gamemode for when word is chose randomly from the dictionary
@bot.command(name='play')
async def play_dict(ctx) -> None:
    if ctx.channel not in bot.current_channels:
        bot.current_channels.add(ctx.channel)

        word = choose_word()
        attempt_number = 1
        guesses = []

        while attempt_number <= 10:
            try:
                reply_message = await bot.wait_for('message')
                if reply_message.content == '--q':
                    await ctx.channel.send('You quit.')
                    bot.current_channels.remove(ctx.channel)
                    return
                elif reply_message.content == word:
                    await ctx.channel.send('You win!')
                elif len(reply_message.content) == 1:
                    if reply_message.content in guesses:
                        await ctx.channel.send(f'"{reply_message.content}" has already been guessed. Guess again.')
                    else:
                        guesses.append(reply_message.content)
                        if reply_message.content not in word:
                            attempt_number += 1
                        await ctx.channel.send(generateDisplay(word, guesses))
                else:
                    attempt_number += 1
                    await ctx.channel.send(f'Incorrect! \n {generateDisplay(word, guesses)}')
            except asyncio.TimeoutError:
                await ctx.channel.send(f'You ran out of time. The word was {word}.')
        await ctx.channel.send(f'The man was so hung. You lose. \n The word was {word}.')
        bot.current_channels.remove(ctx.channel)


# gamemode for when a word is provided by a user
@bot.tree.command()
async def hang(interaction: discord.Interaction, word: str = " ") -> None:
    if interaction.channel not in bot.current_channels:
        bot.current_channels.add(interaction.channel)

        attempt_number = 1
        guesses = []

        await interaction.response.send_message(f'You chose {word}.', ephemeral=True)

        while attempt_number <= 10:
            try:
                reply_message = await bot.wait_for('message')
                if reply_message.content == word:
                    await interaction.channel.send('You win!')

                elif len(reply_message.content) == 1:
                    if reply_message.content == '--q':
                        await interaction.channel.send('You quit.')
                        bot.current_channels.remove(interaction.channel)
                        return
                    elif reply_message.content in guesses:
                        await interaction.channel.send(f'"{reply_message.content}" has already been guessed.'
                                                       f' Guess again.')
                    else:
                        guesses.append(reply_message.content)
                        if reply_message.content not in word:
                            attempt_number += 1
                        await interaction.channel.send(generateDisplay(word, guesses))
                else:
                    attempt_number += 1
                    await interaction.channel.send(f'Incorrect. \n {generateDisplay(word, guesses)}')

            except asyncio.TimeoutError:
                await interaction.channel.send(f'You ran out of time. \n The word was {word}.')
        await interaction.channel.send(f'The man was so hung. You lose. \n The word was {word}.')
        bot.current_channels.remove(interaction.channel)


if __name__ == '__main__':
    bot.run(token)
