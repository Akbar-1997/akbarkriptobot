import ccxt
import pandas as pd
import pandas_ta as ta
from telebot import TeleBot
import time

# Telegram bot ma'lumotlari
TOKEN = "7503644452:AAEmuYssvT673f8PyH1vP5u8a_Qxd8IOIdU"
CHAT_ID = 7949482715
bot = TeleBot(TOKEN)

# Binance exchange
exchange = ccxt.binance()

# Coinlar va timeframe'lar
COINS = [
    "BTC/USDT", "ETH/USDT", "XRP/USDT", "AVAX/USDT", "FTM/USDT", "KAS/USDT", "SUI/USDT",
    "MATIC/USDT", "OP/USDT", "ARB/USDT", "CFX/USDT", "AGIX/USDT", "RNDR/USDT", "STX/USDT",
    "FET/USDT", "OCEAN/USDT", "NEAR/USDT", "MASK/USDT", "CTXC/USDT", "ROSE/USDT", "SAND/USDT",
    "MANA/USDT", "AXS/USDT", "GALA/USDT", "PIXEL/USDT", "XAI/USDT", "THETA/USDT", "INJ/USDT",
    "LDO/USDT", "MINA/USDT", "APT/USDT", "ALGO/USDT", "TON/USDT", "WLD/USDT", "GRT/USDT",
    "IOTA/USDT", "IOTX/USDT", "LINK/USDT", "RWA/USDT"
]

TIMEFRAMES = ['2h', '4h', '1d']

def analyze_and_send_signals():
    print("🔍 Tahlil boshlandi...")
    for coin in COINS:
        for tf in TIMEFRAMES:
            try:
                ohlcv = exchange.fetch_ohlcv(coin, tf, limit=200)
                df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

                df['rsi'] = ta.rsi(df['close'], length=14)
                df['ema200'] = ta.ema(df['close'], length=200)

                if df['rsi'].isnull().any() or df['ema200'].isnull().any():
                    continue

                last = df.iloc[-1]
                resistance = max(df['high'][-20:])  # So'nggi 20ta yuqori narx

                if (
                    last['rsi'] > 70 and
                    last['close'] > last['ema200'] and
                    last['close'] > resistance
                ):
                    signal = f"📈 {coin.replace('/USDT', 'USDT')} Breakout aniqlandi! ({tf})\n" \
                             f"RSI: {round(last['rsi'], 2)}\n" \
                             f"Close: {last['close']}\n" \
                             f"EMA200: {round(last['ema200'], 2)}\n" \
                             f"Resistance: {round(resistance, 2)}"
                    bot.send_message(CHAT_ID, signal)
                    print(f"✅ Signal yuborildi: {signal}")
            except Exception as e:
                print(f"❌ {coin} - {tf} tahlilida xato: {e}")

# 🔁 Doimiy ishga tushirish
print("🚀 Bot ishga tushdi!")
print("♻️ Doimiy signal monitoringi boshlandi...")
while True:
    analyze_and_send_signals()
    time.sleep(1800)  # Har 30 daqiqa
