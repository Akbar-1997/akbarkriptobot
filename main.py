import telebot
from flask import Flask, request
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    raise Exception("Token topilmadi. TELEGRAM_TOKEN environment variable sifatida qo'shilmagan.")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# /start komandasi
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "✅ Bot ishga tushdi!")

# Webhook endpoint
@app.route(f"/{TOKEN}", methods=['POST'])
def receive_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

# Webhook URLni o‘rnatish
@app.route("/", methods=["GET"])
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://akbarkriptobot.onrender.com/{TOKEN}")
    return "✅ Webhook o‘rnatildi", 200

# TO‘G‘RI YOZILISHI SHU ⬇️
if name == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
