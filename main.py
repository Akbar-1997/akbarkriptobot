import time
import schedule
import logging
from flask import Flask, request
from threading import Thread
from analyze import analyze_and_send_signals

app = Flask(__name__)  # ✅ to'g'rilandi

@app.route('/')
def home():
    return 'Bot ishlayapti!'

# ✅ Telegram webhook'ни қабул қилувчи endpoint
@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    try:
        update = request.get_json()
        logging.info(f"Telegramdan update: {update}")
        # Bu yerda istasangiz handle_update(update) funksiyasi qo‘shishingiz mumkin
        return 'ok'
    except Exception as e:
        logging.exception("Webhook qabul qilishda xatolik yuz berdi:")
        return 'error', 500

# Har 30 daqiqada signal tahlili
def job():
    try:
        print("⏳ Signal tahlili boshlanmoqda...")
        analyze_and_send_signals()
        print("✅ Signal tahlili yakunlandi.")
    except Exception as e:
        logging.exception("Xatolik yuz berdi (analyze_and_send_signals):")

# Schedule thread
def run_schedule():
    schedule.every(30).minutes.do(job)
    job()
    while True:
        schedule.run_pending()
        time.sleep(1)

# Flask server thread
def run_flask():
    app.run(host='0.0.0.0', port=10000)

if name == '__main__':  # ✅ to'g'rilandi
    Thread(target=run_schedule).start()
    Thread(target=run_flask).start()
