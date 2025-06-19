import telebot

TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! @Akbarkriptobot ishga tushdi.")

bot.polling()
