import requests

from MyTgBot import bot
from pyrogram import filters

BOT_ID = (6005606875)

@bot.on_message(filters.text, group=200)
async def chatbot(_, message):
          if message.reply_to_message.from_user.id == BOT_ID:
               Message = message.text
               API = requests.get("https://kora-api.vercel.app/chatbot/2d94e37d-937f-4d28-9196-bd5552cac68b/Serena/Anonymous/message="+Message).json()
               await message.reply(API["reply"])