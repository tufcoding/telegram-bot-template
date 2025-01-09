from bot.commands.commands import get_bot_commands
from logger.logger import logger

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from pyrogram import Client
import asyncio

def register_tasks(app: Client, tasks_app: AsyncIOScheduler):
    async def on_startup():
        while True:
            try:
                await app.set_bot_commands(await get_bot_commands())
            except Exception:
                await asyncio.sleep(1)
                continue
            break
        
        bot_name = (await app.get_me()).username
        logger.info(f"{bot_name} is running!")

    tasks_app.add_job(on_startup, 'date', run_date=datetime.now())