import telebot

bot = telebot.TeleBot('5902384286:AAEyVy_SyGVCIX3Q0EJyChPUhEL1MecldoU')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome!!!')


@bot.message_handler(content_types=['text'])
def repeat_message(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()

