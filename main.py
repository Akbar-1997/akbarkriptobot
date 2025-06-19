import telebot
import os  # OS moduli kerak bo'ladi

TOKEN = os.environ.get("TELEGRAM_TOKEN")  # Tokenni atrof-muhitdan olamiz
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! @Akbarkriptobot ishga tushdi.")

bot.polling()
