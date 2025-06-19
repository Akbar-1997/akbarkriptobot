import telebot
import os

# Environment variabledan tokenni olish
TOKEN = os.environ.get('BOT_TOKEN')

if not TOKEN:
    raise Exception("Bot token not found in environment variables.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot ishlayapti!")

try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Bot stopped due to: {e}")
