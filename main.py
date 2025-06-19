import telebot
import os

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise Exception("Bot token not found in environment variables.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "Assalomu alaykum, bot ishga tushdi!")

bot.polling()
