import telebot
import config22

bot = telebot.TeleBot(config22.TOKEN) 

# Start
@bot.message_handler(commands=['Hey'])
def send_start(message):
	bot.send_message(message.chat.id, '( >_<)')

  
#RUN
bot.polling(none_stop=True)
