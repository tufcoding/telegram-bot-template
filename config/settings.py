from dotenv import load_dotenv
import os

load_dotenv()

# Bot configuration
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Database configuration
DATABASE_URL = "sqlite:///bot.db"