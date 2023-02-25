import discord
from discord.ext import  commands
import asyncio

TOKEN = 'MTA3ODY4MDUzNTY2NjI3MDM2MA.GQFEe2.5QO05ay702Tga1DPM_F-glB8qALN90UIl8ijo8'
intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('BOT IS READY')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------')


@client.event
async def on_voice_state_update(member, before, after):
    if member.id == 1078680535666270360:
        return

    channelName = ""
    if after.channel is not None:
        channelName = after.channel.name

    if before.channel is None and after.channel is not None:
        await play_voice(after.channel, channelName)


async def play_voice(channel, oldName):
    await channel.edit(name="УВАГА ВОЛОДЯ В КАНАЛІ УВАГА")
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/Users/44782/Desktop/audio_2023-02-24_23-07-45.ogg"))
    while(True):
        await asyncio.sleep(1)
        if not vc.is_playing():
            await channel.edit(name=oldName)
            await vc.disconnect()
            break

if __name__ == '__main__':
    client.run(TOKEN)