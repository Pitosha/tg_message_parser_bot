import config as c
import random
import chat
from time import sleep
from telebot import types


#Обработка первого появления Бота в чате
@c.bot.message_handler(content_types=['new_chat_members'])
def reg_cchat(message):
    if message.new_chat_member.id == c.bot.get_me().id:
        target_chat = chat.Chat(message.chat.id)
        check_chat = target_chat.init_chat("chat")

        if check_chat is False:
            target_chat.create_chat(message)
            c.bot.send_message(message.chat.id, "Вы зарегали чат, скоро Эрек напишет правила")
            print("Прошла регистрация в чате ", message.chat.title)
        else:
            c.bot.send_message(message.chat.id, "Бот уже зарегистрировал ваш чат")
        

#Обработка удаления Бота из чата
@c.bot.message_handler(content_types=['left_chat_member'])
def delete_chat(message):
    if message.left_chat_member.id == c.bot.get_me().id:
        target_chat = chat.Chat(message.chat.id)
        check_chat = target_chat.init_chat("chat")

        if check_chat is True:
            target_chat.delete_chat(message.chat.id)
            #тут сообщение выдает ошибку
            print("Прошло удаление бота в чате ", message.chat.title)


#Обработка команды включения бота
@c.bot.message_handler(commands=["start_bot"])
def start(message):
    if message.chat.type == "private":
        pass
    else:
        #Вызов класса Чат
        target_chat = chat.Chat(message.chat.id)
        #Проверка чата на существование
        check_chat = target_chat.init_chat("bool")

        #Если чат существует в БД то:
        if check_chat is True:
            this_chat = target_chat.init_chat("obj")

            admins = c.bot.get_chat_administrators(message.chat.id)
            for i in admins:
                if i.user.id == message.from_user.id:
                    if this_chat[3] == "No":
                        target_chat.update_chat(this_chat[0], this_chat[1], this_chat[2], "Yes")
                        c.bot.send_message(message.chat.id, "Бот включен")
                    elif this_chat[3] == "Yes":
                        c.bot.send_message(message.chat.id, "В этом чате бот уже включен")

        else:
            c.bot.send_message(message.chat.id, "Ваш чат не зарегестрирован")

#Обработка команды выключения бота
@c.bot.message_handler(commands=["stop_bot"])
def start(message):
    if message.chat.type == "private":
        pass
    else:
        #Вызов класса Чат
        target_chat = chat.Chat(message.chat.id)
        #Проверка чата на существование
        check_chat = target_chat.init_chat("bool")

        #Если чат существует в БД то:
        if check_chat is True:
            this_chat = target_chat.init_chat("obj")

            admins = c.bot.get_chat_administrators(message.chat.id)
            for i in admins:
                if i.user.id == message.from_user.id:
                    if this_chat[3] == "Yes":
                        target_chat.update_chat(this_chat[0], this_chat[1], this_chat[2], "No")
                        c.bot.send_message(message.chat.id, "Бот выключен")
                    elif this_chat[3] == "No":
                        c.bot.send_message(message.chat.id, "В этом чате бот НЕ включен")

        else:
            c.bot.send_message(message.chat.id, "Ваш чат не зарегестрирован")

#Обработка команды включения служебных сообщений бота
@c.bot.message_handler(commands=["start_alert_mes"])
def start(message):
    if message.chat.type == "private":
        pass
    else:
        #Вызов класса Чат
        target_chat = chat.Chat(message.chat.id)
        #Проверка чата на существование
        check_chat = target_chat.init_chat("bool")

        #Если чат существует в БД то:
        if check_chat is True:
            this_chat = target_chat.init_chat("obj")

            admins = c.bot.get_chat_administrators(message.chat.id)
            for i in admins:
                if i.user.id == message.from_user.id:
                    if this_chat[2] == "No":
                        target_chat.update_chat(this_chat[0], this_chat[1], "Yes", this_chat[3])
                        c.bot.send_message(message.chat.id, "Системные сообщения включены")
                    elif this_chat[2] == "Yes":
                        c.bot.send_message(message.chat.id, "В этом чате уже включены системные сообщения")

        else:
            c.bot.send_message(message.chat.id, "Ваш чат не зарегестрирован")
        
#Обработка команды выключения служебных сообщений бота
@c.bot.message_handler(commands=["stop_alert_mes"])
def start(message):
    if message.chat.type == "private":
        pass
    else:
        #Вызов класса Чат
        target_chat = chat.Chat(message.chat.id)
        #Проверка чата на существование
        check_chat = target_chat.init_chat("bool")

        #Если чат существует в БД то:
        if check_chat is True:
            this_chat = target_chat.init_chat("obj")

            admins = c.bot.get_chat_administrators(message.chat.id)
            for i in admins:
                if i.user.id == message.from_user.id:
                    if this_chat[2] == "Yes":
                        target_chat.update_chat(this_chat[0], this_chat[1], "No", this_chat[3])
                        c.bot.send_message(message.chat.id, "Системные сообщения выключены")
                    elif this_chat[2] == "No":
                        c.bot.send_message(message.chat.id, "В этом чате уже вЫключены системные сообщения")

        else:
            c.bot.send_message(message.chat.id, "Ваш чат не зарегестрирован")


@c.bot.message_handler(content_types=['text'])
def chat_nessage_hendler(message):
    #Если сообщение пришло в ЛК
    if message.chat.type == "private":
        pass

    #Если сообщение пришло в чат
    else:
        #Вызов класса Chat
        target_chat = chat.Chat(message.chat.id)
        #Выбираем обьект Чата из БД
        check_chat = target_chat.init_chat("obj")

        if check_chat[3] != "No":

            i = 0

            while i <= len(c.box):
                if c.box[i][0:-1] in message.text:
                    break
                i += 1

                if i == len(c.box):

                    c.bot.delete_message(message.chat.id, message.message_id)

                    if check_chat[2] != "No":
                        
                        #Это сообщение обьясняет причину удаления сообщения юзера
                        c.bot.send_message(message.chat.id, "заткнись сука")
                        break
                    else:
                        break


if __name__ == "__main__":
    try:
        c.bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        print("чета не работает")
        sleep(20)