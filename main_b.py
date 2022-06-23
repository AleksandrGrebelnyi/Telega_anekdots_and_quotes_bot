
import requests
from flask import Flask, request
import telebot
import os
from bs4 import BeautifulSoup as b
import requests
import random
import bleach

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

URL = 'https://www.anekdot.ru/tags/%D0%B4%D0%B5%D0%B2%D1%83%D1%88%D0%BA%D0%B8/?type=anekdots&sort=sum'
URL_a_9= 'https://www.anekdot.ru/tags/%D0%B4%D0%B5%D0%B2%D1%83%D1%88%D0%BA%D0%B8/9?type=anekdots&sort=sum'
URL_a_10 = 'https://www.anekdot.ru/tags/%D0%B4%D0%B5%D0%B2%D1%83%D1%88%D0%BA%D0%B8/10?type=anekdots&sort=sum'
URL2 = 'https://allcitations.ru/tema/korotkie-citaty-o-zhizni'
URL3 = 'https://allcitations.ru/tema/korotkie-citaty-o-zhizni#'
URL4 = 'https://allcitations.ru/tema/citaty-iz-filmov'
URL5 = 'https://allcitations.ru/tema/umnye-frazy'


def parser_anekdots(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood = parser_anekdots(URL)
random.shuffle(list_of_good_mood)

next_url2 = URL
next_url2 = next_url2[:71] + '2' + next_url2[71:]


def parser_anekdots_second_page(next_url2):
    r = requests.get(next_url2)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood2 = parser_anekdots_second_page(next_url2)
list_of_good_mood.extend(list_of_good_mood2)
random.shuffle(list_of_good_mood)


next_url3 = URL
next_url3 = next_url3[:71] + '3' + next_url3[71:]


def parser_anekdots_3_page(next_url3):
    r = requests.get(next_url3)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood3 = parser_anekdots_3_page(next_url3)
list_of_good_mood.extend(list_of_good_mood3)
random.shuffle(list_of_good_mood)

next_url4 = URL
next_url4 = next_url4[:71] + '4' + next_url4[71:]


def parser_anekdots_4_page(next_url4):
    r = requests.get(next_url4)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood4 = parser_anekdots_4_page(next_url4)
list_of_good_mood.extend(list_of_good_mood4)
random.shuffle(list_of_good_mood)

next_url5 = URL
next_url5 = next_url5[:71] + '5' + next_url5[71:]


def parser_anekdots_5_page(next_url5):
    r = requests.get(next_url5)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood5 = parser_anekdots_5_page(next_url5)
list_of_good_mood.extend(list_of_good_mood5)
random.shuffle(list_of_good_mood)

next_url6 = URL
next_url6 = next_url6[:71] + '6' + next_url6[71:]


def parser_anekdots_6_page(next_url6):
    r = requests.get(next_url6)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood6 = parser_anekdots_6_page(next_url6)
list_of_good_mood.extend(list_of_good_mood6)
random.shuffle(list_of_good_mood)

next_url7 = URL
next_url7 = next_url7[:71] + '7' + next_url7[71:]


def parser_anekdots_7_page(next_url7):
    r = requests.get(next_url7)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood7 = parser_anekdots_7_page(next_url7)
list_of_good_mood.extend(list_of_good_mood7)
random.shuffle(list_of_good_mood)


def parser_anekdots_9_page(next_url9):
    r = requests.get(next_url9)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood9 = parser_anekdots_7_page(URL_a_9)
list_of_good_mood.extend(list_of_good_mood9)
random.shuffle(list_of_good_mood)


def parser_anekdots_9_page(next_url9):
    r = requests.get(next_url9)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood9 = parser_anekdots_9_page(URL_a_9)
list_of_good_mood.extend(list_of_good_mood9)
random.shuffle(list_of_good_mood)


def parser_anekdots_10_page(next_url10):
    r = requests.get(next_url10)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


list_of_good_mood10 = parser_anekdots_10_page(URL_a_10)
list_of_good_mood.extend(list_of_good_mood10)
random.shuffle(list_of_good_mood)
# End collect anekdots and below started to collect list of jokes


def parser_quotes(url2):
    r3 = requests.get(url2)
    soup = b(r3.text, 'html.parser')
    quotes = soup.find_all('div', class_='cittext')
    return [i.text for i in quotes]


list_of_quotes = parser_quotes(URL2)
random.shuffle(list_of_quotes)


def parser_quotes_page_2(url3_next_page):
    r3 = requests.get(url3_next_page)
    soup = b(r3.text, 'html.parser')
    quotes_list2 = soup.find_all('div', class_='cittext')
    return [i.text for i in quotes_list2]


list_of_quotes2 = parser_quotes_page_2(URL3)
list_of_quotes.extend(list_of_quotes2)
random.shuffle(list_of_quotes)


def parser_quotes_page_4(url4_next_page):
    r3 = requests.get(url4_next_page)
    soup = b(r3.text, 'html.parser')
    quotes_list4 = soup.find_all('div', class_='cittext')
    return [i.text for i in quotes_list4]


list_of_quotes4 = parser_quotes_page_4(URL4)
list_of_quotes.extend(list_of_quotes4)
random.shuffle(list_of_quotes)


def parser_quotes_page_5(url5_next_page):
    r3 = requests.get(url5_next_page)
    soup = b(r3.text, 'html.parser')
    quotes_list5 = soup.find_all('div', class_='cittext')
    return [i.text for i in quotes_list5]


list_of_quotes5 = parser_quotes_page_5(URL5)
list_of_quotes.extend(list_of_quotes5)
random.shuffle(list_of_quotes)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button_yes = telebot.types.InlineKeyboardButton(text='Хочу анекдотик😂', callback_data='yes')
    button_no = telebot.types.InlineKeyboardButton(text='Хочу умную цитату🤓', callback_data='no')
    markup.add(button_yes, button_no)
    bot.send_message(message.chat.id, '<u><b>Привет, хочешь посмеяться или воодушевиться?</b></u> '
                                      'Выбирай кнопку и жмакай 🤗', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    markup2 = telebot.types.InlineKeyboardMarkup()
    button_yes = telebot.types.InlineKeyboardButton(text='Хочу eщё анекдотик😂😎', callback_data='yes')
    button_no = telebot.types.InlineKeyboardButton(text='Хочу цитату🤓', callback_data='no')
    markup2.add(button_yes, button_no)
    if call.data == 'yes' and list_of_good_mood:
        bot.send_message(call.message.chat.id, list_of_good_mood[0], reply_markup=markup2)
        del list_of_good_mood[0]
    elif call.data == 'yes':
        bot.send_message(call.message.chat.id, '<b>Анекдоты закончились🤦‍♂️, теперь я твое эхо, просто напиши, '
                                               'что то в чат, а я напишу, что вы написали...</b> 🤷‍♂️ ')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, list_of_quotes[0], reply_markup=markup2)
        del list_of_quotes[0]
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, '<b>Ой, цитаты закончились🤦‍♂, теперь я эхо бот, просто пиши, что то'
                                               ' в чат, а я напишу, что вы написали... ')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, '<b>Вы написали:</b> ' + message.text)


@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot", 200


@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://bot-anekdots-quotes.herokuapp.com/' + TOKEN)
    return 'Python Telegram Bot', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))



