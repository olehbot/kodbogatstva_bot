import os
import telegram
import asyncio
from datetime import datetime

BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_USERNAME = os.environ['CHANNEL_USERNAME']

bot = telegram.Bot(token=BOT_TOKEN)

async def send_post():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"🔥 Это автоматический пост от {now}\n\nСкоро здесь начнутся посты для твоего роста 💼"
    await bot.send_message(chat_id=CHANNEL_USERNAME, text=message)

if name == '__main__':
    asyncio.run(send_post())
