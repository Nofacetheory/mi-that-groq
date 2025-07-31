# ✅ File chính: bot.py (phiên bản chạy trực tiếp, không cần Flask/Telegram)

import requests
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Key thật của Lủ

# Hàm gọi Groq
def call_groq(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "Bạn là Mì, trợ lý thông minh của Lủ."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Mì lỗi rồi Lủ ơi... Lỗi: {e}"

# Telegram Bot
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TELEGRAM_TOKEN = "7230484227:AAFaThmILI50HNnFTPfqApBvxNj9WhxCEGQ"
OWNER_ID = os.getenv("OWNER_ID", "")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Mì online rồi Lủ ơi! Gửi gì đi nè.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = call_groq(user_message)
    await update.message.reply_text(reply)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Mì Telegram online rồi!")
    app.run_polling()
