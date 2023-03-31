import discord
import random
#import math
import requests
import os
from newsapi import NewsApiClient
#from dotenv import load_dotenv

#api-key=e6d136b01ba740c5943273d31ae35d63
#load_dotenv()

DISCORD_TOKEN=""
newsapi = NewsApiClient(api_key='')

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

#bot=discord.Client()
#top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          #language='en',
                                          #country='us')

#sources = newsapi.get_sources()

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
		response=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=e6d136b01ba740c5943273d31ae35d63")
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		matter=response.json()
		#print(matter)
		#x=len(matter)
		r=random.randrange(0,19)
		#print(x)
		#print(matter)
		#print(matter['articles'])
		#print(matter['articles'][r]['url'])
		#await message.channel.send(matter['articles'][r]['author'])
		await message.channel.send(matter['articles'][r]['title'])
		await message.channel.send(matter['articles'][r]['url'])
		#await message.channel.send("@everyone")

bot.run(DISCORD_TOKEN)
