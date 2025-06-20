import telebot
import os
from flask import Flask, request

TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    raise Exception("Bot token not found in environment variables.")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# /start буйруғи
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Bot ishga tushdi.")

# Webhook endpoint
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

# Telegram webhook URL’ни ўрнатиш
@app.route("/", methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://akbarkriptobot.onrender.com/{TOKEN}")
    return "Webhook set", 200

if name == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
