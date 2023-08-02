import os

import telebot
import time

telebot_id = os.environ.get("TELEBOT_ID")
telebot_token = os.environ.get("TELEBOT_TOKEN")

bot = telebot.TeleBot(f"{telebot_id}:{telebot_token}")


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте, я ваша личная напоминалка! Напишите мне сообщение, и скажите, "
                                      "когда его вам переслать!")


@bot.message_handler(content_types=["text"])
def remind(message):
    if message.text.startswith("/remind"):
        bot.send_message(message.chat.id, "Через сколько часов я должен вам это переслать?")
        with open("remindment.txt", "w") as file:
            file.write((message.text+" ")[7:-1])

    else:
        try:
            time_ = float(message.text)
            time.sleep(time_*3600)
            with open("remindment.txt", encoding="UTF-8") as file:
                text_ = file.read()
            bot.send_message(message.chat.id, text_)

        except ValueError:
            bot.send_message(message.chat.id, "🤨")


bot.polling()
