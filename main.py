import telebot

bot = telebot.TeleBot('6383848728:AAExXNVJkqYT5UfDJyvnHLr1x8hFP3y_GN0')


@bot.message_handler(commands=['start'])

def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}' )

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
 

bot.polling(none_stop=True)


