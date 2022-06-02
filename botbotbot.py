# -*- coding: utf-8 -*-
import telebot, bs4, requests
bot = telebot.TeleBot("1239157216:AAHgozkrePKPvaIxIRx_qNkfZd8WCKntYEg")


def getanekdot():
    z=''
    s=requests.get('http://anekdotme.ru/random')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.anekdot_text')
    for x in p:
        s=(x.getText().strip())
        z=z+s+'\n\n'
    return s


@bot.message_handler(content_types=["text"])
def handle_text(message):
    msg=message.text
    msg=msg.lower()
    if (u'анекдот' in msg):
        try:
            bot.send_message(message.from_user.id, getanekdot())
        except:
            pass
    else:
        bot.send_message(message.from_user.id, u'Хочешь еще? Нажми кнопку "Анекдот"')

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Анекдот')
    bot.send_message(message.chat.id, 'Хочешь еще? Нажми кнопку "Анекдот"', reply_markup=keyboard)




@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.from_user.id, u'Хочешь еще? Нажми кнопку "Анекдот"')



bot.polling(none_stop=True, interval=0)