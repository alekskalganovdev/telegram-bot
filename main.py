import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot('6383848728:AAExXNVJkqYT5UfDJyvnHLr1x8hFP3y_GN0')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://mail.ru')

@bot.message_handler(content_types='photo')
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)

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


