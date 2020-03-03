import discord
import urllib.request
import json
from time import sleep
import random

client = discord.Client()

citycode = '400020'
resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
resp = json.loads(resp.decode('utf-8'))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("/"):
        if client.user != message.author:
            c = message.content
            x1 = c[1]

            if message.content == ("/おはよう"):
                m0 = "おはようございます" + message.author.name + "さん！"
                m1 = resp['location']['city']
                m1 += "の天気は、\n"
                for f in resp['forecasts']:
                    m1 += f['dateLabel'] + "が" + f['telop'] + "\n"
                    m2 = "です。"
                await message.channel.send(m0 + m1 + m2)
                r2 = ["大吉", "中吉", "小吉", "吉", "凶", "大凶", "吉外"]
                await message.channel.send("本日の運勢は" + random.choice(r2) + "でした！")



            if x1 == ("t"):
                m4 = int(c[4]) * 6
                await message.channel.send(c[2] + "分" + str(m4) + "秒" + "計測します。")
                sleep(int(c[2]) * 60 + m4)
                await message.channel.send(message.author.mention + " " + c[2] +  "分" + str(m4) + "秒" + "経過しました。")

            if message.content == ("/cat"):
                r1 = ["ネコより私のほうが可愛いです！！", "https://www.pakutaso.com/20200309063post-25896.html", "https://www.pakutaso.com/20200315063post-25898.html", "https://www.pakutaso.com/20200304063post-25899.html", "https://www.pakutaso.com/20200203058post-25990.html", "https://www.pakutaso.com/20200349063post-25901.html", "https://www.pakutaso.com/20200344063post-25900.html"]
                await message.channel.send(random.choice(r1))




client.run("NjQyOTY0NjA3ODM2ODgwOTA2.XluHyg.9S7OPxQ0AMblpxlGyq6MFonKuFA")
