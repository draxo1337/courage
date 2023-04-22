import os
from afks import afks
import logging
import string
import time
import datetime
import os
import time
import datetime
import httpx
import requests
import random
import asyncio
import aiohttp
from discord import Game
from discord.ext import commands as commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound, MissingRequiredArgument
from discord.utils import get
from dhooks import Webhook, Webhook

os.system('pip install jishaku')
import jishaku
import discord
import sys
import psutil
import json
import shutil
import time
import wikipedia
import discord_games as games
from discord_games import button_games
import pathlib
from discord.ext import tasks
import webserver
from webserver import keep_alive
from discord.ui import View, Button
from PIL import Image, ImageDraw, ImageFont

os.environ["JISHAKU_FORCE_PAGINATOR"] = "False"
os.system('clear')
p = ","
prefix = ([", ", ","])
TOKEN = "MTAxMTMwNzcyODUzMjE1MjM0MA.GtcGUr.ICLemvxVI3CwbYe4-RrFm5DTpksjPrh6kHZMUI"

modsrole = 998879484642074644
black_list_role = 987687884150693888
admin_role = [987687884150693888, 998879484642074644]
erroremo = "<:error:1011269460751040583>"
pforp = False
intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.presences = False
headers = {'Authorization': f'Bot {TOKEN}'}
shards = 1
friendemo = "<:friends:1011556910547349614>"
partneremo = "<a:partner:1011957205920129114>"
bugemo = "<:IconBugHunterGoldBadge:1011559678473416785>"
devemo = "<a:discordBotDev:1011957869429674024>"
owneremo = "<:ROISFamilyOwners:1011958189648003143>"
earlyemo = "<a:early_animated:1011959978787094528>"
vipemo = "<:courage_vip:1011960874774319115>"
staffemo = "<a:Courage_Staff:1013783376672596069>"


async def prefixis(client, message):
    # returns a list
    return commands.when_mentioned_or(",")(client, message)


async def get_prefix(client, message):
    with open('info.json', 'r') as f:
        p = json.load(f)
    if message.author.id in p["np"]:
        nop = [", ", ",", ""]
        return discord.ext.commands.when_mentioned_or(*nop)(client, message)
    else:
        prefix = [", ", ","]
        return discord.ext.commands.when_mentioned_or(*prefix)(client, message)


client = commands.AutoShardedBot(shard_count=1,
                                 command_prefix=get_prefix,
                                 case_insensitive=True,
                                 intents=intents)
Client = discord.Client(intents=intents)
tree = client.tree

bot = client
chat = '''！﹒chat﹒🌙ᶻᶻᶻ'''
dashemo = "<:dash:1011298552074469386>"
replyemo = "<:reply:1011298613755904000>"
successemo = "<:courage_check:1018927279956566066>"

client.remove_command('help')

os.environ["JISHAKU_NO_UNDERSCORE"] = "TRUE"
noprefix = 980720852440084540
officialrole = 998788950506340473
import io


class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Moderation",
                emoji="<:courage_moderation:1019274210373275700>",
                description="Shows Moderation Commands"),
            discord.SelectOption(label="Fun",
                                 emoji="<:courage_fun:1019274140101910609>",
                                 description='''Shows Fun Commands'''),
            discord.SelectOption(
                label="Utility",
                emoji="<:courage_utility:1019272180808306688>",
                description="Shows Utility Commands")
        ]
        super().__init__(placeholder="Select an cartogery",
                         max_values=1,
                         min_values=1,
                         options=options)

    async def callback(self, interaction: discord.Interaction):

        embed_fun = discord.Embed(
            title="<:courage_fun:1019274140101910609> Fun Commands:",
            description=
            '''**screenshot** ・ `takes screenshot from website | ,screenshot <website>`
**pfp** ・ `shows cartogery of pfps` 
**akinator** ・ `Guesses character`,
**tictactoe** ・ `,ttt <@user>` 
**rps** ・ `,rps [@user]` 
**worldle** ・ `wordle game`
**gender** ・ `Guesses gender by name | ,gender <name>`''',
            color=discord.Colour(0x2f3136))

        embed_ut = discord.Embed(
            title="<:courage_utility:1019272180808306688> Utility Commaands:",
            description='''```
membercount, rmc, avatar, settings, botinfo, ping, invite
```''',
            color=discord.Colour(0x2f3136))

        embed_mod = discord.Embed(
            title=
            "<:courage_moderation:1019274210373275700> Moderation Commands:",
            description=
            '''**ban** ・ `bans member from guild | ,ban <@user> [reason]`
**unban** ・ `removes ban from member | ,unban <@user> [reason]` 
**kick** ・ `kicks member from guild, ,kick <@user> [reason]`,
**role** ・ `adds role and removes if member already has role | ,role <@user> <@role>` 
**mute** ・ `timeouts member for 1d if duration is not provided | ,mute <@user> [duration]` 
**unmute** ・ `removes timeout from member | ,unmute <@user>`''',
            color=discord.Colour(0x2f3136))
        if self.values[0] == "Fun":
            await interaction.response.send_message(embed=embed_fun,
                                                    ephemeral=True)
        elif self.values[0] == "Moderation":
            await interaction.response.send_message(embed=embed_mod,
                                                    ephemeral=True)
        elif self.values[0] == "Utility":
            await interaction.response.send_message(embed=embed_ut,
                                                    ephemeral=True)


class dropdown(discord.ui.View):
    def __init__(self, *, timeout=120):
        super().__init__(timeout=timeout)
        self.add_item(Select())
        self.response = None


def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk


@commands.command()
async def afk(ctx, *, reason="AFK"):
    member = ctx.author
    if member.id in afks.keys():
        afks.pop(member.id)
    else:
        #try:
        #await member.edit(nick = f"{member.display_name}")
        #except:
        #pass
        await asyncio.sleep(1)
        afks[member.id] = reason
        embed = discord.Embed(
            description=
            f"{member.mention} You're now afk with the reason: **{reason}**.",
            colour=0x2F3136)
        await ctx.send(embed=embed)


@bot.listen()
async def on_message(message):
    if message.author.id in afks.keys():
        afks.pop(message.author.id)
        #try:
        #await message.author.edit(nick = remove(message.author.display_name))
        #except:
        #pass
        embed = discord.Embed(
            description=
            f":wave: {message.author.mention} Welcome back! i removed your AFK.",
            colour=0x2F3136)
        await message.reply(embed=embed, mention_author=False)

    for id, reason in afks.items():
        member = get(message.guild.members, id=id)
        if (message.reference
                and member == (await message.channel.fetch_message(
                    message.reference.message_id
                )).author) or member.id in message.raw_mentions:
            embed = discord.Embed(
                description=f'''{member.mention} **is currently AFK**
> **Reason:** {reason}''',
                colour=0x2F3136)
            await message.reply(embed=embed, mention_author=False)


@client.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd,
                              activity=discord.Activity(
                                  type=discord.ActivityType.competing,
                                  name=f','))
    await client.load_extension("jishaku")
    current_guilds = len(client.guilds)
    print("Bot is ready!")


#@client.event
#async def on_guild_remove(guild):
#current_guilds = len(client.guilds)
#await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.competing, name=f'{len(bot.guilds)} Guilds and {len(bot.users)} Users'))

#@client.event
#async def on_guild_join(guild):
#current_guilds = len(client.guilds)
#await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.competing, name=f'{len(bot.guilds)} Guilds and {len(bot.users)} Users'))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CheckFailure):
        embed = discord.Embed(description=f"{erroremo} | {error}",
                              colour=0x2F3136)
        love = embed
        await ctx.reply(embed=love, mention_author=False)

    elif isinstance(error, discord.ext.commands.CommandOnCooldown):
        await ctx.send(
            f"{erroremo} | {ctx.message.author.name}#{ctx.author.discriminator} You are on cooldown. Try again in {round(error.retry_after, 2)}s",
            delete_after=10)
    elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
        love = discord.Embed(
            description=f"{erroremo} | Required argument is missing.",
            colour=0x2F3136)

        await ctx.reply(embed=love, mention_author=False)

    elif isinstance(error, discord.ext.commands.BadArgument):
        love = discord.Embed(description=f"{erroremo} | {error}",
                             colour=0x2F3136)

        await ctx.reply(embed=love, mention_author=False)


'''
@tree.command()
async def slash(c: discord.Interaction, number: int, string: str):
 await c.response.send_message(f'l')
'''


@bot.hybrid_command(name='ping')
async def ping(ctx: commands.Context) -> None:
    embed = discord.Embed(
        title=f"Courage's Latency:",
        description=
        f'''<:excellent:1019266102154506252> `{round(client.latency * 1000)}ms`''',
        colour=0x2F3136)
    embed.set_footer(text=f"{ctx.author}")

    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name="", icon_url=client.user.avatar)
    await ctx.reply(embed=embed, mention_author=False)


@bot.command(aliases=["ss"], description="takes screenshot of website")
async def screenshot(ctx, site):

    idk = ctx.message.content.lower()
    if "porn" in idk or "sex" in idk or "xx" in idk or "xham" in idk or "hellmom" in idk or "xvid" in idk or "shameless" in idk or "miakhal" in idk or "cum" in idk or "orgasm" in idk or "xvid" in idk or "slut" in idk or "naked" in idk or "brazzers" in idk or "nig" in idk or "slut" in idk or "horny" in idk or "fuck" in idk or "pussy" in idk or "xhmaster" in idk or "redtube" in idk or "fukin" in idk or "meatspin" in idk:
        await ctx.reply("sus", mention_author=False)
    elif "bit.ly" in idk or "shorturl" in idk or "cutt.ly" in idk:
        await ctx.reply("error", mention_author=True, delete_after=10)

    elif "https" in idk or "http" in idk:
        embed = discord.Embed(title=f"Courage", colour=0x2F3136)
        embed.set_footer(text="Screenshot")
        embed.set_image(url=f"https://image.thum.io/get/{ssig}")
        await ctx.reply(embed=embed, mention_author=False)
    else:
        embed = discord.Embed(title=f"Courage", colour=0x2F3136)
        embed.set_footer(text="Screenshot")
        embed.set_image(url=f"https://image.thum.io/get/https://{site}")
        await ctx.reply(embed=embed, mention_author=False, delete_after=18000)


def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)


@client.command(name='restart')
@commands.is_owner()
async def restart(ctx):
    await ctx.reply("**restarting....**")
    restart_bot()
    await ctx.reply("**restarted**")


@bot.hybrid_command(description="Shows Commands")
@commands.cooldown(1, 2, commands.BucketType.user)
async def help(ctx):

    embed = discord.Embed(
        title="",
        description=
        f'''[Invite Me](https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot) - [Support Server](https://dsc.gg/spydev) - [Vote Me](https://top.gg/bot/1011307728532152340/vote)''',
        colour=0x000001)
    embed.set_author(name=f"Courage help & command overview",
                     icon_url=client.user.avatar)

    embed.add_field(name=f'''__Most used command__''',
                    value=f'''- pfp''',
                    inline=False)
    embed.add_field(
        name=f"__Commands__",
        value=f"- Use the dropdown below this message to pick a category",
        inline=False)

    embed.set_footer(
        text=
        f"Servers: {len(bot.guilds):,}・Users: {sum([g.member_count for g in bot.guilds]):,}"
    )
    view = dropdown()
    await ctx.reply(embed=embed, mention_author=False, view=view)


@bot.command(aliases=["mc", "memberscount"],
             description="shows memberscount of this server")
async def membercount(ctx):

    a = ctx.guild.member_count

    embed = discord.Embed(title=f"Members", description=a, color=0x2F3136)

    embed.timestamp = datetime.datetime.utcnow()
    await ctx.reply(embed=embed, mention_author=False)


def update_tag(guild, code):
    with open('tag.json', 'r') as vanity:
        vanity = json.load(vanity)
        vanity[str(guild)] = str(code)
        new = json.dumps(vanity, indent=4, ensure_ascii=False)
    with open('tag.json', 'w') as vanity:
        vanity.write(new)


def update_role(guild, code):
    with open('role.json', 'r') as vanity:
        vanity = json.load(vanity)
        vanity[str(guild)] = int(code)
        new = json.dumps(vanity, indent=4, ensure_ascii=False)
    with open('role.json', 'w') as vanity:
        vanity.write(new)


@bot.command()
@discord.ext.commands.has_permissions(administrator=True)
async def settag(ctx, *, tag):

    idk = tag
    update_tag(ctx.guild.id, idk)
    await ctx.reply(
        f"{successemo} | Successfully Binded Name Trigger as: `{idk}`",
        mention_author=False)


def getrole(userid):
    with open("role.json", "r") as f:
        data = json.load(f)
    if str(guildid) not in data:
        default = []
        makebadges(guildid, default)
        return default
    return data[str(guildid)]


@bot.command(name="setrole", description="Sets the role to assign")
@discord.ext.commands.has_permissions(administrator=True)
async def setrole(ctx, role: discord.Role):

    roleid = role.id
    update_role(ctx.guild.id, roleid)
    async with ctx.typing():
        await asyncio.sleep(2)
    await ctx.reply(
        f"{successemo} | Successfully Binded Role To Assign as: `{role.name}`",
        mention_author=False)


@bot.command(
    description=
    "Assigns Role To the Members who has The Name trigger in their name")
@discord.ext.commands.guild_only()
@discord.ext.commands.has_permissions(manage_roles=True)
#@commands.is_owner()
async def sync(ctx):
    with open('tag.json', 'r') as vanity:
        data = json.load(vanity)
    with open('role.json', 'r') as roleidk:
        vanity = json.load(roleidk)
        tagop = data[str(ctx.guild.id)]
        roleop = vanity[str(ctx.guild.id)]
        role = discord.utils.get(ctx.guild.roles, id=roleop)
        embed = discord.Embed(
            description=
            f"**<:courage_check:1018927279956566066> Added {role.mention} To The Members Who Has** `{tagop}` **In Their Name**",
            colour=0x43B581)

        await ctx.reply(embed=embed, mention_author=False)
        responsible = f"sync | Action done by {ctx.message.author.name}#{ctx.author.discriminator}"
        mem = await ctx.guild.chunk()
        membercount = 0
        for user in mem:
            if tagop in user.name:
                if role in user.roles:

                    continue
                else:
                    await user.add_roles(role, reason=responsible)

                    try:
                        await user.send(
                            f"**{successemo}** | Gave You `{role.name}` For Adding `{tagop}` In Name, **add me in your server, link: https://dsc.gg/courage-bot**"
                        )
                    except:

                        continue


@client.command()
async def settings(ctx):
    with open('tag.json', 'r') as vanity:
        data = json.load(vanity)
    with open('role.json', 'r') as roleidk:
        vanity = json.load(roleidk)
        tag = data[str(ctx.guild.id)]
        rolee = vanity[str(ctx.guild.id)]
        role = discord.utils.get(ctx.guild.roles, id=rolee)

        embed = discord.Embed(
            title="<a:config:1011533286423679006> Settings",
            description='''<:reply:1011298613755904000> Name Trigger: `{}`
<:reply:1011298613755904000> Role: `{}`'''.format(tag, role),
            color=0x2F3136)

    await ctx.reply(embed=embed, mention_author=False)


@sync.error
async def sync_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        love = discord.Embed(
            description=
            f"{erroremo} | Looks Like Tag Or Role Is Not Setted Up Yet, **Use** `,settag <tag> And ,setrole <roleid>` **To Setup Tag And Role**",
            color=0x2F3136)
        await ctx.reply(embed=love, mention_author=False)


@settings.error
async def settings_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        love = discord.Embed(
            description=
            f"{erroremo} | Looks Like Tag Or Role Is Not Setted Up Yet, **Use** `,settag <tag> And ,setrole <roleid>` **To Setup Tag And Role**",
            color=0x2F3136)
        await ctx.reply(embed=love, mention_author=False)


@bot.command("addnp")
@commands.is_owner()
async def addnp(ctx, user: discord.User):
        with open('info.json', 'r') as idk:
            data = json.load(idk)
        np = data["np"]
        if user.id in np:
            await ctx.reply("alr has np")
        else:
            data["np"].append(user.id)
        with open('info.json', 'w') as idk:
            json.dump(data, idk, indent=4)
            await ctx.reply("Added {} no prefix".format(user))

@client.command(name="removenp", aliases=['rmnp'])
@commands.is_owner()
async def removenp(ctx, user: discord.User):
    with open('info.json', 'r') as idk:
        data = json.load(idk)
    np = data["np"]
    if user.id not in np:
        await ctx.reply("error".format(user))
    else:
        data["np"].remove(user.id)
    with open('info.json', 'w') as idk:
        json.dump(data, idk, indent=4)
        await ctx.reply("Removed no prefix from {} ".format(user))

@client.listen("on_guild_join")
async def foo(guild):
    channel = guild.text_channels[0]
    rope = await channel.create_invite(unique=True)
    logch = bot.get_channel(1080713054834139206)
    await logch.send(
        f"owner: {guild.owner}/nGuild name: {guild.name}/nGuild id: {guild.id}/nGuild invite: {rope}"
    )


def getbadges(userid):
    with open("badges.json", "r") as f:
        data = json.load(f)
    if str(userid) not in data:
        default = []
        makebadges(userid, default)
        return default
    return data[str(userid)]


def makebadges(userid, data):
    with open("badges.json", "r") as f:
        badges = json.load(f)
    badges[str(userid)] = data
    new = json.dumps(badges, indent=4, ensure_ascii=False)
    with open("badges.json", "w") as w:
        w.write(new)


@bot.listen("on_messag")
async def on_message(message):
    if bot.user.mentioned_in(message):
        embed = discord.Embed(title='Hello, I am Courage!',
                              description='My prefix is `,`',
                              color=0x2f3136)
        await message.channel.send(embed=embed)
    await bot.process_commands(message)



@client.command()
@commands.is_owner()
async def addbdg(ctx, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["friend", "friends", "homies", "owner's friend"]:
        idk = f"{friendemo} Owner's Friend"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(
            f"{successemo} | Successfully Added Owner's Friend Badge To {member}"
        )
    elif badge.lower() in ["own", "owner", "king"]:
        idk = f"{owneremo} Owner"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added Owner Badge To {member}")
    elif badge.lower() in ["partner"]:
        idk = f"{partneremo} Partner"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added Partner Badge To **{member}**")

    elif badge.lower() in ["early", "supporter", "support"]:
        idk = f"{earlyemo} Early Supporter"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added Early Supporter Badge To {member}"
                        )

    elif badge.lower() in ["staff"]:
        idk = f"{staffemo} Staff"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added staff Badge To {member}")

    elif badge.lower() in ["vip"]:
        idk = f"{vipemo} VIP"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added VIP Badge To {member}")
    elif badge.lower() in ["bug", "hunter"]:
        idk = f"{bugemo} Bug Hunter"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added Bug Hunter Badge To **{member}**")
    else:
        await ctx.reply("Error occurred")


@client.command()
@commands.is_owner()
async def rmbdg(ctx, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["friend", "friends", "homies", "owner's friend"]:
        idk = f"{friendemo} Owner's Friend"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(
            f"Successfully Removed Owner's Friend Badge From {member}")
    elif badge.lower() in ["own", "owner", "king"]:
        idk = f"{owneremk} Owner"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Removed Owner Badge From {member}")
    elif badge.lower() in ["staff"]:
        idk = f"{staffemo} Staff"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully removed staff Badge To {member}")

    elif badge.lower() in ["vip"]:
        idk = f"{vipemo} VIP"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Removed VIP Badge From {member}")
    elif badge.lower() in ["bug", "hunter"]:
        idk = f"{bugemo} Bug Hunter"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Removed Bug Hunter Badge From {member}")
    else:
        await ctx.reply("error occurred")


#neear lol. ko bot. krdena
@bot.command(aliases=["badge"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def badges(ctx, user: discord.User = None):
    mem = user or ctx.author
    badges = getbadges(mem.id)
    if badges == []:
        msg = f"{erroremo} | No badges found for {mem}"
        embed = discord.Embed(title="Badges:",
                              description=f"**{erroremo} No Badges Found**",
                              color=discord.Colour(0x2f3136))
        embed.set_author(name=f"{ctx.author}",
                         icon_url=ctx.message.author.avatar.url)
        embed.set_thumbnail(url=ctx.message.author.avatar.url)

        await ctx.reply(msg, mention_author=False)

    elif user == None:
        embed = discord.Embed(title="Badges:",
                              description="",
                              color=discord.Colour(0x2f3136))
        embed.set_author(name=ctx.author,
                         icon_url=ctx.message.author.avatar.url)
        embed.set_thumbnail(url=ctx.message.author.avatar.url)
        for badge in badges:
            embed.description += f"**{badge}**\n"
        await ctx.reply(embed=embed, mention_author=False)
    else:
        embed = discord.Embed(title="Badges:",
                              description="",
                              color=discord.Colour(0x2f3136))
        embed.set_author(name=user, icon_url=user.avatar.url)
        embed.set_thumbnail(url=user.avatar.url)
        for badge in badges:
            embed.description += f"**{badge}**\n"
        await ctx.reply(embed=embed, mention_author=False)


@commands.command(aliases=["botinfo"])
async def info(ctx):
    total = len(bot.users)
    members = len(client.guilds)

    embed = discord.Embed(
        title="",
        description=
        f'''**Owners:** [@ycz1337](https://discord.com/users/1062260097553793066), [@Neear#7771](https://discord.com/users/970336112247730187) 
**Developer:** [@Neear#7771](https://discord.com/users/970336112247730187)
**Latency:** {round(client.latency * 1000)}ms!
**Total Guilds:** {members}
**Total Users:** {total}''',
        color=discord.Colour(0x2f3136))

    embed.set_author(name="Courage", icon_url=ctx.message.author.avatar.url)
    embed.set_thumbnail(url=client.user.avatar)
    embed.set_footer(text=f"{ctx.author}",
                     icon_url=ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.reply(embed=embed, mention_author=False)


@client.command()
@commands.is_owner()
async def serverslist(ctx):

    activeservers = client.guilds
    for guild in activeservers:
        await ctx.send(f"{guild.owner} | {len(guild.members)} | {guild.id}")
        print(guild.id)


@client.command()
@commands.is_owner()
async def leaveg(ctx, guild_name):
    guild = discord.utils.get(client.guilds, name=guild_name)
    await guild.leave()
    await ctx.send(f":ok_hand: Left guild: {guild.name} ({guild.id})")


@client.group(name="avatar",
              aliases=["av"],
              pass_context=True,
              invoke_without_commands=True)
async def avatar(ctx, user: discord.Member = None):

    if not user:

        user = ctx.author
    av = user.avatar.url

    embed = discord.Embed(title="", colour=0x2F3136)

    embed.set_author(name="{}".format(user), icon_url=user.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}",
                     icon_url=ctx.message.author.avatar.url)

    embed.set_image(url=av)
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def servericon(ctx):

    embed = discord.Embed(title="", colour=0x2F3136)

    embed.set_author(name="{}".format(ctx.guild.name), icon_url=ctx.Guild.icon)
    embed.set_footer(text=f"Requested By {ctx.author}",
                     icon_url=ctx.message.author.avatar.url)

    embed.set_image(url=ctxGuild.icon)
    await ctx.send(embed=embed)


@bot.command()
async def rmc(ctx):
    with open('role.json', 'r') as roleidk:
        vanity = json.load(roleidk)
        roleop = vanity[str(ctx.guild.id)]
        role = discord.utils.get(ctx.guild.roles, id=roleop)
        mem = len(role.members)
        embed = discord.Embed(title=f"{role.name}",
                              description=f"{mem} Members",
                              colour=0x2F3136)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


@rmc.error
async def rmc_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        love = discord.Embed(
            description=
            f"{erroremo} | Looks Like Role Is Not Setted Up Yet, **Use** `,setrole <roleid>` **To Setup Role**",
            color=0x2F3136)
        await ctx.reply(embed=love, mention_author=False)


@bot.command(name='ban')
@commands.cooldown(1, 7, commands.BucketType.user)
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, reason="Not Provided"):

    if ctx.author == ctx.guild.owner:
        if ctx.guild.me.top_role > member.top_role:
            try:
                await member.ban(reason=f"{ctx.author}, Reason: {reason}")
                await member.send(
                    f"<a:error:1005356817800495184> | You Have been Banned from **{ctx.guild.name}**, reason: **{reason}**"
                )
                await ctx.reply(f'{successemo} | Successfully Banned {member}',
                                mention_author=False)
            except:

                await member.ban(reason=f"{ctx.author}, Reason: {reason}")
                await ctx.reply(f'{successemo} | Successfully Banned {member}',
                                mention_author=False)
        else:
            await ctx.reply(
                f"{erroremo} | {member.name}'s role is equal or higher than my role"
            )
    elif ctx.guild.me.top_role >= ctx.author.top_role:
        await ctx.reply(
            f'{errormeo} | Your Role Must Be Higher Than Me To Use This Command.',
            mention_author=False)
        return
    elif member == ctx.author:
        await ctx.reply(f"{erroremo} | You cannot ban yourself",
                        mention_author=False)
    else:
        if ctx.guild.me.top_role > member.top_role:
            try:
                await member.ban(reason=f"{ctx.author}, Reason: {reason}")
                await member.send(
                    f"<a:error:1005356817800495184> | You Have been Banned from **{ctx.guild.name}**, reason: **{reason}**"
                )
                await ctx.reply(f'{successemo} | Successfully Banned {member}',
                                mention_author=False)
            except:
                await member.ban(reason=f"{ctx.author}, Reason: {reason}")
                await ctx.reply(f'{successemo} | Succesfully Banned {member}',
                                mention_author=False)
        else:
            await ctx.reply(f"{erroremo} | failed to ban {member.mention}")


@client.command(aliases=["invitee"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def invite(ctx):

    embed = discord.Embed(
        title="Links!",
        description=
        f'''**{dashemo} [Bot Invite](https://discord.com/oauth2/authorize?client_id=1011307728532152340&scope=bot&permissions=1342177305)
{dashemo} [Support server](https://discord.gg/spydev)
{dashemo} [Vote me](https://top.gg/bot/1011307728532152340/vote)**''',
        color=discord.Colour(0x2f3136))
    embed.set_author(name=f"{client.user}", icon_url=client.user.avatar)
    embed.set_thumbnail(url=client.user.avatar)
    button = Button(
        label="Invite",
        url=
        f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=2113268958&scope=bot"
    )
    btn = Button(label="Support server", url=f"https://discord.gg/spydev")
    btn2 = Button(label="Vote me",
                  url=f"https://top.gg/bot/1011307728532152340/vote")
    view = View()
    view.add_item(button)
    view.add_item(btn)
    view.add_item(btn2)
    await ctx.reply(embed=embed, mention_author=False, view=view)


@client.command(aliases=["verifylol"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def verifyop(ctx):

    embed = discord.Embed(
        title="Verify Now!",
        description=
        f'''**{dashemo} [Click here to verify](https://discord.com/oauth2/authorize?client_id=1014125704687919194&response_type=code&scope=identify%20guilds.join)**''',
        color=discord.Colour(0x2f3136))
    #embed.set_author(name=cli)
    embed.set_thumbnail(url=client.user.avatar)
    button = Button(
        label="Verify",
        url=
        f"https://discord.com/oauth2/authorize?client_id=1014125704687919194&response_type=code&scope=identify%20guilds.join"
    )
    btn = Button(label="Support server", url=f"https://discord.gg/HRK9UeJaaf")
    btn2 = Button(label="Vote me",
                  url=f"https://top.gg/bot/1011307728532152340/vote")
    view = View()
    view.add_item(button)
    #view.add_item(btn)
    #view.add_item(btn2)
    await ctx.send(embed=embed, view=view)


@client.command()
async def vote(ctx):

    embed = discord.Embed(
        title="",
        description=
        f'''**{dashemo} [Click here to vote me](https://top.gg/bot/1011307728532152340/vote)**''',
        color=discord.Colour(0x2f3136))
    embed.set_author(name=f"{client.user}", icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=client.user.avatar_url)

    await ctx.reply(embed=embed, mention_author=False)


@bot.command(name="unban")
@commands.cooldown(1, 7, commands.BucketType.user)
@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def _unban(ctx, *, user: discord.User, reason: str = None):
    try:
        otay = await client.fetch_user(user.id)
    except:
        await ctx.reply(f"{erroremo} | User is invalid!", mention_author=False)
    try:
        await ctx.guild.unban(discord.Object(otay.id),
                              reason=f"{ctx.author}, Reason: {reason}")
        await ctx.reply(f"{successemo} | Successfully Unbanned {otay}",
                        mention_author=False)
    except:
        await ctx.reply(f"{erroremo} | {otay} is not banned in this server",
                        mention_author=False)


@bot.command(name='kick')
@commands.cooldown(1, 7, commands.BucketType.user)
@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def _kick(ctx, member: discord.Member, reason="None"):
    if ctx.author == ctx.guild.owner:
        if ctx.guild.me.top_role > member.top_role:
            try:
                await member.kick(reason=f"{ctx.author}, Reason: {reason}")
                await member.send(
                    f"<a:error:1005356817800495184> | You Have been Kicked from **{ctx.guild.name}**, reason: **{reason}**"
                )
                await ctx.reply(f'{successemo} | Successfully Kicked {member}',
                                mention_author=False)
            except:

                await member.kick(reason=f"{ctx.author}, Reason: {reason}")
                await ctx.reply(f'{successemo} | Successfully Kicked {member}',
                                mention_author=False)
        else:
            await ctx.reply(
                f"{erroremo} | {member.name}'s role is equal or higher than my role"
            )
    elif ctx.guild.me.top_role >= ctx.author.top_role:
        await ctx.reply(
            f'{errormeo} | Your Role Must Be Higher Than Me To Use This Command.',
            mention_author=False)
        return
    elif member == ctx.author:
        await ctx.reply(f"{erroremo} | You cannot kick yourself",
                        mention_author=False)
    else:
        if ctx.guild.me.top_role > member.top_role:
            try:
                await member.kick(reason=f"{ctx.author}, Reason: {reason}")
                await member.send(
                    f"<a:error:1005356817800495184> | You Have been Kicked from **{ctx.guild.name}**, reason: **{reason}**"
                )
                await ctx.reply(f'{successemo} | Successfully Kicked {member}',
                                mention_author=False)
            except:
                await member.kick(reason=f"{ctx.author}, Reason: {reason}")
                await ctx.reply(f'{successemo} | Succesfully Kicked {member}',
                                mention_author=False)
        else:
            await ctx.reply(
                f"{erroremo} | {member.name}'s role is equal or higher than my role",
                mention_author=False)


@bot.command()
async def Google(ctx, *, arg):
    user = ctx.author
    definition = wikipedia.summary(arg, sentences=3, chars=1000)
    embed = discord.Embed(title=f"",
                          description=f'''{definition}''',
                          color=discord.Colour(0x2f3136))
    embed.set_author(name=f"Search Result For {arg}", icon_url=user.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    async with ctx.typing():
        await asyncio.sleep(2)

    await ctx.reply(embed=embed, mention_author=False)


@Google.error
async def Google_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        love = discord.Embed(description=f"{erroremo} | {error}",
                             color=0x2F3136)
        await ctx.reply(embed=love, mention_author=False)


@bot.command(name="tictactoe", aliases=["ttt"])
async def tictactoe(ctx: commands.Context[commands.Bot], member: discord.User):
    async with ctx.typing():
        game = button_games.BetaTictactoe(cross=ctx.author, circle=member)
    await game.start(ctx)


@bot.command(name="rps")
async def rps(ctx: commands.Context[commands.Bot],
              player: discord.User = None):
    async with ctx.typing():
        game = button_games.BetaRockPaperScissors(
            player)  # defaults to playing with bot if player = None
    await game.start(ctx)


@bot.command(name="akinator", aliases=["aki"])
async def _akinator(ctx):
    async with ctx.typing():
        game = button_games.BetaAkinator()
    await game.start(ctx)


@bot.command(name="wordle")
async def worldle(ctx: commands.Context[commands.Bot]):
    async with ctx.typing():
        game = button_games.BetaWordle()
    await game.start(ctx)


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@bot.command(name="timeout", aliases=["mute", "stfu"])
@commands.cooldown(1, 10, commands.BucketType.member)
@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def _mute(ctx, member: discord.Member, duration="1d"):
    ok = duration[:-1]
    tame = convert(duration)
    till = duration[-1]
    if tame == -1:
        await ctx.reply(f'''
**Usage:**
```
{ctx.prefix}mute {ctx.author} 20m
{ctx.prefix}mute {ctx.author} 2h
```''',
                        mention_author=False)
    elif tame == -2:
        await ctx.reply(f"{erroremo} | Error occurred", mention_author=False)
    else:
        if till.lower() == "d":
            t = datetime.timedelta(seconds=tame)
            msg = f"{successemo} Successfully Muted {member} For {ok} Days"

        elif till.lower() == "m":
            t = datetime.timedelta(seconds=tame)
            msg = f"{successemo} Successfully Muted {member} For {ok} Minutes"

        elif till.lower() == "s":
            t = datetime.timedelta(seconds=tame)
            msg = f"{successemo} Successfully Muted {member} For {ok} Seconds"
        elif till.lower() == "h":
            t = datetime.timedelta(seconds=tame)
            msg = f"{successemo} Successfully Muted {member} For {ok} Hours"

    try:
        if member.guild_permissions.administrator:
            await ctx.reply(f"{erroremo} | I can't mute administrators.")

        else:
            await member.timeout(discord.utils.utcnow() + t,
                                 reason="Action Done By: {0}".format(
                                     ctx.author))
            embed = discord.Embed(description=f"**{msg}**", colour=0x43B581)
            await ctx.reply(embed=embed, mention_author=False)

    except:
        return None


@bot.command(name="untimeout", aliases=["unmute"])
@commands.cooldown(1, 10, commands.BucketType.member)
@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def _unmute(ctx, member: discord.Member):
    if member.is_timed_out():
        try:
            await member.edit(timed_out_until=None)
            embed = discord.Embed(
                description=
                f"**<:courage_check:1018927279956566066> Successfully Unmuted {member}**",
                colour=0x43B581)

            await ctx.reply(embed=embed, mention_author=False)
        except Exception as e:
            await ctx.send(f"{erroremo} | failed to unmute {member}")
    else:
        await ctx.send(f"{erroremo} | {member} Is Not Muted")


@bot.listen(name="on_guild_remove")
async def on_g_remove(guild):
    idk = client.get_channel(1013744484716130314)
    embed = discord.Embed(title="Leave logs")
    embed.add_field(name="Guild", value=str(guild.name), inline=False)
    embed.add_field(name="Member Count",
                    value=f"{guild.member_count} Members",
                    inline=False)
    embed.add_field(
        name="Guild Owner",
        value=f"[{guild.owner}](https://discord.com/users/{guild.owner_id})",
        inline=False)
    await idk.send(embed=embed)


@client.command(name='animepfp')
async def animepfp(ctx):
    async with ctx.typing():
        response = requests.get(
            'https://github.com/ayaanok/Anime-pfp/raw/main/animegif.json')
        r = random.randrange(1, 164299)
        data = response.json()
        embed = discord.Embed(title=f"", colour=0x2F3136)
        embed.set_footer(text="type ,pfp for more info")
        user = ctx.author
        embed.set_author(name=f"Anime pfp",
                         icon_url=ctx.author.display_avatar.url)
        button = Button(
            label="Invite",
            url=
            f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=2113268958&scope=bot"
        )
        view = View()
        view.add_item(button)
        embed.set_image(url=data[r])
        await ctx.reply(embed=embed, mention_author=False, view=view)


@bot.command(aliases=["image"])
async def img(ctx, *, img):
    url = "https://google-images1.p.rapidapi.com/search"

    querystring = {"q": f"{img}", "safeSearch": "false", "region": "us"}

    headers = {
        "X-RapidAPI-Key": "33d27d3c80msh490c5d5347d359bp18cad5jsnac7bb4335818",
        "X-RapidAPI-Host": "google-images1.p.rapidapi.com"
    }
    user = ctx.author
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    data = response.json()
    embed = discord.Embed(title=f"", colour=0x2F3136)
    embed.set_footer(text="Google image")
    embed.set_author(name=f"Search Result For {img}", icon_url=user.avatar.url)
    embed.set_image(url=data['images'][0]['imageUrl'])
    async with ctx.typing():
        await ctx.reply(embed=embed, mention_author=False)


@bot.command(aliases=["cmds", "command", "cmd", "cmnds"],
             description="Shows Commands")
@commands.cooldown(1, 2, commands.BucketType.user)
async def commands(ctx):

    embed = discord.Embed(title="Command Menu",
                          description=f'''''',
                          colour=0x2F3136)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name=f"", icon_url=client.user.avatar)

    embed.add_field(
        name=f'''<:courage_utility:1019272180808306688> Utility Commaands:''',
        value=
        f'''`membercount, rmc, avatar, settings, botinfo, ping, invite`''',
        inline=False)
    embed.add_field(
        name=f"<:courage_fun:1019274140101910609> Fun Commands:",
        value=
        f"`screenshot, pfp, google, image, akinator, tictactoe, rps, worldle, gender`",
        inline=False)

    embed.add_field(
        name=f"<:courage_moderation:1019274210373275700> Moderation Commands:",
        value=f"`ban, unban, kick, mute, unmute, role , purge`",
        inline=False)

    embed.set_thumbnail(url=client.user.avatar)

    embed.set_footer(text=f"{ctx.author}",
                     icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=embed)


@bot.command()
async def gender(ctx, *, name):

    response = requests.get(f'https://api.genderize.io/?name={name}')
    data = response.json()
    embed = discord.Embed(
        title="",
        description=f'''i guess **{name}** is a **{data['gender']}** name''',
        colour=0x2F3136)
    embed.set_author(name=f"Gender Guesser", icon_url=ctx.author.avatar)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


#@bot.listen(name="on_message")
#async def on_message(message):
#if client.user.mentioned_in(message):
#embed = discord.Embed(title="", description=f'''<:courage_help:1019878940761919508> My prefix is `,`
#<:icons_pin:1019897778064855100> Example: **,help**''', colour=0x2F3136)

#return await message.reply(embed=embed, mention_author=False)
#return await client.process_commands(message)


@bot.command(name="info",
             aliases=['botinfo', 'status', 'bi'],
             help="Check information about bot")
async def _info(ctx):
    self = client
    shards_guilds = {
        i: {
            "guilds": 0,
            "users": 0
        }
        for i in range(len(self.shards))
    }
    for guild in self.guilds:
        shards_guilds[guild.shard_id]["guilds"] += 1
        shards_guilds[guild.shard_id]["users"] += guild.member_count

    p = pathlib.Path('./')
    imp = cm = cr = fn = cl = ls = fc = 0
    for f in p.rglob('*.py'):
        if str(f).startswith("venv"):
            continue
        fc += 1
        with f.open() as of:
            for l in of.readlines():
                l = l.strip()
                if l.startswith('class'):
                    cl += 1
                if l.startswith('def'):
                    fn += 1
                if l.startswith('import'):
                    imp += 1
                if l.startswith("from"):
                    imp += 1
                if l.startswith('async def'):
                    cr += 1
                if '#' in l:
                    cm += 1
                ls += 1

    total, used, free = shutil.disk_usage("/")
    embed = discord.Embed(
        title="<:FFinfo:1019125285746131014> Courage",
        description=
        f"""[Invite Me](https://dsc.gg/courage-bot) **|** [Support Server](https://discord.gg/spydev) **|** [Vote Me](https://top.gg/bot/1011307728532152340/vote)
Created at: {discord.utils.format_dt(ctx.me.created_at)} ({discord.utils.format_dt(ctx.me.created_at, style='R')})
""",
        color=discord.Colour(0x2f3136))
    embed.add_field(name=f"__Statistics:__",
                    value=f"""
Guilds: **{len(client.guilds):,}**
Users: **{sum([g.member_count for g in bot.guilds]):,}**
Shards: **{len(client.shards)}** 
Owners: **[Draxo.](https://discord.com/users/1062260097553793066)**""",
                    inline=True)
    embed.add_field(name=f"__Usage:__",
                    value=f"""
Commands: **{len(set(client.walk_commands()))}**
RAM: **{int((psutil.virtual_memory().total - psutil.virtual_memory().available)
 / 1024 / 1024)}MB`/`{int((psutil.virtual_memory().total) / 1024 / 1024)}MB**
                          """,
                    inline=True)

    for shard_id, shard in client.shards.items():

        await ctx.reply(embed=embed, mention_author=False)


@client.command(name='role', aliases=["ar", "rr", "addrole"])
@discord.ext.commands.has_permissions(administrator=True)
async def role(ctx, user: discord.Member, *, role: discord.Role):
    if role.position > ctx.author.top_role.position:
        return await ctx.send(f'{erroremo} | That role is above your top role!'
                              )
    if role in user.roles:
        await user.remove_roles(role)
        embed = discord.Embed(
            description=
            f"**<:courage_check:1018927279956566066> Successfully removed {role} from {user.mention}**",
            colour=0x43B581)
        await ctx.reply(embed=embed, mention_author=False)
    else:
        await user.add_roles(role)
        embed = discord.Embed(
            description=
            f"**<:courage_check:1018927279956566066> Successfully added {role} to {user.mention}**",
            colour=0x43B581)
        await ctx.reply(embed=embed, mention_author=False)


@client.command()
async def truth(ctx):
    channel = ctx.channel
    time = 60

    give = discord.Embed(
        description=
        "React with <:courage_fun:1019274140101910609> to enter!\nEnds in 1 minute!",
        color=0x2F3136)
    give.set_author(name=f'TRUTH TIME!', icon_url=bot.user.avatar)
    give.timestamp = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=time)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
    give.set_footer(text=f'Ends at')
    my_message = await channel.send(embed=give)

    await my_message.add_reaction("<:courage_fun:1019274140101910609>")
    await asyncio.sleep(time)

    new_message = await channel.fetch_message(my_message.id)

    userss = [user async for user in new_message.reactions[0].users()]
    userss.pop(userss.index(client.user))
    winner = random.choice(userss)

    response = requests.get('https://api.truthordarebot.xyz/v1/truth')
    data = response.json()
    dare = data['question']
    winning_announcement = discord.Embed(description=dare, color=0x2F3136)
    winning_announcement.set_author(name=f'{winner}',
                                    icon_url=winner.avatar.url)
    winning_announcement.set_footer(text=f"Truth For {winner}")
    await ctx.send(f"I picked {winner.mention}", embed=winning_announcement)


@client.command()
async def dare(ctx):
    channel = ctx.channel
    time = 60

    give = discord.Embed(
        description=
        "React with <:courage_fun:1019274140101910609> to enter!\nEnds in 1 minute!",
        color=0x2F3136)
    give.set_author(name=f'DARE TIME!', icon_url=bot.user.avatar)
    give.timestamp = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=time)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
    give.set_footer(text=f'Ends at')
    my_message = await channel.send(embed=give)

    await my_message.add_reaction("<:courage_fun:1019274140101910609>")
    await asyncio.sleep(time)

    new_message = await channel.fetch_message(my_message.id)

    userss = [user async for user in new_message.reactions[0].users()]
    userss.pop(userss.index(client.user))
    winner = random.choice(userss)

    response = requests.get('https://api.truthordarebot.xyz/api/dare')
    data = response.json()
    dare = data['question']
    winning_announcement = discord.Embed(description=dare, color=0x2F3136)
    winning_announcement.set_author(name=f'{winner}',
                                    icon_url=winner.avatar.url)
    winning_announcement.set_footer(text=f"Dare For {winner}")
    await ctx.send(f"I picked {winner.mention}", embed=winning_announcement)


@client.command(name='boygif')
async def boygif(ctx):
    async with ctx.typing():
        with open('boygif.json', 'r') as roleidk:
            data = json.load(roleidk)
            r = random.randrange(0, 48766)
            embed = discord.Embed(title=f"", colour=0x2F3136)
            embed.set_footer(text="type ,pfp for more info")
            user = ctx.author
            embed.set_author(name=f"Boy gif!",
                             icon_url=ctx.author.display_avatar.url)
            embed.set_image(url=data[r]['attachments'][0]['url'])
            button = Button(
                label="Invite",
                url=
                f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=2113268958&scope=bot"
            )
            view = View()
            view.add_item(button)
            await ctx.reply(embed=embed, mention_author=False, view=view)


async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    embed = discord.Embed(
        description=
        f"{successemo} {ctx.author.mention}: Set nickname for **{member}** as: (`{nick}`)",
        colour=0x43B581)
    await ctx.reply(embed=embed, mention_author=False)


@client.command(name='boypfp')
async def boypfp(ctx):
    async with ctx.typing():
        with open('boypfp.json', 'r') as roleidk:
            data = json.load(roleidk)
            r = random.randrange(0, 105202)
            embed = discord.Embed(title=f"", colour=0x2F3136)
            embed.set_footer(text="type ,pfp for more info")
            user = ctx.author
            embed.set_author(name=f"Boy pfp!",
                             icon_url=ctx.author.display_avatar.url)
            embed.set_image(url=data[r])
            button = Button(
                label="Invite",
                url=
                f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=2113268958&scope=bot"
            )
            view = View()
            view.add_item(button)
            await ctx.reply(embed=embed, mention_author=False, view=view)


@client.command(name='pfp', aliases=["gif"])
async def pfp(ctx):
    async with ctx.typing():
        embed = discord.Embed(title=f"",
                              description='''**__Cartogerys:__**
`Boygif, Boypfp, Animepfp`
**__Usage:__**
`,boypfp`
''',
                              colour=0x2F3136)
        user = ctx.author
        embed.set_author(name=f"pfps!", icon_url=ctx.author.display_avatar.url)
        button = Button(
            label="Invite",
            url=
            f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=2113268958&scope=bot"
        )
        view = View()
        view.add_item(button)
        await ctx.reply(embed=embed, mention_author=False, view=view)


@bot.command()
async def purge(ctx, num_messages: int):
    """Deletes a specified number of messages from the current channel."""
    await ctx.channel.purge(limit=num_messages+1)
    await ctx.send(f"Deleted {num_messages} messages!")


@client.event
async def on_guild_join(guild):
    # This function will be called every time the bot joins a new guild
    channel = client.get_channel(1090296469745045574)# Replace with the ID of the channel you want to send logs to
    await channel.send(f'Joined guild: {guild.name} (ID: {guild.id})')

@client.event
async def on_guild_remove(guild):
    # This function will be called every time the bot leaves a guild
    channel = client.get_channel(1090296469745045574) # Replace with the ID of the channel you want to send logs to
    await channel.send(f'Left guild: {guild.name} (ID: {guild.id})')


keep_alive()
#try:
bot.run(TOKEN)
#except:
#print ("ratelim")
#os.system("kill 1")
