import disc
import sys,os

CHANNEL_ID=803311577020760109
bot = disc.disc(os.getenv('DISCORD_TOKEN'))
print(open('text').read())
bot.send(CHANNEL_ID, open('text').read())
