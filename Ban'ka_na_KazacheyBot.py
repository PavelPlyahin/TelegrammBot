import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('7254958470:AAE_Czh0Xhc-VFQAf8CiiHxbAOU88fnT3zE')
is_clicked = False
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://vk.com/bankanakazachey')
    btn2 = types.InlineKeyboardButton('Отзывы о нас', url='https://vk.com/topic-101755861_35810811')
    btn3 = types.InlineKeyboardButton('Фотогалерея', url='https://vk.com/album-101755861_220862100')
    btn4 = types.InlineKeyboardButton('Бронирование', url='https://vk.com/app5708398_-101755861?ref=group_menu')
    keyboard.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Здравствуйте', reply_markup=keyboard)
    bot.send_message(message.chat.id, f' Рад новому знакомству, {message.from_user.first_name}')
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(func=lambda message: True)
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'https://vk.com/bankanakazachey')
        webbrowser.open('https://vk.com/bankanakazachey', new=2, autoraise=True)
    elif message.text == 'Отзывы о нас':
        bot.send_message(message.chat.id, 'https://vk.com/topic-101755861_35810811')
        webbrowser.open('https://vk.com/topic-101755861_35810811')
    elif message.text == 'Фотогалерея':
        bot.send_message(message.chat.id, 'https://vk.com/album-101755861_220862100')
        webbrowser.open('https://vk.com/album-101755861_220862100')
    elif message.text == 'Бронирование':
        bot.send_message(message.chat.id, 'https://vk.com/app5708398_-101755861?ref=group_menu')
        webbrowser.open('https://vk.com/app5708398_-101755861?ref=group_menu')


    # Функция для обработки сообщения
    if message.text in questions:
        bot.send_message(message.chat.id, questions[message.text])
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял. Попробуйте задать другой вопрос.")


# Массив с вопросами и ответами
questions = {
    "Привет": "Привет!",
    "Баня на дровах?": "Да конечно, в русских традициях!",
    "Сколько стоит час?": "1600 рублей за час до 6 человек!",
    "Можно забронировать баню?": "Да, для этого нажмите кнопку в меню Бронирование, или позвоните по телефону 89003980333",
    "Можно заказать баню?": "Да, для этого нажмите кнопку в меню Бронирование, или позвоните по телефону 89003980333",
    "До скольки работаете?": "Работает пока гости не устанут!",
    "Веники есть?": "Да,в наличии дубовые веники по 500 рублей за штуку!",
    "": ""
}

# Запуск бота
bot.polling(none_stop=True)
