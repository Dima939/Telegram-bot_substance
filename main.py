import telebot
from func_mol_mass import func

bot = telebot.TeleBot('5902384286:AAEyVy_SyGVCIX3Q0EJyChPUhEL1MecldoU')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введи формулу вещества, молекулярную массу которого хочешь узнать\n'
                                      'Если в ответе получается не то вещество, которое тебе нужно, поставь '
                                      'после эелемента без индекса "1"')


@bot.message_handler(content_types=['text'])
def repeat_message(message):
    try:
        result = func(message.text)
        bot.send_message(message.chat.id, result)
    except:
        bot.send_message(message.chat.id, 'Некорректная формула, попробуй ещё раз')


if __name__ == '__main__':
    bot.infinity_polling()
