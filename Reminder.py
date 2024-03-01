import os

import telebot
import time

telebot_id = os.environ.get("TELEBOT_ID")
telebot_token = os.environ.get("TELEBOT_TOKEN")
working_reminders = 0
current_reminder = None

bot = telebot.TeleBot(f"{telebot_id}:{telebot_token}", num_threads=3)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте, я ваша личная напоминалка! Напишите мне сообщение, и скажите, "
                                      "когда его вам переслать!")


@bot.message_handler(content_types=["text"])
def remind(message):
    global working_reminders
    global current_reminder
    if message.text.startswith("/remind"):
        if working_reminders < 3:
            bot.send_message(message.chat.id, "Через сколько часов я должен вам это переслать?")
            if working_reminders == 0:
                print("BEGIN 1", working_reminders)
                with open("remindment1.txt", "w") as file:
                    file.write((message.text + " ")[8:-1])
                working_reminders += 1
                current_reminder = 1
                print("END 1", working_reminders)
            elif working_reminders == 1:
                print("BEGIN 2", working_reminders)
                with open("remindment2.txt", "w") as file:
                    file.write((message.text + " ")[8:-1])
                working_reminders += 1
                current_reminder = 2
                print("END 2", working_reminders)
            elif working_reminders == 2:
                print("BEGIN 3", working_reminders)
                with open("remindment3.txt", "w") as file:
                    file.write((message.text + " ")[8:-1])
                working_reminders += 1
                current_reminder = 3
                print("END 3", working_reminders)
        else:
            bot.send_message(message.chat.id, "У меня слоты для напоминаний кончились")

    else:
        try:
            if current_reminder == 1:
                time_ = float(message.text)
                bot.send_message(message.chat.id, "Принято")
                time.sleep(time_ * 3600)
                with open("remindment1.txt", encoding="UTF-8") as file:
                    text_ = file.read()
                bot.send_message(message.chat.id, text_)
                current_reminder = None
                working_reminders -= 1
            elif current_reminder == 2:
                time_ = float(message.text)
                bot.send_message(message.chat.id, "Принято")
                time.sleep(time_ * 3600)
                with open("remindment2.txt", encoding="UTF-8") as file:
                    text_ = file.read()
                bot.send_message(message.chat.id, text_)
                current_reminder = None
                working_reminders -= 1
            elif current_reminder == 3:
                time_ = float(message.text)
                bot.send_message(message.chat.id, "Принято")
                time.sleep(time_ * 3600)
                with open("remindment3.txt", encoding="UTF-8") as file:
                    text_ = file.read()
                bot.send_message(message.chat.id, text_)
                current_reminder = None
                working_reminders -= 1
            else:
                bot.send_message(message.chat.id, "🤨")

        except ValueError:
            bot.send_message(message.chat.id, "🤨")


bot.polling()
