from logging.handlers import RotatingFileHandler
import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists('logger/logs'):
    os.makedirs('logger/logs')

# Configure logger
logger = logging.getLogger("TelegramBot")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)

# File handler
file_handler = RotatingFileHandler(
    'logger/logs/bot.log',
    maxBytes=5 * 1024 * 1024,  # 5MB
    backupCount=5,
    encoding='utf-8'
)
file_handler.setLevel(logging.INFO)
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler) 
