import discord
from discord import channel
from discord.client import Client
import dotenv
import requests
import json
import requests
import os
from requests.api import head
from requests.structures import CaseInsensitiveDict
from os.path import join, dirname
from dotenv import load_dotenv 
from os import system
from discord.ext import commands
prefix=os.getenv('PREFIX')
token = os.getenv('TOKEN')
secret_key = os.getenv('API_KEY')
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


@bot.event
async def on_ready():
    print('-------')
    print('Online')
    print('-------')



@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="-_-", description="You are using that command wrong, please retry with the correct roles or arguments.")
    embed.set_footer(text="-skeet")
    await ctx.send(embed=embed)
    print(error)


@bot.command()
async def list(ctx):
    order = "https://dev.sellix.io/v1/orders"
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    print (secret_key)
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    head= 'Bearer '+secret_key
    headers["Authorization"] =  head
    resp = requests.get(order, headers=headers)
    output = resp.text
    parsed = json.loads(output)
    file="all.json"
    o = open(file,"w")
    o.write(json.dumps(parsed, indent=2))
    #print (json.dumps(parsed, indent=2))
    await ctx.send(file=discord.File(file))

@bot.command()
async def order(ctx,description):
    order = "https://dev.sellix.io/v1/orders/" + description
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    secret_key = os.getenv('API_KEY')
    print (secret_key)
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    head= 'Bearer '+secret_key
    headers["Authorization"] =  head
    resp = requests.get(order, headers=headers)
    output = resp.text
    parsed = json.loads(output)
    file ="order " + description
    o = open(file,"w")
    o.write(json.dumps(parsed, indent=2))
    print(description)
    await ctx.send(file=discord.File(file))
bot.run(token)
