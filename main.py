import telebot
from const import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_message(message):
        bot.reply_to(message, 'Привет!')

@bot.message_handler(content_types=['text'])
def handle_message(message):
    bot.reply_to(message, message.text)

bot.polling()