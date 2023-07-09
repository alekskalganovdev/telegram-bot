import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot('6383848728:AAExXNVJkqYT5UfDJyvnHLr1x8hFP3y_GN0')

@bot.message_handler(commands=['start'])

def get_photo(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.add(btn1)
    btn2 = types.KeyboardButton('Обо мне')
    btn3 = types.KeyboardButton('Мои работы')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Web site')
    elif message.text == 'Обо мне':
        bot.send_message(message.chat.id, url = 'https://instagram.com/fvvictoria?igshid=OGQ5ZDc2ODk2ZA==')
    elif message.text == 'Мои работы':
        bot.send_message(message.chat.id, url = 'https://instagram.com/fvv.photo?igshid=MjEwN2IyYWYwYw==')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://mail.ru')

#@bot.message_handler(content_types='photo')
#def get_photo(message):
#    markup = types.InlineKeyboardMarkup()
#    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
#    markup.add(btn1)
#    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#    markup.row(btn2, btn3)
#   bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)




bot.polling(none_stop=True)


