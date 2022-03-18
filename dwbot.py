import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_config_from
config_dict = get_config_from('defo.json')

owm = OWM('', config_dict)
mgr = owm.weather_manager()






bot = telebot.TeleBot("5122770218:AAH7S776q9_0mmzimMinvVrmt5-qvxmjhX0", parse_mode=None)

@bot.message_handler(commands=['start', 'pogoda'])
def send_welcome(message):
	bot.reply_to(message, "Я погодный бот. В каком городе смотрим погоду? Используйте символ $ перед названием города.")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	city = message.text
	if city.startswith("$"):
		city = city[1:]
		observation = mgr.weather_at_place( city )
		w = observation.weather
		temp = w.temperature('celsius')["temp"]
		hum = w.humidity
		clo = w.detailed_status	
		answer =  "В городе " + city + " " +clo + "\n"
		answer += "Температура за окном " + str(temp) + "°C, " + "\n"
		answer += "Относительная влажность " + str(hum) + "%" + "\n"
		bot.reply_to(message, answer)

bot.infinity_polling()