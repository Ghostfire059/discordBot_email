from myImapClient import myImapClient
from emailUtil import emailUtil

import discord
from discord.ext import commands
from discordBot import discordBot

import schedule
from asyncio import sleep, create_task

#Constructor of myImapClient
IMAP = 'imap.example.com'
USER = 'username@example.com'
PASSWORD = 'applicationPassword'

#Constructor of emailsUtil
TARGET_EMAIL = 'targetemail@example.com'
TARGET_SUBJECT = 'Alerte Google : Ghostfire059'
EMAIL_FOOTER = 100

#Constructor of discordBot
DISCORD_TOKEN = 'PUT YOUR DISCORD TOKEN HERE'
CHANNEL_ID = 0

#Date to post
REGION = "Europe/Amsterdam"
TIME = "12:00"

#setup
imapClient = myImapClient(IMAP, USER, PASSWORD)
intents = discord.Intents.default()

utils = emailUtil(imapClient, TARGET_EMAIL, TARGET_SUBJECT, EMAIL_FOOTER)

bot = commands.Bot(command_prefix='!', intents=intents)
myBot = discordBot(CHANNEL_ID)

async def postEmail():
    email = utils.getEmail()
    email = utils.formatEmail(email)

    await myBot.postMessage(bot, email)

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')
    schedule.every().day.at(TIME, REGION).do(lambda: create_task(postEmail()))

    while True:
        schedule.run_pending()
        await sleep(1)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

bot.run(DISCORD_TOKEN)