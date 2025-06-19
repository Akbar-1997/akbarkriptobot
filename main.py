import telebot
import os  # ⬅️ OS modulini qo‘shamiz

TOKEN = os.environ.get("TELEGRAM_TOKEN")  # ⬅️ TOKENni ENV dan olamiz
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! @Akbarkriptobot ishga tushdi.")

bot.polling()