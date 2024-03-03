import os

import telebot
from time import sleep

telebot_id = os.environ.get("TELEBOT_ID")
telebot_token = os.environ.get("TELEBOT_TOKEN")
working_reminders = 0
file_ = {0: "reminder1.txt",
         1: "reminder2.txt",
         2: "reminder3.txt"}
time__ = {1: "reminder1.txt",
          2: "reminder2.txt",
          3: "reminder3.txt"}

bot = telebot.TeleBot(f"{telebot_id}:{telebot_token}", num_threads=3)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте, я ваша личная напоминалка! Напишите мне сообщение, и скажите, "
                                      "когда его вам переслать!")


@bot.message_handler(content_types=["text"], regexp="/remind")
def remind(message):
    global working_reminders
    global file_
    if working_reminders < 3:
        bot.send_message(message.chat.id, "Через сколько часов я должен вам это переслать?")
        with open(file_[working_reminders], "w") as file:
            file.write((message.text + " ")[8:-1])
        working_reminders += 1
    else:
        bot.send_message(message.chat.id, "У меня слоты для напоминаний кончились")


@bot.message_handler(content_types=["text"])
def time(message):
    global working_reminders
    try:
        if working_reminders:
            time_ = float(message.text)
            bot.send_message(message.chat.id, "Принято")
            sleep(time_ * 3600)
            with open(time__[working_reminders], encoding="UTF-8") as file:
                text_ = file.read()
            bot.send_message(message.chat.id, text_)
            working_reminders -= 1
        else:
            bot.send_message(message.chat.id, "🤨")

    except ValueError:
        bot.send_message(message.chat.id, "🤨")


bot.polling()
