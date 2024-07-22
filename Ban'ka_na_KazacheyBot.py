"""Телеграмм Бот, "Банька на Казачей!"
Основная функция, автоматизированно отвечать на вопросы людей, знакомить с сообществом в ВК "Банька на Казачей",
выполнять онлайн бронирование на посещение бани!"""

import telebot  # telebot — библиотека для работы с ботами в Telegram.
from telebot import types  # types — модуль внутри библиотеки telebot, содержащий различные типы сообщений,
# которые можно отправить пользователю.
import webbrowser  # webbrowser — стандартный модуль Python, который используется для открытия браузера.

bot = telebot.TeleBot(
    '7254958470:AAE_Czh0Xhc-VFQAf8CiiHxbAOU88fnT3zE')  # Создаётся объект бота с помощью метода TeleBot,
# которому передаётся токен бота.
is_clicked = True


# Этот код создаёт обработчик команды start, которая является одной из команд, доступных пользователю
# для взаимодействия с ботом.
# Когда пользователь отправляет сообщение с командой start, бот отвечает сообщением "Здравствуйте",
# "Рад новому знакомству",
# и обращается по имени к тому, кто пишет! (first_name),
# а также предлагает пользователю несколько вариантов действий с помощью клавиатуры.
# Пользователь может нажать на одну из кнопок, чтобы перейти по указанной ссылке.
# Код также регистрирует функцию on_click как следующий шаг обработки сообщения. Это означает, что после того,
# как пользователь нажмёт на одну из кнопок клавиатуры, бот выполнит функцию on_click, которая обрабатывает действие
# пользователя в зависимости от нажатой кнопки.
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем клавиатуру, и меняем размер кнопок
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://vk.com/bankanakazachey')
    btn2 = types.InlineKeyboardButton('Отзывы о нас', url='https://vk.com/topic-101755861_35810811')
    btn3 = types.InlineKeyboardButton('Фотогалерея', url='https://vk.com/album-101755861_220862100')
    btn4 = types.InlineKeyboardButton('Предворительная запись',
                                      url='https://vk.com/app5708398_-101755861?ref=group_menu')
    btn5 = types.InlineKeyboardButton('Online Брoнь', url='https://calendar.app.google/GWVQvmkASAAeEfMo6')
    keyboard.add(btn1, btn2, btn3, btn4, btn5)  # Добовляем кнопки

    bot.send_message(message.chat.id, 'Здравствуйте', reply_markup=keyboard)
    # Бот отпраляет сообщение "Зравствуйте" и запускает клавиатуру с кнопками к которым привязаны ссылки!
    bot.send_message(message.chat.id, f' Рад новому знакомству, {message.from_user.first_name}!')
    # Бот отправляет сообщение "Рад новому знакомству", инициализирует пользователя по имени и обрашается к нему
    bot.register_next_step_handler(message, on_click)

    # Метод register_next_step_handler позволяет задать функцию, которая будет вызвана после получения определённого
    # типа сообщения. В данном случае, эта функция — on_click.
    # Этот метод используется для организации последовательности обработки сообщений.
    # Он позволяет реализовать логику, при которой после выполнения какого-либо действия
    # (например, нажатия на кнопку) происходит переход к следующему шагу взаимодействия с пользователем.


# Этот код определяет функцию on_click, которая вызывается после того, как пользователь нажимает на кнопку в сообщении.
# Функция проверяет, какое действие было выбрано пользователем, и выполняет соответствующее действие.
# Если пользователь выбирает действие «Перейти на сайт», бот отправляет ссылку на сайт и открывает её в новой вкладке
# браузера. Аналогично обрабатываются и другие действия.
# Если пользователь выбирает действие, которого нет в списке, ничего не происходит.
@bot.message_handler(func=lambda message: True)
def on_click(message):
    if message.text in ('Перейти на сайт', 'Отзывы о нас', 'Фотогалерея', 'Предворительная запись', 'Online Брoнь'):
        if message.text == 'Перейти на сайт':
            bot.send_message(message.chat.id, 'https://vk.com/bankanakazachey')
            webbrowser.open_new_tab('https://vk.com/bankanakazachey')
        elif message.text == 'Отзывы о нас':
            bot.send_message(message.chat.id, 'https://vk.com/topic-101755861_35810811')
            webbrowser.open_new_tab('https://vk.com/topic-101755861_35810811')
        elif message.text == 'Фотогалерея':
            bot.send_message(message.chat.id, 'https://vk.com/album-101755861_220862100')
            webbrowser.open_new_tab('https://vk.com/album-101755861_220862100')
        elif message.text == 'Предворительная запись':
            bot.send_message(message.chat.id, 'https://vk.com/app5708398_-101755861?ref=group_menu')
            webbrowser.open_new_tab('https://vk.com/app5708398_-101755861?ref=group_menu')
        elif message.text == 'Online Брoнь':
            bot.send_message(message.chat.id, 'https://calendar.app.google/GWVQvmkASAAeEfMo6')
            webbrowser.open_new_tab('https://calendar.app.google/GWVQvmkASAAeEfMo6')

    else:
        pass  # Ничего не делать

        # Функция для обработки сообщения. Этот код проверяет, есть ли текст сообщения (message.text)
        # в списке вопросов (questions). Если да, то бот отправляет пользователю ответ из списка вопросов,
        # соответствующий тексту сообщения. Если текста сообщения нет в списке вопросов, бот сообщает пользователю,
        # что не может ответить на этот вопрос.

        if message.text in questions:
            bot.send_message(message.chat.id, questions[message.text])
        else:
            bot.send_message(message.chat.id, "Извините, я не могу ответить на этот вопрос!")


# Массив с вопросами и ответами
questions = {
    "Привет": "Привет!",
    "Баня на дровах?": "Да конечно, в русских традициях!",
    "Сколько стоит час?": "1600 рублей за час до 6 человек!",
    "Можно забронировать баню?": "Да, нажмите кнопку в меню Бронирование, или позвоните по телефону 89003980333",
    "Можно заказать баню?": "Да, нажмите кнопку в меню Бронирование, или позвоните по телефону 89003980333",
    "До скольки работаете?": "Работает пока гости не устанут!",
    "Веники есть?": "Да,в наличии дубовые веники по 500 рублей за штуку!",
    "Добрый день": "Добрый день!",
    "Как забронировать баню?": "Пожалуйста перейдите по ссылке https://calendar.app.google/GWVQvmkASAAeEfMo6",
}

# Запуск бота
bot.polling(none_stop=True)
