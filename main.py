import os
import telebot
from flask import Flask, request

# Telegram bot token
TOKEN = "7503644452:AAEmuYssvT673f8PyH1vP5u8a_Qxd8IOIdU"
bot = telebot.TeleBot(TOKEN)

# Flask ilovasi
app = Flask(__name__)

# /start komandasi uchun
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Salom! Bu Akbar Crypto Bot!")

# Oddiy matnli xabarlarga echo
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Webhook endpoint
@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "", 200

# Asosiy sahifa (test uchun)
@app.route("/")
def index():
    return "Bot ishlayapti!"

# TEST SIGNAL (brauzerda tekshirish uchun)
@app.route("/test")
def send_test_signal():
    chat_id = 7949482715  # Sizning Telegram ID'ingiz
    bot.send_message(chat_id, "✅ Test signali: bot ishlayapti!")
    return "Test yuborildi", 200

# Flask serverni ishga tushirish
if name == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
