import telebot

from telebot.types import Message

print("Lord Michelin is working...")

bot = telebot.TeleBot("934747315:AAGULA3JzsOeKUieypa1xKCuZbkUfUkrDHg")

'''@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    print(message.sticker)
    print(message.sticker)'''


@bot.message_handler(commands=['try'])
def parser_tg(message: Message):
    bot.send_message(message.chat.id, 'You wrote me /try', reply_markup = keyboard1)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Hi', 'Bye')


@bot.message_handler(commands=['start'])  # Виклик по команді "/start "
@bot.message_handler(content_types=['sticker'])
def command_handler(message: Message):
    bot.reply_to(message, "Welcome to the club buddy, " + str(message.from_user.first_name) + '!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBsV8t1B_namWDA8bL2Udjw9Mdz3UxAALgAANdj6EVOvi2q-rwxQ8aBA')
    bot.send_message(message.chat.id, 'You wrote me /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])  # Виклик по тексту
@bot.message_handler(content_types=['sticker'])
@bot.edited_message_handler(content_types=['text'])  # Бот ревгує на редакію повідомлень у ТГ
def echo_digits(message: Message):
    if 'Hi' in message.text:  # Бот реагує на текст 'Привіт'
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBcV8txcjB7q7Lknl-aQyOGBKE5C4ZAAI5AANdj6EVVJml4_dDVrwaBA')
        return
    elif 'Bye' in message.text:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBwV8t1TnhXvhCjt0AARCwXXi4d-SQgQAC2AADXY-hFcYzjXjp9fbJGgQ')
    else:
        bot.reply_to(message, "I don't understand you!")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBUV8twyOwqStsVQRWrzuGYxYVtm3bAAI2AANdj6EVOylnZmQBNYYaBA')


bot.polling(none_stop=True)
