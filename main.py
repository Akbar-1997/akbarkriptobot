import telebot
from flask import Flask, request

TOKEN = "7503644452:AAEmuYssvT673f8PyH1vP5u8a_Qxd8IOIdU"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Start buyrug‘i
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Salom! Bu Akbar Crypto Bot!")

# Oddiy echo funksiyasi
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Flask route — Telegram webhook'lar uchun
@app.route(f'/{TOKEN}', methods=['POST'])
def receive_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

# Root route (browserda tekshirish uchun)
@app.route('/')
def index():
    return "Bot ishlayapti!"

# Run Flask server
if name == "__main__":
    app.run(host="0.0.0.0", port=10000)
