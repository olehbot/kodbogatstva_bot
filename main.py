import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

async def send_post():
    bot = Bot(token=BOT_TOKEN)
    message = "🔥 Это автоматический пост! Скоро здесь начнутся посты для твоего роста"
    await bot.send_message(chat_id=CHANNEL_USERNAME, text=message)

if name == "__main__":
    asyncio.run(send_post())
