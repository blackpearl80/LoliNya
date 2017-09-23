import discord
import asyncio
import random
import requests
import io
import os
from discord.ext import commands
from os import listdir

description = "LoliNya Bot"
bot_prefix = "!"
bot_name = "LoliNya"

client = commands.Bot(description=description, command_prefix=bot_prefix)

@client.event
async def on_ready():
    print('Logged in as')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)

# Bot commands from here

# When someone join the server...
@client.event
async def on_member_join(member):
    serverchannel = member.server.default_channel
    msg = "N-nya! Welcome {0} to {1} server! (/ω＼)".format(member.name, server.name)
    await client.send_message(serverchannel, msg)

# When someone leave the server...
@client.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel
    msg = "{0} as left the server. Goodbye {0}. N-not that I care a-anyway, nya! (=ﾟωﾟ)ﾉ".format(member.name)
    await client.send_message(serverchannel, msg)

@client.command(pass_context=True)
async def ping(ctx):
    await client.say('Pong!')


@client.command(pass_context=True)
async def nya(ctx):
    # Show a random image when using the command !nya
    nekoRnd = random.choice(["EM51ap9PlJOJa","VykFoFEFQPT4A","VcGAyTT62OIdq","qWAvh9GmlryEg","yLhsOrnEGiPRe","W2JiHcUyeev5u","jqXH5VeTYNeTu","jCaU8WfesJfH2","j0SAkJD6RchKE","I9rLlXXDOdb7a","AGnyClt29AkEg","l8vODjlQrm2YM","UfZR37U3uqsTe","PGkmhjuq9MdVK","zqg9QNFbbtkqY","4JpvyNYuyf0aI","13b39zZL7zioaQ","8s2HN6SdyQd1K","KmajZqcgbSRxK"])
    channel = ctx.message.channel
    response = requests.get("https://media.giphy.com/media/" + nekoRnd + "/giphy.gif", stream=True)
    nya = random.choice(['Nya! =ටᆼට=', 'Nyo!', '*Purssss intensify*', 'Meow Meow ㅇㅅㅇ','Someone said nya!? Nya!',"Nya? Nyaa... Nya nya. *licks her paws*. Nya. (⁎˃ᆺ˂)","Nekomimi image alert incoming! Nya!","D-do you Nya too? (ΦωΦ)","Nekos are the best, don't you think {}!? *Purrs*".format(ctx.message.author.mention)])
    await client.send_file(channel, io.BytesIO(response.raw.read()), filename="neko.gif", content=nya)


@client.command(pass_context=True)
async def yorha(ctx):
    yorhaMsg = random.choice(['For the Glory of Mankind!','You don\'t say.','Become as Gods','Everything that lives is designed to end. We are perpetually trapped in a never-ending spiral of life and death','What is it that separates machines from androids like us?','I—or we machine lifeforms I suppose—have a keen interest in humanity. Love. Family. Religion. War.','This pod has serious concerns about unit A2 cognitive abilities.',"Don't know, Don't Care"])
    await client.say(yorhaMsg)


@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    # Show a random image when using the command !hug
    hugRnd = random.choice(["a5s3dI6Wv1Qcw","aVmEsdMmCTqSs","od5H3PmEG5EVq","9bbIQ1ZUgHbqw","xZshtXrSgsRHy","IRUb7GTCaPU8E","3ZnBrkqoaI2hq","aD1fI3UUWC4","DjczAlIcyK1Co","3bqtLDeiDtwhq","GMFUrC8E8aWoo","Tog1tiXFFqZji","wxpvOKvCGf82Y"])
    channel = ctx.message.channel
    response = requests.get("https://media.giphy.com/media/" + hugRnd + "/giphy.gif", stream=True)
    if not user:
        #hugR = random.choice(["*Evades and throw you a pillow.* H-hey nya, don't try hug me! (/ω＼)","Σ(￣ロ￣lll) da heck you are hugging? Are you crazy?","Nya bruh. If you are so desperate to hug something, t-try a train at 100km/h!","Error 404. Object to hug not found. please try again nya!"])
        #await client.say(hugR)
        return
    #elif user.mention == user.mention_everyone:
    #await client.say("Th-this isn't a or-org... I mean everyone as been hugged. (/ε＼*)")
    else:
        if user.mention == ctx.message.author.mention:
            hugR = random.choice(["So sad. You must be feeling so lonely... (⋟﹏⋞)","Are you feeling cold?","Nya... so pitiful. (´・ω・｀)","Amaaazing nya! You can actually hug yourself! Congratz {}. (￣ε￣〃)ｂ".format(ctx.message.author.mention),"You hugged yourself! That's a nice improvement!"])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="hug.gif", content=hugR)
        elif user.name == client.user.name:
            hugR = random.choice(["T-thankies, I-I guess...","Huggu {}. (.づ◡﹏◡)づ.".format(ctx.message.author.mention),"H-hey, what are you touching! You p-perv! (#｀皿´)","Cuddles {}".format(ctx.message.author.mention), "Pedo much {}? (￣︶￣;)".format(ctx.message.author.mention)])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="hug.gif", content=hugR)
        else:
            hugR = random.choice(["{0}, this is a huggie huggie from {1}. ⊂((・▽・))⊃".format(user.mention,ctx.message.author.mention),"A lovely and warm hug to you, {}. ლ(´ ❥ `ლ)".format(user.mention),"You've been hugged, {}. ლ(･ω･*ლ)".format(user.mention),"Hug {} tight. I want a huggu too, nya. (◕︿◕✿)".format(user.mention)])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="hug.gif", content=hugR)

@client.command(pass_context=True)
async def pet(ctx, user: discord.Member = None):
    # Show a random image when using the command !pet
    petRnd = random.choice(["ZGXGE1F1l8OY0","k5ganPlCBq1uU","BxdqaKAfdcCsg","QJpNqJJtBnkwU","lq72vRtxJtpgQ","4HP0ddZnNVvKU","xLm9fux5DSodq","ERUkEhOS1diV2","iM0nTZDrFMPOE","e7xQm1dtF9Zni","r61gZfqvJZMtO","lZnEy2UefUZvq","SvQ7tWn8zeY2k","L2z7dnOduqEow","X9MUeQelKifU4","iGZJRDVEM6iOc"])
    channel = ctx.message.channel
    response = requests.get("https://media.giphy.com/media/" + petRnd + "/giphy.gif", stream=True)
    if not user:
        #petR = random.choice(["P-pet me please! (* >ω<)=3","Are you trying to pet someone? (๑˃̵ᴗ˂̵)و","Pets are good nya! (￣∇￣)","I would love that pet. Can I have one please, nya? （●＞ω＜●）"])
        #await client.say(petR)
        return
    #elif user.mention == user.mention_everyone:
    #await client.say("Th-this isn't a or-org... I mean everyone as been hugged. (/ε＼*)")
    else:
        if user.mention == ctx.message.author.mention:
            petR = random.choice(["Y-you can't seriously pet yourself nya... Σ(ﾟДﾟ)","Are you brushing your hairs just to look cool? (ー∀ー；)","Does pet yourself feels good, {}?".format(ctx.message.author.mention),"Try and find someone else to pet instead yourself! (´ε｀；)","M-maybe I'll let you pet me if you are nice."])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="pet.gif", content=petR)
        elif user.name == client.user.name:
            petR = random.choice(["Pets feels so good! *purrrrs* (=^_^=)","Thankies {}, pet me more nya! (=①ω①=)".format(ctx.message.author.mention),"Is not that I asked for it but thanks... (=ｘェｘ=)","*Blushu* One more, I love pets. (ᗒᗨᗕ)"])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="pet.gif", content=petR)
        else:
            petR = random.choice(["Have a pat {}".format(user.mention),"Someone sent you a pat, {}".format(user.mention),"Pettu-pettu {}. Nyaaa, so cute.".format(user.mention),"Pat {0}. H-hey, I'm jelous! Pet me too {1}!! |ω・｀)".format(user.mention, ctx.message.author.mention),"Sending a pet to {}. Mission complete NYU!".format(user.mention)])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="pet.gif", content=petR)

@client.command(pass_context=True)
async def slap(ctx, user: discord.User = None):
    # Show a random image when using the command !slap
    slapRnd = random.choice(["ayYEBVLyVC9iw","iREUC7qrjN4vC","Zau0yrl17uzdK","4nHsalgvIblUk","zRlGxKCCkatIQ","81kHQ5v9zbqzC","fNdolDfnVPKNi","jLeyZWgtwgr2U","VEmm8ngZxwJ9K","LB1kIoSRFTC2Q"])
    channel = ctx.message.channel
    response = requests.get("https://media.giphy.com/media/" + slapRnd + "/giphy.gif", stream=True)
    if not user:
        #slapMsg = random.choice(['Nya. Your slap had no effect, you silly!', 'Are you trying to kill mosquitoes or something, nya?'])
        #await client.say(slapMsg)
        return
    else:
        if user.mention == ctx.message.author.mention:
            slapMsg = random.choice(['Should I slap you instead? （≧ｙ≦＊）', 'Such violence (つ﹏⊂), a-are you hurt {}?'.format(ctx.message.author.mention)])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="slap.gif", content=slapMsg)
        elif user.name == client.user.name:
            slapMsg = random.choice(["Hey, why are you slapping me!? ༼☯﹏☯༽",
                                     "S-stop it! You shouldn't slap kittens, y-you meanie! ༼ノ◕ヮ◕༽ノ︵┻━┻",
                                     "Y-you know... I might *like* it... (=ↀωↀ=)"])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="slap.gif", content=slapMsg)
        else:
            slapMsg = random.choice(["You've been slapped {}, I b-bet you *like* it! (〃￣ω￣〃ゞ".format(user.mention),"Slap {}. B-baka! (*＇Д＇)ﾉｼ)ﾟﾛﾟ)".format(user.mention),"{0} gives you a lovely slap, {1}. N-nya. ｏ(≧▼≦○〃".format(ctx.message.author.mention, user.mention),"S-S-Slapping sometimes is good for health, don't you know {}?".format(user.mention),"Slap Slap. Snap out of it {}! (=ﾟωﾟ)つ)ﾟ∀ﾟ)".format(user.mention)])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="slap.gif", content=slapMsg)

@client.command(pass_context=True)
async def spank(ctx, user: discord.User = None):
    # Show a random image when using the command !spank
    spankRnd = random.choice(["5JfmRGx","8ea38Q7","xbU26Le","oLxhBlr","iD8W5KK","nSBsk3Y","2b4B4dZ","khdUQwu","Ha17MT3","MWKUWfq"])
    channel = ctx.message.channel
    response = requests.get("https://imgur.com/" + spankRnd + ".gif", stream=True)
    if not user:
        #spankMsg = random.choice(["W-who are you spanking, You perv! (#｀皿´)","Let me spank you instead? (｀ω´)","M-my master spank me when I'm a bad bot! (ノ﹏ヽ)","Don't you dare to spank me! ლಠ益ಠ)ლ","Someone as been bad to you, {}?".format(ctx.message.author.mention)])
        #await client.say(spankMsg)
        return
    else:
        if user.mention == ctx.message.author.mention:
            spankMsg = random.choice(["D-do you likes it, nya?","Why are you spanking yourself?","Masochist much, {}?".format(ctx.message.author.mention),"*Enjoys the view*. I-I'm not a perv, I swear! NYA!","Are you just teasing someone? *feels tempted*."])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="spank.gif", content=spankMsg)
        elif user.name == client.user.name:
            spankMsg = random.choice(["H-hey that's hurt! S-stop it!","Why me. (இ﹏இ`｡) I did anything bad!","S-stop spanking me, nya! W-wait.. actually I likes it... *blushu*","No no no! Not me! I bet Moist likes it more!","Yamete kudasai senpai! I'm innocent! ((;ﾟДﾟ))"])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="spank.gif", content=spankMsg)
        else:
            spankMsg = random.choice(["*Spanku spanku* you have been a bad kitten, {}".format(user.mention),"{0} stop being meanie to {1}!!!".format(user.mention, ctx.message.author.mention),"*Spank!* Y-you likes it {}? Want more? *grin intensify*".format(user.mention),"I-I might like that too! Oh my, what I'm saying...((-ω-｡)(｡-ω-))","*Lewdie spank* and *spank more* ... *spank spank spank spank spank!* I'm satisfied. (○ﾟε＾○)v"])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="spank.gif", content=spankMsg)

@client.command(pass_context=True)
async def poke(ctx, user: discord.User = None):
    # Show a random image when using the command !spank
    pokeRnd = random.choice(["yITI94s","CaXE0fX","3s6cBSh","FJxZhEI","SjjHjqU","sRvh3pA","hHqkKcE","hRseqxj","1tcQnAX","dirFXV6","CYGTaXK","d9xY2dw"])
    channel = ctx.message.channel
    response = requests.get("https://imgur.com/" + pokeRnd + ".gif", stream=True)
    if not user:
        #pokeMsg = random.choice(["","",""])
        #await client.say(pokeMsg)
        return
    else:
        if user.mention == ctx.message.author.mention:
            pokeMsg = random.choice(["I won't allow that! NYA.","Self pokes are BAD, you are BAD!","Are you asking me to poke you? *blushu*"])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="poke.gif", content=pokeMsg)
        elif user.name == client.user.name:
            pokeMsg = random.choice(["Eeeek. Why are you poking me!?","Ouch, you shouldn't poke me so hard. Meanie.","*blushu* w-where you are poking me, you perv. N-nya!","Abusing of a poor innocent bot, do you?","Poking me like that... it tickles!"])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="poke.gif", content=pokeMsg)
        else:
            pokeMsg = random.choice(["*Pokes {0}*. {1}, I-I'm innocent!".format(user.name, ctx.message.author.mention),"Does this poke feels good {}, nya?".format(user.mention),"You have been poked from {}.".format(ctx.message.author.mention),"Sneak poke {0}! Will you poke me too {1}?".format(user.mention, ctx.message.author.mention)])
            await client.send_file(channel, io.BytesIO(response.raw.read()), filename="poke.gif", content=pokeMsg)

@client.command(pass_context=True)
async def bot(ctx):
    # Bot Commands Info
    embed = discord.Embed(
        title="Hey! It's a me, M-Ma... jokes!! It is your lovely-dovely nekomimi bot!\n",
        color=0xe67e22,
        description='Showing you some of my "features" (Not in a lewd way, b-baka!):\n'
                    "- Welcome Message for whoever join! [NEW]\n"
                    "- Goodbye Message for whoever leave! [NEW]\n"
    )
    embed.set_author(
        name=client.user.name,
        icon_url="https://cdn.discordapp.com/attachments/356158413861814273/356237516585566208/5ka93GJ.png",
        url="https://cdn.discordapp.com/attachments/356158413861814273/356237516585566208/5ka93GJ.png"
    )
    embed.add_field(
        name="NEW COMMANDS",
        value="1: !slap (Good for the meanies!)\n"
              "2: !hug (Love is in the air~)\n"
              "3: !yorha (For those that feels a bit \"android\")\n"
              "4: !bot (Huh? Don't you remember me, nya? *puppy eyes*)\n"
              "5: !nya (Because everyone is a kitten inside)\n"
              "6: !pet (Who doesn't love pet?)\n"
              "7: !spank (A good spank is good?)\n"
              "8: !poke (Pokes are fun! Don't be lewd tho!)\n",
        inline=False
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/356158413861814273/356237516585566208/5ka93GJ.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/356158413861814273/356237516585566208/5ka93GJ.png")

    msgDet = "\nThis message will be deleted in 20 seconds, nya!"

    msg1 = await client.say(embed=embed)
    await asyncio.sleep(5)
    msg2 = await client.say(msgDet)
    await asyncio.sleep(5)
    await client.delete_message(msg2)
    msg3 = await client.say("Deleting in 10... NYA!")
    await asyncio.sleep(5)
    await client.delete_message(msg3)
    await asyncio.sleep(5)
    await client.delete_message(msg1)

client.run('MzU2MTYwODU1Njg1MjAxOTIx.DJc5WA.FFrO4uDlZXPCN-jsuJvhOYSOlCc')
