from config.settings import API_ID, API_HASH, BOT_TOKEN
from bot.handlers import register_handlers
from bot.tasks import register_tasks

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

tasks_app = AsyncIOScheduler()

if __name__ == "__main__":
    register_tasks(app, tasks_app)
    register_handlers(app)
    tasks_app.start()
    app.run()