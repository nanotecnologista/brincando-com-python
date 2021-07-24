import telebot
import my_infos

token = my_infos.token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def diga_oi(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Olá, eu sou a J.B.O.T, a auxiliar da dr. Júlia, nanotecnologista.")
bot.polling()