import telebot
import requests

# 🔑 DIRECT TOKEN (yahan apna daalo)
BOT_TOKEN = "8676477566:AAF5nGSIfQuCVAVxY1w0zvQqMrQCXiLs8Sg"
GROQ_API_KEY = "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""

bot = telebot.TeleBot(BOT_TOKEN)

# 🤖 AI function
def ask_ai(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are Aira, a friendly AI assistant. Talk naturally."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except:
        return "⚠️ Error aaya, baad me try karo"

# 📩 Message handler
@bot.message_handler(func=lambda message: True)
def reply(message):
    user_text = message.text
    answer = ask_ai(user_text)
    bot.reply_to(message, answer)

# ▶️ Start bot
print("🤖 Aira Bot is running...")
bot.infinity_polling()
