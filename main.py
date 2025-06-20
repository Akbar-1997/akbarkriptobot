import telebot
import os

# Tokenni olish
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not BOT_TOKEN:
    raise Exception("Bot token not found in environment variables.")

bot = telebot.TeleBot(BOT_TOKEN)

# /start buyrug'i
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men AkbarCryptoBotman. Buyruqlaringizni kutyapman.")

# /info buyrug'i
@bot.message_handler(commands=['info'])
def bot_info(message):
    bot.reply_to(message, "🤖 Bu bot Akbar tomonidan yaratildi.\n📈 Kripto signal, Elliott tahlil, news alert va boshqa qulayliklarni taqdim etadi.")

# /status buyrug'i
@bot.message_handler(commands=['status'])
def bot_status(message):
    bot.reply_to(message, "✅ Bot faol ishlayapti!")

# /help buyrug'i
@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.reply_to(message, "📋 Buyruqlar ro'yxati:\n/start - Botni ishga tushirish\n/info - Bot haqida\n/status - Holatini tekshirish\n/help - Yordam")

# Botni ishga tushurish
print("Bot is running...")
bot.infinity_polling()
