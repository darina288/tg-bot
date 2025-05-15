import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
# Получаем переменные окружения
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Приветствую👋! Используйте команду /books, чтобы я смог подобрать для Вас книгу📔')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/books')
    markup.row(btn1)
    bot.send_message(message.chat.id, '⤵️', reply_markup=markup)

# Выбираем уровень владения англ. языком
@bot.message_handler(commands=['books'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('A2-B1')
    markup.row(btn1)
    btn2 = types.KeyboardButton('B2-C1')
    markup.row(btn2)
    bot.send_message(message.chat.id, 'Укажите ваш уровень владения английским языком🇬🇧:', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

# Получаем перечень предложенных книг
def on_click(message):
    if message.text == 'A2-B1':
        bot.send_message(message.chat.id, '✅Рекомендуемые книги для Вас: '
                                          '\n•Детектив: Sherlock Holmes by Arthur Conan Doyle, '
                                          '\n•Фантастика: The Wizard of Oz by L. Frank Baum, '
                                          '\n•Романтика: Love or Money by Rowena Akinyemi, '
                                          '\n•Классика: Great Expectations by Charles Dickens')
    elif message.text == 'B2-C1':
        bot.send_message(message.chat.id, '✅Рекомендуемые книги для Вас: '
                                          '\n•Детектив: The Da Vinci Code by Dan Brown, '
                                          '\n•Фантастика: Harry Potter and the Philosopher’s Stone by J.K. Rowling, '
                                          '\n•Романтика: Pride and Prejudice by Jane Austen, '
                                          '\n•Классика: 1984 by George Orwell')

# Получаем список команд, которые может осуществить бот
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Мои команды🙋‍♂️: '
                                      '\n/start - Запустить бота '
                                      '\n/books - Выбрать подходящий уровень английского языка '
                                      '\n/info - Информация о боте' 
                                      '\n\nP.S. Возможны временные ограничения работоспособности бота, заранее '
                                      'приносим свои извинения за предоставленные неудобства🥺')

# Получаем информацию о боте
@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, '👋Приветствую! Данный бот - разработка студентов курса "Цифровой переводчик" '
                                      'института ВШМОиМИ ИМОИиВ. '
                                      '\n\n✅Этот бот предназначен для того чтобы рекомендовать литературу '
                                      'на английском языке. Целью данного бота является упрощение поиска нужной '
                                      'литературы для ознакомления и возможного последующего прочтения. '
                                      '\n\n😊Спасибо за то, что воспользовались нашим ботом!')

bot.polling(none_stop=True)
