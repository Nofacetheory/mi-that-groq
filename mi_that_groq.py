# ✅ File chính: bot.py (phiên bản chạy trực tiếp, không cần Flask/Telegram)

import requests

# Cấu hình
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

# Tương tác không dùng input() để tránh lỗi I/O trong môi trường sandbox

def run_conversation(queries):
    replies = []
    for prompt in queries:
        if prompt.lower() in ["exit", "quit"]:
            replies.append("Tạm biệt Lủ!")
            break
        reply = call_groq(prompt)
        replies.append(f"Mì: {reply}")
    return replies

# Test mẫu nếu chạy trên môi trường không hỗ trợ input()
if __name__ == '__main__':
    test_inputs = [
        "Mì ơi, hôm nay trời thế nào?",
        "Kể chuyện ma đi Mì",
        "quit"
    ]
    responses = run_conversation(test_inputs)
    for res in responses:
        print(res)
