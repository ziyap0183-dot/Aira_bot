import telebot
import requests

BOT_TOKEN = "PASTE_YOUR_TELEGRAM_TOKEN"
GROQ_API_KEY = "PASTE_YOUR_GROQ_API_KEY"

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
    answer = ask_ai(message.text)
    bot.reply_to(message, answer)

bot.polling()
