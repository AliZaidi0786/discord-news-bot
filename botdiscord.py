import discord
import random
#import math
import requests
import os
from newsapi import NewsApiClient


DISCORD_TOKEN=""
newsapi = NewsApiClient(api_key='Enter your API key here!')

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "%news":
		response=requests.get("Enter your News API here!")
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		matter=response.json()
		r=random.randrange(0,19)
		await message.channel.send(matter['articles'][r]['title'])
		await message.channel.send(matter['articles'][r]['url'])

bot.run(DISCORD_TOKEN)
