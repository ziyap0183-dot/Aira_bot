import telebot
import requests
import os

BOT_TOKEN = os.getenv("8676477566:AAF5nGSIfQuCVAVxY1w0zvQqMrQCXiLs8Sg")
GROQ_API_KEY = os.getenv("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")

bot = telebot.TeleBot(BOT_TOKEN)

def ask_ai(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        answer = ask_ai(message.text)
        bot.reply_to(message, answer)
    except Exception:
        bot.reply_to(message, "Error aa gaya 😅")

bot.polling()
