# 🤖 Telegram Bot Template

A clean and scalable Telegram bot template using [Pyrotgfork](https://github.com/TelegramPlayGround/Pyrogram) (a forked version of [Pyrogram](https://github.com/pyrogram/pyrogram)) with multi-language support and SQLite database.

## ✨ Features

- 🌐 Multi-language support with easy switching
- 💾 SQLite database with SQLAlchemy ORM
- 📅 Task scheduling with APScheduler
- 📁 Clean and organized folder structure
- ⚙️ Environment variables management
- 🎯 Decorator-based user handling

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tufcoding/telegram-bot-template.git
   ```

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file with:
   ```env
   API_ID=your_api_id
   API_HASH=your_api_hash
   BOT_TOKEN=your_bot_token
   ```

4. **Run the bot:**
   ```bash
   python main.py
   ```

## 📖 How to Use

Follow these simple steps to customize the bot:

1. Add your commands in the `commands` folder
2. Add your callbacks in the `callbacks` folder
3. Register commands and callbacks in `handlers.py` file
4. Register tasks in `tasks.py` file
5. Add new languages in the `languages` folder
6. Create database models in the `database` folder

## 📈 Scaling to PostgreSQL (Optional)

To upgrade to PostgreSQL:

1. **Install PostgreSQL adapter:**
   ```bash
   pip install psycopg2-binary
   ```

2. **Update database configuration:**
   In `settings.py`, modify the `DATABASE_URL`:
   ```python
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

## 📝 Note

This template follows Telegram bot development best practices and can be customized to suit your needs.
For custom implementations, please reach out to us at any of the following links:

- [Telegram](https://t.me/tufcoding)
- [Discord](https://discord.com/invite/64CDPKPN3V)

## 🤝 Contributing

- Create a new branch for your features
- Submit pull requests for improvements
- Open issues for bugs or suggestions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.