import telebot

bot = telebot.TeleBot('6383848728:AAExXNVJkqYT5UfDJyvnHLr1x8hFP3y_GN0')

@bot.message_handler(commands=['start'])

def main(message):
    bot.send_message(messge.chat.id, 'Привет')



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

