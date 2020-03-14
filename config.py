import telebot
token = ""
bot = telebot.TeleBot(token)

'''connect_db = ["localhost", "", "", ""]'''

connect_db = ["localhost", "", "", ""]

box = []
file = open("stopwords.txt", "r")
for f in file:
    box.append(f)