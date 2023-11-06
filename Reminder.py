import os

import telebot
import time

telebot_id = os.environ.get("TELEBOT_ID")
telebot_token = os.environ.get("TELEBOT_TOKEN")
working_remindments = 0
current_remindment = None

bot = telebot.TeleBot(f"{telebot_id}:{telebot_token}")


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте, я ваша личная напоминалка! Напишите мне сообщение, и скажите, "
                                      "когда его вам переслать!")


@bot.message_handler(content_types=["text"])
def remind(message):
    global working_remindments
    global current_remindment
    if message.text.startswith("/remind"):
        bot.send_message(message.chat.id, "Через сколько часов я должен вам это переслать?")
        if not working_remindments:
            with open("remindment1.txt", "w") as file:
                file.write((message.text + " ")[8:-1])
                working_remindments += 1
                current_remindment = 1
        elif working_remindments == 1:
            with open("remindment2.txt", "w") as file:
                file.write((message.text + " ")[8:-1])
                working_remindments += 1
                current_remindment = 2

    else:
        try:
            if current_remindment == 1:
                time_ = float(message.text)
                time.sleep(time_ * 3600)
                with open("remindment1.txt", encoding="UTF-8") as file:
                    text_ = file.read()
                bot.send_message(message.chat.id, text_)
                current_remindment = None
            elif current_remindment == 2:
                time_ = float(message.text)
                time.sleep(time_ * 3600)
                with open("remindment2.txt", encoding="UTF-8") as file:
                    text_ = file.read()
                bot.send_message(message.chat.id, text_)
                current_remindment = None
            else:
                bot.send_message(message.chat.id, "🤨")

        except ValueError:
            bot.send_message(message.chat.id, "🤨")


bot.polling()
