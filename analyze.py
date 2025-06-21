import time
import telebot

TOKEN = "7503644452:AAEmuYssvT673f8PyH1vP5u8a_Qxd8IOIdU"
CHAT_ID = 7949482715
bot = telebot.TeleBot(TOKEN)

def analyze_and_send_signals():
    signal_text = "📈 TEST SIGNAL: BTCUSDT Breakout aniqlandi! (RSI > 70, 200 EMA yuqorida, Resistance buzildi)"
    bot.send_message(CHAT_ID, signal_text)
    print(f"✅ Signal yuborildi: {signal_text}")