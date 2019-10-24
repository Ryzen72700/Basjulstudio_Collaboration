import discord
import datetime
import requests
import json

token = "Not Found" #디스코드 봇 토큰
unveri_role = 636871756635832332 #미인증 역할 ID
user_role = 604934112863846401 #유저 역할 ID

client = discord.Client()

@client.event
async def on_ready():
    print("Basjul Studio // Made with XxPKBxX#4684 X 리스트 반월#1134")

@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(598378147339304961)
    member = guild.get_member(payload.user_id)
    if payload.message_id == 629641994917904384 and payload.emoji.name == "✅" and not user_role in member.roles:
        user_role_get = guild.get_role(user_role)
        unveri_role_get = guild.get_role(unveri_role)
        await member.add_roles(user_role_get)
        await member.remove_roles(unveri_role_get)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if not message.content.startswith("밧줄님 "):
        return
    command = message.content[4:].split()[0]
    commandline = message.content.split()[1:]
    if command == "랜덤냥":
        try:
            response = requests.get("http://aws.random.cat/meow").json()
        except Exception as error:
            embed = discord.Embed(title=":sob: 오류 발생!", description="랜덤 냥이를 불러오는 데 오류가 발생하였습니다.\n잠시 후 다시 시도해 주세요.", color=discord.Colour.dark_red(), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="오류 내용:", value=f"```\n{error}\n```", inline=True)
            embed.set_footer(text=f"{message.author.display_name}님을 위해", icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
        else:
            url = response["file"]
            embed = discord.Embed(title=":cat: 랜덤냥!", description="여러분이 좋아할 만한 랜덤냥을 제가 불러와드렸습니다.\n~~(후스다냥!#1924 님이 좋아해요.)~~", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
            embed.set_image(url=url)
            embed.set_footer(text=f"{message.author.display_name}님을 위해", icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)

client.run(token)