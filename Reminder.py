import telebot

# jfkshfueisdhishfriufshdsjchfirefsakhfyruid;ohsg87frudiwok


bot = telebot.TeleBot("5910558079:AAFMX4Zz7fDagtjVc4uKQHtDXwaRy2XbQz0")


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте, я ваша личная напоминалка! Напишите мне сообщение, и скажите, "
                                      "когда его вам переслать!")


bot.polling()
