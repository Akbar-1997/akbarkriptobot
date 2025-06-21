from flask import Flask, request
import telebot

TOKEN = "7503644452:AAEmuYssvT673f8PyH1vP5u8a_Qxd8IOIdU"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)  # TO‘G‘RI

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Salom! Bu Akbar Crypto Bot!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

@app.route(f'/{TOKEN}', methods=['POST'])
def receive_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    return "Bot ishlayapti!"

@app.route('/test')
def send_test_signal():
    chat_id = 7949482715  # Sizning Telegram ID
    bot.send_message(chat_id, "✅ Test signali: bot ishlayapti!")
    return "Test yuborildi", 200

# 🟢 MUHIM: Shu yer tuzatildi
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
