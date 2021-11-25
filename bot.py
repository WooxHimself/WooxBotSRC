import asyncio
import datetime
import functools
import itertools
import json
import logging
import math
import os
import platform
import random
import time
from asyncio import sleep
from random import choice
from typing import List

import colorama
import discord
import requests
import youtube_dl
from aiohttp import ClientSession
from async_timeout import timeout
from colorama import Fore, Style
from discord import Client, Intents
from discord.enums import Status
from discord.ext import commands
from discord.ext.commands import Bot
from discord_components import Button, ButtonStyle, DiscordComponents
import secrets
from bs4 import BeautifulSoup
import PyCurrency_Converter

os.system('clear')
os.system('cls')
print("Starting WooxBot...")






client = commands.Bot(command_prefix = '-')

discord.Intents.all()




intent = Intents().all()
intent.members = True

response = requests.get("https://www.bitcoin.de")
soup = BeautifulSoup(response.content, 'html.parser')
btc_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/etheur/market")
soup = BeautifulSoup(response.content, 'html.parser')
ether_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/bcheur/market")
soup = BeautifulSoup(response.content, 'html.parser')
bch_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/btgeur/market")
soup = BeautifulSoup(response.content, 'html.parser')
btg_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/bsveur/market")
soup = BeautifulSoup(response.content, 'html.parser')
bsv_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/ltceur/market")
soup = BeautifulSoup(response.content, 'html.parser')
ltc_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/xrpeur/market")
soup = BeautifulSoup(response.content, 'html.parser')
xrp_price = soup.find(id="ticker_price").text
response = requests.get("https://www.bitcoin.de/de/etheur/market")
soup = BeautifulSoup(response.content, 'html.parser')
ether_price = soup.find(id="ticker_price").text






@client.event
async def on_ready():
    channel = client.get_channel(726462784170229760)
    embed=discord.Embed(title="<:info:909522102330228736> INFO!", color=0xff1c21)
    embed.add_field(name=":green_circle: BOT JE ONLINE", value="Všechny funkce byly zapnuty!", inline=True)
    embed.set_footer(text="© WooxBot 2021")
    await channel.send(embed=embed)
    await client.change_presence(activity=discord.Game(name='BugFixer.exe'))
    logging.info("Bot started successfully!")




        
    os.system('cls')
    print(Fore.RED + """ 
    
    ██╗    ██╗ ██████╗  ██████╗ ██╗  ██╗    ██████╗  ██████╗ ████████╗
    ██║    ██║██╔═══██╗██╔═══██╗╚██╗██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝
    ██║ █╗ ██║██║   ██║██║   ██║ ╚███╔╝     ██████╔╝██║   ██║   ██║   
    ██║███╗██║██║   ██║██║   ██║ ██╔██╗     ██╔══██╗██║   ██║   ██║   
    ╚███╔███╔╝╚██████╔╝╚██████╔╝██╔╝ ██╗    ██████╔╝╚██████╔╝   ██║   
    ╚══╝╚══╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                                  
    
    """ + Style.RESET_ALL)
    time.sleep(0.5)
    print("")
    print("")
    print(f"BOT: " + Fore.YELLOW + "{0.user}".format(client))
    time.sleep(0.3)
    print("STATUS: " + Fore.GREEN + "ONLINE")
    print("")
    time.sleep(0.2)
    print("")
    print("")
    print("LOGS:")



@client.event
async def on_message(message):
    if message.author.bot:
        return


@commands.Cog.listener()
async def on_member_update(self, before, after):
    if before.id == 726462784170229760:
      if after.status == discord.Status.offline:
        channel = self.bot.get_channel(726462784170229760)
        timestamp = datetime.now()
        embed = discord.Embed(title = "⚠️ WooxBOT je Offline!", description = "Naposledy Offline: " + str(timestamp.strftime("%H:%M:%S")) , color = 0xf03224)
        embed.add_field(name = "Vyčkejte než Woox zvedne prdel a opraví to", value = ";)")
        await channel.send(embed = embed)

#Prefix


#Remove the default help command
client.remove_command("help")





	
#Help command

@client.group(invoke_without_command=True)
async def help(ctx):

    embed=discord.Embed(title="HELP MENU", description="Defaultní help menu pro WooxBOT 2.3", color=0xe839fb)
    embed.add_field(name="======== ZÁBAVA ========", value="dadjoke |  ping |  gay |  weather |  ud |  coinflip |  8ball |  sorryforping |  hug |  cm  |  meme", inline=False)
    embed.add_field(name="======== MODERACE ========", value="kick |  ban |  banlist", inline=False)
    embed.add_field(name="======== HUDBA ========", value="play |  stop |  skip |  join |  leave |  queue |  clearqueue |  pause |  volume", inline=False)
    embed.add_field(name="======== OSTATNÍ ========", value="serverlist |  info |  hey |  odezva | hug | members |  avatar  |  changelog  | uselessfact  | stepan ", inline=False)
    embed.add_field(name="======== NEZAŘAZENÉ ========", value="stfu |  cringe", inline=False)
    embed.add_field(name="======== NSFW ========", value="cocks", inline=False)
    embed.set_footer(text="© WooxBot 2021")
    await ctx.send(embed=embed)




badlinks = ['appnitro-discord.ru', 'apps-discord.org', 'apps-nitro.com', 'boost-discord.com', 'boosted-nitro.com', 'boostnitro.com', 'christmasdiscord.gifts', 'cliscord-gift.ru', 'cllscordapp.fun', 'cpp-discord.com', 'd.iscord.xyz', 'diccrd.com', 'dicord.gift', 'dicsord-airdrop.com', 'dicsord-airdrop.ru', 'dicsord-app.com', 'dicsord-gift.com', 'dicsord-give.com', 'dicsord-gives.com', 'dicsord-hypesquads.com', 'dicsord-nitro.com', 'dicsord-ticket.com', 'dicsord.gifts', 'dicsord.net', 'dicsord.pw', 'dicsord.ru', 'dicsord.space', 'dicsordapp.co', 'dicsordgift.com', 'dicsordgive.ru', 'dicsordnitro.info', 'dicsordnitro.store', 'dicsords.ru', 'diiscord.gift', 'dilscord.com', 'dilscordl.com', 'dirscod.com', 'dirscod.gift', 'dis.cord.gifts', 'disc0rd.site', 'discapp.info', 'disccrd.gifts', 'discoapps.club', 'discocl.xyz', 'discoclapp.pw', 'discoclapp.xyz', 'discocrd-nitro.com', 'discocrd.com', 'discocrd.gift', 'discocrd.gifts', 'discocrdapp.com', 'discod-nitro.ru', 'discod.art', 'discod.fun', 'discod.gift', 'discod.gifts', 'discod.info', 'discod.tech', 'discodapp.gift', 'discodnitro.info', 'discodnitro.ru', 'discond-nitro.ru', 'discond-njtro.tech', 'discond.gift', 'discond.ru', 'discoord.space', 'discorb-nitro.ru', 'discorb.blog', 'discorb.co', 'discorb.gift', 'discorb.gifts', 'discorb.ru', 'discorcd-gift.com', 'discorcd-nitro.com', 'discorcd.gift', 'discorcd.gifts', 'discorcdapp.com', 'discorcg.xyz', 'discorcl-air.xyz', 'discorcl-app.com', 'discorcl-app.ru', 'discorcl-app.xyz', 'discorcl-boost.ru', 'discorcl-gift.ru', 'discorcl-give.site', 'discorcl-nitro.com', 'discorcl-nitro.ru', 'discorcl-nitro.site', 'discorcl.app', 'discorcl.art', 'discorcl.click', 'discorcl.club', 'discorcl.gift', 'discorcl.gifts', 'discorcl.info', 'discorcl.link', 'discorcl.org', 'discorcl.shop', 'discorcl.site', 'discorclapp.com', 'discorclapp.fun', 'discorclapp.xyz', 'discorclgift.com', 'discorclgift.net.ru', 'discorclgift.xyz', 'discorclgifts.store', 'discorcll.com', 'discorcll.online', 'discorcz-booster.ru', 'discord-accept.com', 'discord-air.fun', 'discord-air.xyz', 'discord-airdop.link', 'discord-airdrop.com', 'discord-airdrop.fun', 'discord-airdrop.info', 'discord-airdrop.me', 'discord-airdrop.pw', 'discord-airnitro.xyz', 'discord-alidrop.me', 'discord-alrdrop.com', 'discord-app.cc', 'discord-app.click', 'discord-app.co', 'discord-app.co.uk', 'discord-app.gifts', 'discord-app.info', 'discord-app.io', 'discord-app.live', 'discord-app.me', 'discord-app.net', 'discord-app.ru', 'discord-app.shop', 'discord-app.top', 'discord-app.uk', 'discord-app.us', 'discord-app.xyz', 'discord-application.com', 'discord-applications.com', 'discord-appnitro.com', 'discord-apps.fun', 'discord-apps.site', 'discord-apps.space', 'discord-apps.xyz', 'discord-boost.xyz', 'discord-bugs.com', 'discord-claim.com', 'discord-claim.ru', 'discord-click.shop', 'discord-control.com', 'discord-controls.com', 'discord-cpp.com', 'discord-develop.com', 'discord-developer.com', 'discord-devs.com', 'discord-drop.gift', 'discord-drop.info', 'discord-drop.xyz', 'discord-drops.ru', 'discord-egift.com', 'discord-event.com', 'discord-event.info', 'discord-faq.com', 'discord-free-nitro.ru', 'discord-free.com', 'discord-free.site', 'discord-freenitro.online', 'discord-freenitro.pw', 'discord-fun.com', 'discord-game.com', 'discord-get.click', 'discord-get.shop', 'discord-gift-nitro.site', 'discord-gift.online', 'discord-gift.shop', 'discord-gift.site', 'discord-gifte.com', 'discord-gifte.site', 'discord-giftef.xyz', 'discord-gifteh.xyz', 'discord-giftes.com', 'discord-gifts.com', 'discord-gifts.me', 'discord-gifts.ru', 'discord-gifts.shop', 'discord-give.com', 'discord-give.net', 'discord-give.org', 'discord-give.ru', 'discord-give.xyz', 'discord-giveaway.com', 'discord-giveaways.ru', 'discord-glft.com', 'discord-glft.ru', 'discord-glft.xyz', 'discord-halloween.com', 'discord-halloween.link', 'discord-halloween.me', 'discord-halloween.ru', 'discord-hallowen.ru', 'discord-help.com', 'discord-helpers.com', 'discord-hse.com', 'discord-hype.com', 'discord-hypes.com', 'discord-hypesquade.com', 'discord-hypesquaders.com', 'discord-hypesquads.com', 'discord-info.com', 'discord-infoapp.xyz', 'discord-information.com', 'discord-information.ru', 'discord-informations.com', 'discord-informations.ru', 'discord-job.com', 'discord-jobs.com', 'discord-mod.com', 'discord-moderation.com', 'discord-moderations.com', 'discord-mods.com', 'discord-netro.ru', 'discord-nilro.ru', 'discord-niltro.com', 'discord-niltro.ru', 'discord-nitro-free.ru', 'discord-nitro.click', 'discord-nitro.club', 'discord-nitro.co', 'discord-nitro.eu', 'discord-nitro.gift', 'discord-nitro.link', 'discord-nitro.net', 'discord-nitro.org', 'discord-nitro.pro', 'discord-nitro.ru', 'discord-nitro.su', 'discord-nitro.tech', 'discord-nitroapp.ru', 'discord-nitroapp.xyz', 'discord-nitrogift.com', 'discord-nitrogift.ru', 'discord-nitros.ru', 'discord-nitrot.xyz', 'discord-nltro.com', 'discord-nltro.ru', 'discord-partner.com', 'discord-partners.com', 'discord-present.ru', 'discord-promo.com', 'discord-promo.info', 'discord-promo.ru', 'discord-promo.xyz', 'discord-promox.com', 'discord-report.com', 'discord-security.com', 'discord-service.com', 'discord-shop.fun', 'discord-spooky.ru', 'discord-staff.com', 'discord-steam.com', 'discord-steam.ru', 'discord-steam.site', 'discord-steams.com', 'discord-stemdrop.me', 'discord-stuff.com', 'discord-sup.com', 'discord-supports.com', 'discord-team.com', 'discord-tech.com', 'discord-tester.com', 'discord-up.ru', 'discord-verification.com', 'discord-verifications.com', 'discord-verify.com', 'discord-verify.ru', 'discord-vetify.com', 'discord.app', 'discord.foundation', 'discord.givaeway.com', 'discord.givaewey.com', 'discord.giveawey.com', 'discord.giveaweys.com', 'discord.link', 'discord.moscow', 'discord.shop', 'discord.voto', 'discord4nitro.com', 'discordaepp.com', 'discordapp.biz', 'discordapp.click', 'discordapp.one', 'discordapp.pw', 'discordapp.store', 'discordapp.su', 'discordapps.gift', 'discordappss.com', 'discordc.gift', 'discordchristmas.gifts', 'discordcommunlty.com', 'discordd.gift', 'discorde.gift', 'discordevents.com', 'discordf.gift', 'discordfrnitro.site', 'discordgift.app', 'discordgift.info', 'discordgift.net.ru', 'discordgift.org', 'discordgift.ru', 'discordgift.site', 'discordgift.xyz', 'discordgifte.com', 'discordgifte.site', 'discordgiftfree.site', 'discordgiftis.ru', 'discordgifts.co.uk', 'discordgifts.com', 'discordgifts.info', 'discordgifts.link', 'discordgifts.me', 'discordgifts.store', 'discordgiftss.com', 'discordgiftz.xyz', 'discordgiveaway.fun', 'discordgivenitro.com', 'discordgivenitro.ru', 'discordglft.com', 'discordglft.ru', 'discordglfts.com', 'discordhalloween.co.uk', 'discordhalloween.com', 'discordhalloween.uk', 'discordi.gift', 'discordj.gift', 'discordjob.com', 'discordl-steam.com', 'discordl.gift', 'discordlapp.fun', 'discordlgift.com', 'discordlgift.ru', 'discordll.gift', 'discordmoderations.com', 'discordn.gift', 'discordnitro.cc', 'discordnitro.click', 'discordnitro.fun', 'discordnitro.info', 'discordnitro.ru', 'discordnitroapp.ru', 'discordnitrogift.ru', 'discordq.com', 'discordqr.com', 'discordrgift.com', 'discordrgift.ru', 'discords-app.com', 'discords-developers.com', 'discords-gift.com', 'discords-gift.ru', 'discords-gifts.ru', 'discords-hypes.com', 'discords-hypesquad.com', 'discords-hypesquads.com', 'discords-moderation.com', 'discords-moderator.com', 'discords-nitro.xyz', 'discords-nitroapp.xyz', 'discords-nitros.fun', 'discords-premium.com', 'discords-premium.site', 'discords-steam.com', 'discords-support.com', 'discords-teams.com', 'discords.ru', 'discords.us', 'discordsgift.com', 'discordsgift.info', 'discordstaff.xyz', 'discordsteam.com', 'discordsteam.ru', 'discordsteams.com', 'discordsub.com', 'discordt.gift', 'discordtotal.com', 'discordu.gift', 'discordup.ru', 'discordxnitro.xyz', 'discorgift.xyz', 'discorid.gift', 'discoril.com', 'discorl.com', 'discorrd.gift', 'discorrd.ru', 'discorrl.com', 'discorsd.gifts', 'discortnitosteam.online', 'discortnitostem.online', 'discourd.info', 'discrod-app.com', 'discrod-app.ru', 'discrod-app.site', 'discrod-apps.ru', 'discrod-gift.com', 'discrod-gift.xyz', 'discrod-glfts.com', 'discrod-nitro.fun', 'discrod-nitro.info', 'discrod-up.ru', 'discrod.gift', 'discrod.gifts', 'discrodapp.ru', 'discrodapp.site', 'discrodnitro.org', 'discrodsteam.ru', 'discrodup.ru', 'discurcd.com', 'diskord.ru', 'disocrd.codes', 'disocrd.gifts', 'disord.codes', 'disord.fun', 'disord.gifts', 'disordapp.codes', 'disordapp.gift', 'disordapp.gifts', 'disordgift.codes', 'disordgifts.com', 'disordglft.com', 'disordnitros.xyz', 'disordsnitro.gifts', 'disrcod.com', 'disrcod.gift', 'disrcod.gifts', 'dissord.gift', 'dizcord.gift', 'dlcsorcl.com', 'dlcsord-airdrop.com', 'dlicord-glfts.site', 'dlicsord.ru', 'dliscord-gift.com', 'dliscord-giveaway.ru', 'dliscord-glft.ru', 'dliscord-nitro.com', 'dliscord.com', 'dliscord.us', 'dliscordl.com', 'dliscordnltro.com', 'dliscords.com', 'dlscard.ru', 'dlsccrd.com', 'dlscocl.xyz', 'dlscocrd.club', 'dlscocrd.com', 'dlscocrdapp.com', 'dlscorcl.gift', 'dlscorcl.info', 'dlscorcl.pw', 'dlscorcl.ru', 'dlscorclapp.fun', 'dlscord-alirdrop.com', 'dlscord-app.com', 'dlscord-app.info', 'dlscord-app.net', 'dlscord-app.xyz', 'dlscord-apps.com', 'dlscord-boost.fun', 'dlscord-claim.com', 'dlscord-game.com', 'dlscord-gift.com', 'dlscord-gifts.com', 'dlscord-glft.pw', 'dlscord-halloween.ru', 'dlscord-hypesquad.com', 'dlscord-inventory.fun', 'dlscord-nitro.click', 'dlscord-nitro.club', 'dlscord-nitro.fun', 'dlscord-nitro.info', 'dlscord-nitro.link', 'dlscord-nitro.ru', 'dlscord-nitro.space', 'dlscord-nitro.store', 'dlscord-nltro.com', 'dlscord-nltro.ru', 'dlscord-nltro.xyz', 'dlscord-promo.com', 'dlscord-promo.xyz', 'dlscord-steam.com', 'dlscord-stime-2021.ru', 'dlscord-support.com', 'dlscord.app', 'dlscord.cc', 'dlscord.cloud', 'dlscord.co.uk', 'dlscord.gg', 'dlscord.gifts', 'dlscord.help', 'dlscord.in', 'dlscord.info', 'dlscord.ink', 'dlscord.link', 'dlscord.net', 'dlscord.one', 'dlscord.online', 'dlscord.org', 'dlscord.press', 'dlscord.pro', 'dlscord.shop', 'dlscord.space', 'dlscord.store', 'dlscord.support', 'dlscord.tech', 'dlscord.tips', 'dlscord.wiki', 'dlscord.work', 'dlscord.world', 'dlscordapp.codes', 'dlscordapp.fun', 'dlscordapp.info', 'dlscordapp.ru', 'dlscordapps.com', 'dlscordd.ru', 'dlscordgift.com', 'dlscordgived.xyz', 'dlscordglft.xyz', 'dlscordniltro.com', 'dlscordnitro.com', 'dlscordnitro.info', 'dlscordnitro.ru', 'dlscordnitro.store', 'dlscordnitros.gifts', 'dlscordnltro.ru', 'dlscordsglfts.xyz', 'dlscordsteam.com', 'dlscorldnitro.store', 'dlscourd.info', 'dlscrod-app.xyz', 'dlscrod.ru', 'dlscrodapp.ru', 'ds-nitro.com', 'dscord.gifts', 'dsicord.gift', 'event-discord.com', 'events-discord.com', 'free-dislcordnitrlos.ru', 'free-niltross.ru', 'free-nitlrols.ru', 'free-nitlross.ru', 'free-nitroi.ru', 'free-nitroos.ru', 'free-nitros.ru', 'free-nitross.ru', 'freediscrodnitro.org', 'freediskord-nitro.xyz', 'freegiftcards.co', 'freenitro.ru', 'freenitroi.ru', 'freenitrol.ru', 'freenitros.com', 'freenitros.ru', 'freenltro.ru', 'gave-nitro.com', 'gift-discord.shop', 'gift-nitro.store', 'giftdiscord.info', 'glets-nitro.com', 'glft-discord.com', 'hallowen-nitro.com', 'jope-nitro.com', 'ldiscord.gift', 'nitro-app-store.com', 'nitro-app.com', 'nitro-app.fun', 'nitro-discord.info', 'nitro-discord.me', 'nitro-discord.org', 'nitro-discord.ru', 'nitro-discordapp.com', 'nitro-discords.com', 'nitro-drop.com', 'nitro-gift.ru', 'nitro-gift.space', 'nitro-gift.store', 'nitro-up.com', 'nitroairdrop.com', 'nitroappstore.com', 'nitrochallange.com', 'nitrodlscordl.xyz', 'nitrofrees.ru', 'nitroos-frieie.ru', 'nltro.site', 'official-nitro.com', 'official-nitro.fun', 'premium-discord.com', 'premium-discords.com', 'promo-discord.com', 'seed-nitro.com', 'steam-discord.com', 'steam-discords.com', 'steam-dlscord.com', 'steam-free-nitro.ru', 'steam-nitro.ru', 'steam-nitros.com', 'steam-nitros.ru', 'steam-nltro.com', 'steam-nltro.ru', 'steam-nltros.ru', 'steamcommunity-nitro.ru', 'steamcommunity-nitrogeneral.ru', 'steamdiscord.com', 'steamdiscord.ru', 'steamdiscords.com', 'steamdiscrod.ru', 'steamdlscord.com', 'steamdlscords.com', 'steamgivenitro.com', 'steamnitro.com', 'steamnitros.com', 'steamnitros.ru', 'steamnltro.com', 'steamnltros.com', 'steamnltros.ru', 'steams-discord.ru', 'steamsdiscord.com', 'steamsnitro.ru', 'store-discord.com', 'up-discord.ru', 'verification-discord.com', 'verifications-discord.com', 'verify-discord.com', 'xesa-nitro.com', 'xess-nitro.com', 'xpromo-discord.com', 'yummy-nitro.com']

@client.event
async def on_message(message, ctx):
    if badlinks in message.content:
        await ctx.message.delete()
        embed=discord.Embed(title="<:error:909515248833294336> POKUS O PHISHING!", color=0xff1c21)
        embed.add_field(name=f"{ctx.message.author} PRAVDĚPODOBNĚ MÁ ÚČET V OHROŽENÍ", value="Uživatel dostal token log a jeho účet je ovlivněn phishing spamem. Uživatel byl umlčen do té doby než si změní heslo! Po změně hesla kontaktuj moderátory!", inline=True)
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)
        print(f"{ctx.message.author} PHISHING ATTEMPT DETECTED! | {ctx.guild}")
        


@client.command
async def offlinestatus(ctx):
    client.change_presence(status=discord.Status.offline)
    await ctx.message.delete()


#Dad jokes

with open("dadjokes.txt", "r", encoding="utf8") as dj:
    responses = dj.read().splitlines()
    
#GAY COMMAND

with open("gay.txt", "r", encoding="utf8") as gay:
	responses1 = gay.read().splitlines()
	
@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def gay(ctx):
	await ctx.send(f' {random.choice(responses1)}')

@gay.error
async def gay_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
        embed.add_field(name="PŘÍKAZ MÁ COOLDOWN!", value=f"Zkus to znovu za **{round(error.retry_after, 2)}s**", inline=True)
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)

@client.command()
async def niaxuvcock(ctx):
    await ctx.send("**Upozorňuji, že neručím za to co uvidíš, jestli tě to změní psychicky, jestli dostaneš infarkt, jestli tě odveze sanitka, za tohle všechno a ještě dál neručím... Pokud si odhalíš spoiler, neručím za výše uvedené potíže které mohou nastat...** || https://cdn.discordapp.com/attachments/911587423530676275/911670663046127646/umad.jpg ||")

@client.command()
async def dadjoke(ctx):
    await ctx.send(f' {random.choice(responses)}')

with open("useless.txt", "r", encoding="utf8") as useless:
	useless = useless.read().splitlines()
	
@client.command()
async def uselessfact(ctx):
	await ctx.send(f' {random.choice(useless)}')

#Ping pong command	
@client.command()
async def ping(ctx):
	await ctx.send('Pong! ')

@client.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
@commands.is_owner()

async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Přezdívka byla nastavena pro {member.mention} ')
	
#Hey command	
@client.command()
async def hey(ctx):
	await ctx.send('Zdravím, {}'.format(ctx.message.author.mention))


#Cringe command
@client.command()
async def cringe(ctx):
	await ctx.send("https://tenor.com/view/dies-of-cringe-cringe-gif-20747133")


	
	#LATENCY COMMAND
@client.command()
async def odezva(ctx):
    await ctx.send('Moje odezva je ***{0}*** seconds'.format(round(client.latency, 3)))

    
#Error Handling




		
@client.event
async def on_command_error(ctx,*,error):
	if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="CHYBÍ ARGUMENT/Y!", value="Prosím zkus to znovu.", inline=True)
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)
            print(f"Missing Arguments | {ctx.guild}")
            return
@client.event
async def on_command_error(ctx,error):
        fmt = ' and '.join(missing)
        embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
        embed.add_field(name="NEMÁŠ DOSTATEK PERMISÍ!", value="Potřebuješ permisi **{}**".format(fmt), inline=True)
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)
        print(f"User is missing permissions| {ctx.guild}")
        return
@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.BotMissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' and '.join(missing)
            fmt = ' and '.join(missing)
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="CHYBÍ MI PERMISE!", value="Potřebuji permisi **{}**".format(fmt), inline=True)
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)
            print(f"Bot is missing perms | {ctx.guild}")

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="PŘÍKAZ NENALEZEN!", value="Použij -help", inline=True)
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)
            print(f"Command not found | {ctx.guild}")
            return
	
    if isinstance(error, commands.MemberNotFound):
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="UŽIVATEL NENALEZEN!", value="Prosím uveďte správného uživatele.", inline=True)
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)
            return
    if isinstance(error, commands.MissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        fmt = ' and '.join(missing)
        embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
        embed.add_field(name="NEMÁŠ DOSTATEK PERMISÍ!", value="Potřebuješ permisi **{}**".format(fmt), inline=True)
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)
        print(f"User is missing permissions| {ctx.guild}")
    if isinstance(error, commands.NoPrivateMessage):
        embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
        embed.add_field(name="TENTO PŘÍKAZ NELZE POUŽÍT V DMs!", value="Použij ho na serveru **{}**".format(fmt), inline=True)
        embed.set_footer(text="© WooxBot 2021")
#Owner Command
@client.command()
async def owner(ctx):
	await ctx.send("""***Můj majitel***
	
	*Woox Takewashi#0101*
	Kontaktuj ho ohledně problémů!""")


#STFU Command




@client.command()
async def stfu(ctx):
	await ctx.send("Drz hubu prosim https://cdn.discordapp.com/attachments/670959839186386945/852570293813641226/SHUT_THE_FUCCK_UP_YOU_LITTLE_NASTY_ASS_BITCH_WHO_THE_FUCK_YOU_THINK_YOU_TALKING_TO_SHUT_YOUR_BITCH_A.mp4")

##KICK
##KICK
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  embed=discord.Embed(title="<:check:909519406873321502> ÚSPĚCH!", color=0x6afb40)
  embed.add_field(name="UŽIVATEL BYL VYKOPNUT!", value=f"Důvod: **{reason}**", inline=True)
  embed.set_footer(text="© WooxBot 2021")
  await ctx.send(embed=embed)
  if user.dm_channel == None:
      await user.create_dm()
  await user.dm_channel.send(
    content=f"""
                  **{ctx.guild}** 
  
    Byl jsi vyhozen z tohoto serveru!
    Administrátor: **{ctx.message.author}**
    Důvod: **{reason}** 
  
  
    *Prosím. pročti si příště pravidla*
    *Na server se můžeš znovu připojit*
  
    *©WooxBot 2021*""")
  await user.kick()
  print(f"Used command: +kick | {ctx.guild}")



#BAN SYSTEM
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason):
  embed=discord.Embed(title="<:check:909519406873321502> ÚSPĚCH!", color=0x6afb40)
  embed.add_field(name="UŽIVATEL BYL ZABANOVÁN!", value=f"Důvod: **{reason}**", inline=True)
  embed.set_footer(text="© WooxBot 2021")
  await ctx.send(embed=embed)
  if user.dm_channel == None:
      await user.create_dm()
  await user.dm_channel.send(
      content=f"""
                    **{ctx.guild}** 
      
      Byl jsi **PERMANENTNĚ** zabanován z tohoto serveru!
      Administrátor: **{ctx.message.author}**
      Důvod: **{reason}**
      Čas: **PERMANENTNÍ** 
      
      
      *Prosím. pročti si příště pravidla*
      *Pokud si myslíš, že jsi byl zabanován neprávem, kontaktuj administrátory serveru!*
      
      *©WooxBot 2021*""")
  
  await user.ban(reason=reason, delete_message_days=0)
  print(f"Used command: +ban | {ctx.guild}")




#UNBAN
@client.command()
@commands.has_permissions(ban_members=True)
async def unban (ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')
	
	for ban_entry in banned_users:
		user = ban_entry.user
		
	if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed=discord.Embed(title="<:check:909519406873321502> ÚSPĚCH!", color=0x6afb40)
            embed.add_field(name="UŽIVATEL BYL ODBANOVÁN!", value="", inline=True)
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)
            print(f"Used command: +unban | {ctx.guild}")






#
@client.command()
async def hug(ctx, *, member: discord.Member = None):
    """Hug someone on the server <3"""
    try:
        if member is None:
            await ctx.send(ctx.message.author.mention + " byl obejmut!")
        else:
            if member.id == ctx.message.author.id:
                await ctx.send(ctx.message.author.mention + " obejmul sám sebe!")
            else:
                embed=discord.Embed(title="Obejmutí", description=f"{ctx.message.author} obejmul {member.mention}", color=0xe32b9e)
                embed.set_thumbnail(url="https://c.tenor.com/FYKsVaNI7lkAAAAC/anime-hug.gif")
                embed.set_footer(text="© WooxBot 2021")
                await ctx.send(embed=embed)

    except:
        return
 


#BANLIST

@client.command()
async def banlist(ctx):
	"""Lists all banned users on the current server."""
	
	if ctx.message.author.guild_permissions.ban_members:
		x = await ctx.message.guild.bans()
		x = '\n'.join([str(y.user) for y in x])
		embed = discord.Embed(title="Seznam zabanovaných uživatelů", description=x, colour=0xFFFFF)
		return await ctx.send(embed=embed)

	else:
		await ctx.send("<:error:909515248833294336> **CHYBA**! **|** Nemáš dostatečné permise!")


#Coinflip

determine_flip = [1, 0]

@client.command()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip", description="Hodili jsme mincí, dostali jsme: **Hlavu**!")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip", description="Hodili jsme mincí, dostali jsme: **Ocas**!")
        await ctx.send(embed=embed)



@client.command()
async def btc(ctx):
    embed = discord.Embed(title="Bitcoiny")
    embed.add_field(name="Zakladatel", value="Satoshi Nakamoto", inline=False)
    embed.add_field(name="Limit", value="20.999.999,97690000 ₿", inline=False)
    embed.add_field(name="Blockchain", value="340 GB", inline=False)
    embed.add_field(name="1₿ v €", value=btc_price, inline=False)
    embed.set_footer(text="© WooxBot 2021 | Zdroje: API od bitcoin.com")
    await ctx.send(embed=embed)
#REPORT
@client.command()
async def eth(ctx):
    embed = discord.Embed(title="Ethereum")
    embed.add_field(name="Zakladatel", value="Vitalik Buterin, Gavin Wood & Jeffrey Wilcke", inline=False)
    embed.add_field(name="Codebase", value="Solidity", inline=False)
    embed.add_field(name="Blockchain", value="337 GB", inline=False)
    embed.add_field(name="1ETH v €", value=ether_price, inline=False)
    embed.set_footer(text="© WooxBot 2021 | Zdroje: API od bitcoin.com")
    await ctx.send(embed=embed)


#antispam
# Witcher pepeLaugh
@client.event
async def on_message(message):
   if 'witcher' in message.content:
      await message.channel.send(":point_up: :sleeping: :sleeping: :zzz:")
   else:
      await client.process_commands(message)
   if 'Witcher' in message.content:
      await message.channel.send(":point_up: :sleeping: :sleeping: :zzz:")
   elif 'zaklinac' in message.content:
      await message.channel.send(":point_up: :sleeping: :sleeping: :zzz:")
   elif 'zaklínač' in message.content:
      await message.channel.send(":point_up: :sleeping: :sleeping: :zzz:")
   elif 'Zaklinac' in message.content:
      await message.channel.send(":point_up: :sleeping: :sleeping: :zzz:")
   elif 'Zaklínač' in message.content:
      await message.channel.send(":point_up: :sleeping: :sleeping: :zzz:")

@client.event
async def on_message(message):
    if 'cm' in message.content:
        await message.channel.send("<@200537844383481856> <:tf:887051849478307911> https://cdn.discordapp.com/attachments/726462784170229760/910163366134284288/xdd.mp4")
    else:
        await client.process_commands(message)
    if 'CM' in message.content:
        await message.channel.send("<@200537844383481856> <:tf:887051849478307911> https://cdn.discordapp.com/attachments/726462784170229760/910163366134284288/xdd.mp4")
    elif 'cM' in message.content:
        await message.channel.send("<@200537844383481856> <:tf:887051849478307911> https://cdn.discordapp.com/attachments/726462784170229760/910163366134284288/xdd.mp4")
    elif 'Cm' in message.content:
        await message.channel.send("<@200537844383481856> <:tf:887051849478307911> https://cdn.discordapp.com/attachments/726462784170229760/910163366134284288/xdd.mp4")
    elif 'kdi cm' in message.content:
        await message.channel.send("<@200537844383481856> <:tf:887051849478307911> https://cdn.discordapp.com/attachments/726462784170229760/910163366134284288/xdd.mp4")
    elif 'criminal mastermind' in message.content:
        await message.channel.send("<@200537844383481856> <:tf:887051849478307911> https://cdn.discordapp.com/attachments/726462784170229760/910163366134284288/xdd.mp4")






#SERVERLIST

@client.command()
async def serverlist(ctx):
    """List the servers that the bot is active on."""
    x = ', '.join([str(server) for server in client.guilds])
    y = len(client.guilds)
    print("List Serverů: " + x)
    if y > 40:
        embed = discord.Embed(title="Právě aktivní na " + str(y) + " serverech:", description=config.err_mesg_generic + "```json\nNemohu zobrazit více jako 40 serverů!```", colour=0xFFFFF)
        return await ctx.send(embed=embed)
    elif y < 40:
        embed = discord.Embed(title="Právě aktivní na " + str(y) + " serverech:", description="```json\n" + x + "```", colour=0xFFFFF)
        return await ctx.send(embed=embed)
    print(f"Used command: +serverlist | {ctx.guild}")




@client.command()
@commands.is_owner()
async def offline(ctx):
    channel = client.get_channel(726462784170229760)
    embed=discord.Embed(title="<:info:909522102330228736> INFO!", color=0xff1c21)
    embed.add_field(name=":red_circle: BOT JE OFFLINE", value="Od této chvíle nelze použít žádné jeho funkce.", inline=True)
    embed.set_footer(text="© WooxBot 2021")
    await channel.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def online(ctx):
    channel = client.get_channel(726462784170229760)
    embed=discord.Embed(title="<:info:909522102330228736> INFO!", color=0xff1c21)
    embed.add_field(name=":green_circle: BOT JE ONLINE", value="Všechny funkce byly zapnuty!", inline=True)
    embed.set_footer(text="© WooxBot 2021")
    await channel.send(embed=embed)
    await ctx.message.delete()


# Christmas countdown!
@client.command(aliases=['xmas', 'chrimbo'])
async def christmas(ctx):
    """Christmas countdown!"""
    await ctx.send("**{0}** day(s) left until Christmas day! :christmas_tree:".format(str(diff.days)))

#Pocasi

api_key = "047799a2e1b9a99bb7d7de7c17613d2c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@client.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Počasí ve obci {city_name}",
                              color=ctx.guild.me.top_role.color,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Stav", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Teplota C°", value=f"**{current_temperature_celsiuis} °C**", inline=False)
            embed.add_field(name="Vlhkost vzduchu(%)", value=f"**{current_humidity} %**", inline=False)
            embed.add_field(name="Atmosférický tlak (hPa)", value=f"**{current_pressure} hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Požádal: {ctx.author.name}")
        await channel.send(embed=embed)
        print(f"Used command: -weather | {ctx.guild}")


    else:
        embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
        embed.add_field(name="MĚSTO NENALEZENO!", value="Prosím zkus to znovu.", inline=True)
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)
        print(f"CITY NOT FOUND: -weather | {ctx.guild}")




## WARN SYSTEM


#GOOGLE



#GOOGLE



## URBAN

@client.command(aliases=['ud'])
async def urban(ctx, *msg):
    """Searches on the Urban Dictionary."""
    try:
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        # Send request to the Urban Dictionary API and grab info
        response = requests.get(api, params=[("term", word)]).json()
        embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
        embed.add_field(name="NENALEZENY ŽÁDNÉ VÝSLEDKY!", value="Zkuste hledat znovu.", inline=True)
        embed.set_footer(text="© WooxBot 2021")        
        if len(response["list"]) == 0:
            return await ctx.send(embed=embed)
        # Add results to the embed
        embed = discord.Embed(title="Slovo", description="*" + word + "*", colour=embed.colour)
        embed.add_field(name="Nejlepší Definice:", value=response['list'][0]['definition'])
        embed.add_field(name="Příklady:", value=response['list'][0]['example'])
        await ctx.send(embed=embed)
        print(f"Used command: -urban | {ctx.guild}")
    except:
        embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
        embed.add_field(name="CHYBÍ ARGUMENT/Y!", value="Prosím zkus to znovu.", inline=True)
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)
        await ctx.send(config.err_mesg_generic)




#sorryforping

@client.command()
async def sorryforping(ctx):
    await ctx.send("https://media.discordapp.net/attachments/726462784170229760/910159977497387038/sorryForPing.png")

##JOIN


@commands.Cog.listener()
async def on_member_join(self, member, ctx):
    ment = member.mention
    await self.client.get_channel(channel, id).send(f"{ment} has joined the server.")

@commands.Cog.listener()
async def on_member_remove(self, member, ctx):
    ment = member.mention
    embed=discord.Embed(title="UŽIVATEL SE ODPOJIL!", description="Uživatel opustil tento server!", color=0xff0f0f)
    embed.add_field(name="{ment}", value="Cya!", inline=False)
    await ctx.send(embed=embed)






#8BALL



@client.command(aliases=['8ball'])
async def _eightball(ctx, *, question):
    try:
        responses = ['Pravděpodobně.',
                    "Nepočítal bych s tím.",
                    "Ano.",
                    "Že se ptáš",
                    "Ne",
                    "Možná",
                    "Tak určitě...",
                    "Tvoje mama <:tf:887051849478307911>"]

        await ctx.send(f'**Otázka**: {question}\n \n**Odpověď**: {random.choice(responses)}')
    except:
	      await ctx.send("<:error:909515248833294336> **CHYBA**! **|** Chybí argument: **Otázka**")
@_eightball.error
async def eightball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
        embed.add_field(name="CHYBÍ ARGUMENT!", value="Chybějící argument: **Otázka**")
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)


#covid

#

#MUSIC

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''


class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="Nenalezeny žádné výsledky!", value="`{}`".format(search))
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
                embed.add_field(name="Nenalezeny žádné výsledky!", value="`{}`".format(search))
                embed.set_footer(text="© WooxBot 2021")
                await ctx.send(embed=embed)


        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Nelze provést `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
                    embed.add_field(name="Nenalezeny žádné výsledky!", value="`{}`".format(webpage_url))
                    embed.set_footer(text="© WooxBot 2021")
                    await ctx.send(embed=embed)

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} dní'.format(days))
        if hours > 0:
            duration.append('{} hodin'.format(hours))
        if minutes > 0:
            duration.append('{} minut'.format(minutes))
        if seconds > 0:
            duration.append('{} sekund'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (discord.Embed(title='Nyní Hraje',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Délka', value=self.source.duration)
                 .add_field(name='Přidal', value=self.requester.mention)
                 .add_field(name='Nahrál', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 0.5
        self.skip_votes = set()

        self.audio_player = bot.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                # Try to get the next song within 3 minutes.
                # If no song will be added to the queue in time,
                # the player will disconnect due to performance
                # reasons.
                try:
                    async with timeout(180):  # 3 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.bot.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        pass

    @commands.command(name='summon', invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):
        """Joins a voice channel."""

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='nowplaying')
    async def _nowplaying(self, ctx):
        embed = (discord.Embed(title='Nyní Hraje',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Délka', value=self.source.duration)
                 .add_field(name='Přidal', value=self.requester.mention)
                 .add_field(name='Nahrál', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed

    @commands.command(name='join')
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """Summons the bot to a voice channel.
        If no channel was specified, it joins your channel.
        """

        if not channel and not ctx.author.voice:
            raise VoiceError('You are neither connected to a voice channel nor specified a channel to join.')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='leave', aliases=['disconnect'])
    async def _leave(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="NEJSI PŘIPOJEN K ŽÁDNÉMU KANÁLU!", value="Pro použití musíš být připojen do VC")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]

    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="NYNÍ NIC NEHRAJE!", value="Pro použití musíš něco pustit")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        if 0 > volume > 100:
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="HLASITOST MUSÍ BÝT MEZI 0-100!", value="Prosím uveď správné rozmezí!")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        ctx.voice_state.volume = volume / 100
        embed=discord.Embed(title="<:info:909522102330228736> INFO", color=0xff1c21)
        embed.add_field(name=":speaker: HLASITOST ZMĚNĚNA!", value="Hlasitost byla změněna na {}%".format(volume))
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)

    @commands.command(name='now', aliases=['current', 'playing'])
    async def _now(self, ctx: commands.Context):
        """Displays the currently playing song."""

        await ctx.send(embed=ctx.voice_state.current.create_embed())

    @commands.command(name='pause')
    async def _pause(self, ctx: commands.Context):
        """Pauses the currently playing song."""

        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='resume')
    async def _resume(self, ctx: commands.Context):
        """Resumes a currently paused song."""

        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='clearqueue')
    @commands.has_permissions(manage_guild=True)
    async def _clearqueue(self, ctx):
        ctx.voice_state.songs.clear()
        if ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()

        embed=discord.Embed(title="<:info:909522102330228736> INFO", color=0x123cfc)
        embed.add_field(name="FRONTA BYLA VYPRÁZDNĚNA", value="Aktuální song byl pozastaven a fronta vyprázdněna!")
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)




    @commands.command(name='stop')
    async def _stop(self, ctx: commands.Context):
        """Stops playing song and clears the queue."""

        if ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction('⏹')

    @commands.command(name='skip')
    async def _skip(self, ctx: commands.Context):
        """Vote to skip a song. The requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        if not ctx.voice_state.is_playing:
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="NYNÍ NIC NEHRAJE!", value="Pro použití musíš něco pustit")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 3:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()
            else:
                embed=discord.Embed(title="<:info:909522102330228736> INFO", color=0x123cfc)
                embed.add_field(name="HLASOVÁNÍ ÚSPĚŠNÉ", value="Hlas pro přeskočení byl přidán! (**{}/3**)".format(total_votes))
                embed.set_footer(text="© WooxBot 2021")
                await ctx.send(embed=embed)

        else:
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="JIŽ JSI HLASOVAL!", value="Vyčkej pro další hlasování!")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

    @commands.command(name='queue')
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's queue.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.songs) == 0:
            embed=discord.Embed(title="<:info:909522102330228736> INFO", color=0x123cfc)
            embed.add_field(name="FRONTA JE PRÁZDNÁ", value="*silence.wav*")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} skladby:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Zobrazuji stránku {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        """Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            embed=discord.Embed(title="<:info:909522102330228736> INFO", color=0x123cfc)
            embed.add_field(name="FRONTA JE PRÁZDNÁ", value="*silence.wav*")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')

    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index: int):
        """Removes a song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            embed=discord.Embed(title="<:info:909522102330228736> INFO", color=0x123cfc)
            embed.add_field(name="FRONTA JE PRÁZDNÁ", value="*silence.wav*")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')

    @commands.command(name='loop')
    async def _loop(self, ctx: commands.Context):
        """Loops the currently playing song.
        Invoke this command again to unloop the song.
        """

        if not ctx.voice_state.is_playing:
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="NYNÍ NIC NEHRAJE!", value="Pro použití musíš něco pustit")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')

    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        """Plays a song.
        If there are songs in the queue, this will be queued until the
        other songs finished playing.
        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        """

        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except YTDLError as e:
                await ctx.send('Při odesílání požadavku se vyskytl problém: {}'.format(str(e)))
            else:
                song = Song(source)

                await ctx.voice_state.songs.put(song)
                embed=discord.Embed(title="<:info:909522102330228736> INFO", color=0x123cfc)
                embed.add_field(name="PŘIDÁNO DO FRONTY!", value="{}".format(str(source)))
                embed.set_footer(text="© WooxBot 2021")
                await ctx.send(embed=embed)

    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="NEJSI PŘIPOJEN VE VC!", value="Pro použití musíš být ve VC")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
                embed.add_field(name="BOT JE JIŽ PŘIPOJEN NĚKDE JINDE!", value="Vyčkej než se bot odpojí, nebo se připoj za ním")
                embed.set_footer(text="© WooxBot 2021")
                await ctx.send(embed=embed)


client.add_cog(Music(client))

@client.command()
async def gachiroll():
    channel_id = 740302228270874764
    voice_channel = client.get_channel(channel_id)
    await voice_channel.connect()

@client.command()
async def stepan(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/726462784170229760/910646064967729162/Hon_na_romy__1.mp4 <@895685922169946162> <:tf:887051849478307911>")
#MUSIC

@client.command()
async def info(ctx, user: discord.Member):
	"""Gets info on a member, such as their ID."""
	try:
		embed = discord.Embed(title="Profil Uživatele: " + user.name, colour=user.colour)
		embed.add_field(name="Jméno:", value=user.name)
		embed.add_field(name="ID:", value=user.id)
		embed.add_field(name="Nejvyšší Role:", value=user.top_role)
		embed.add_field(name="Připojil se:", value=user.joined_at)
		embed.set_thumbnail(url=user.avatar_url)
		await ctx.send(embed=embed)
	except:
		await ctx.send("<:error:909515248833294336> **CHYBA**! **|** Chybí argument: **user.Mention**")

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
        embed.add_field(name="CHYBÍ ARGUMENT!", value="Chybějící argument: **user.Mention**")
        embed.set_footer(text="© WooxBot 2021")
        await ctx.send(embed=embed)


#TWITCH
@client.command()
async def euro(self, ctx):
    exchangeapikey = '03d889d168b758e1167a75a2f9290e8c'
    exurl = 'api.exchangeratesapi.io/v1/latest?access_key={exchangeapikey}&format=1'
    stats = requests.get(exurl)
    json_stats = stats.json()
    czk = json_stats["CZK"]
    usd = json_stats["EUR"]
    eur = json_stats["EUR"]
    yen = json_stats["YEN"]
    embed2 = discord.Embed(title=f"**1 EURO v CZK", description="Tyto informace nejsou pořád aktualizované a nemusí být 100% přesné!", colour=0x0000ff, timestamp=ctx.message.created_at)
    embed2.add_field(name="**1 EURO**", value=czk, inline=True)
    await ctx.send(embed=embed2)
        




#CHANGELOG

@client.command()
async def changelog(ctx):
    embed=discord.Embed(title="Changelog", description="Seznam změn pro Woox Bota")
    embed.add_field(name="V1.7 - Covid Update 11/17/21", value="Přidán příkaz -covid", inline=False)
    embed.add_field(name="V1.6 - Games Update 11/16/21", value="Přidány příkazy: -8ball, -coinflip, -hug", inline=True)
    embed.add_field(name="V1.5 - Music Update 11/16/21", value="Zprovozněna hudba, přidány příkazy jako: -play, -stop, -queue. Více v -help", inline=False)
    embed.add_field(name="V1.4 - Launch Update 11/15/21", value="Bot spuštěn. Příkazy jako -ud, -weather, -ban, -kick, -serverlist apod. přidány.", inline=False)
    embed.set_footer(text="© WooxBot 2021 | Created by Woox Takewashi#0101 | Private Project for tom's server!")
    await ctx.send(embed=embed)
    print(f"Used command: -changelog | {ctx.guild}")

#

## COCKS!!!

with open("cocks.txt", "r", encoding='utf-8') as cocks:
	responses2 = cocks.read().splitlines()
	
@client.command()
async def cocks(ctx, message):
	await ctx.send(f" Gettin' cock! {random.choice(responses2)}")



#TWITCH


#DO 
#NOT
#WRITE
#ANOTHER
#CODE
#UNDER
#THIS!!!!




		


#Invite command
@client.group(invoke_without_command=True)
async def invite(ctx):
	emm = discord.Embed(title = "Přidej mě na tvůj server!")
	
	emm.add_field(name = "Klikni na tento link pro přidání!", value = "https://discord.com/api/oauth2/authorize?client_id=909460654790938691&permissions=261711981543&scope=bot")
	
	await ctx.send(embed=emm)



client.load_extension("Cogs.covid")
client.load_extension("Cogs.members")
client.load_extension("Cogs.avatar")
client.load_extension("Cogs.subs")
client.run('OTA5NDYwNjU0NzkwOTM4Njkx.YZEnPQ.VMknPVpKzu3cJUZLVXbRWdgTyV4')