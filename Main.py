import telebot

value = ''
old_value = ''

calculon = telebot.TeleBot('6777623757:AAH5hEYB9n4vQJIqzpjKp4wA0XMGnPlTyb8')

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('c', callback_data='c'),
             telebot.types.InlineKeyboardButton('<-', callback_data='<-'),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton('.', callback_data='.'),
             telebot.types.InlineKeyboardButton('=', callback_data='='))

@calculon.message_handler(commands=['start'])
def getMessage(message):
    global value, old_value
    if value == '':
        calculon.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        calculon.send_message(message.from_user.id, value, reply_markup=keyboard)
    old_value = value

@calculon.callback_query_handler(func= lambda call: True)
def callback(query):
    global value, old_value
    data = query.data

    if data == 'c':
        value = ''
    elif data == '<-':
        if value != '':
            value = value[:len(value) - 1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Error'
    else:
        value+= data

    if (value != old_value and value != '') or (old_value != 0 and value ==''):
        if value == '':
            calculon.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
            old_value = 0
        else:
            calculon.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
            old_value = value

    old_value = value
    if value == 'Error':
        value = ''

calculon.polling(none_stop=False, interval=0)