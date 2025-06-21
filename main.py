import time
import schedule
from flask import Flask
from threading import Thread
from analyze import analyze_and_send_signals  # Sizda mavjud bo'lishi kerak
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot ishlayapti!'

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
    job()  # dastlab darhol ishga tushadi
    while True:
        schedule.run_pending()
        time.sleep(1)

# Flask server thread
def run_flask():
    app.run(host='0.0.0.0', port=10000)

if __name__ == '__main__':
    Thread(target=run_schedule).start()
    Thread(target=run_flask).start()
