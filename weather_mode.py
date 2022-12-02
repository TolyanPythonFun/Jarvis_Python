import time

import pyttsx3
import requests
import json
import speech_recognition as sr
from pyowm import OWM
# from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps


def say_weather_world():  # функция для определения погоды в любом городе мира
    gradus = [-31, -21, -1, 1, 21, 31]
    gradusa = [-2, 2, -3, 3, -4, 4, -22, 22, -23, 23, -24, 24, -32, 32, -33, 33, -34, 34]
    gradusov = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, -5, -6, -7, -8,
                -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -25, -26, -27, -28, -29, -30, -35]
    say_message('Какой город Вас интересует?')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    our_speech = r.recognize_google(audio, language="ru")
    print("Город " + our_speech)
    # config_dict = get_default_config()
    # config_dict['language'] = 'ru'
    # owm = OWM('5f4f8634f13a4d83e88fc3970c8a7caf', config_dict)
    owm = OWM('5f4f8634f13a4d83e88fc3970c8a7caf')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(our_speech)
    w = observation.weather
    temp_dict_celsius = w.temperature('celsius')
    numb_round = temp_dict_celsius['temp']
    if our_speech == 'санкт-петербург' or our_speech == 'Питер':
        if round(numb_round) in gradusov:
            say_message('В северной столице сейчас ' + w.detailed_status + ', температура примерно ' + str(
                round(numb_round)) + ' градусов')
        elif round(numb_round) in gradusa:
            say_message('В северной столице ' + w.detailed_status + ', температура примерно ' + str(
                round(numb_round)) + ' градусa')
        elif round(numb_round) in gradus:
            say_message('В северной столице сейчас ' + w.detailed_status + ', температура примерно ' + str(
                round(numb_round)) + ' градус')
        elif round(numb_round) == 0:
            say_message('В северной столице сейчас ' + w.detailed_status + ', не тепло не холодно')
    elif our_speech == 'Москва':
        if round(numb_round) in gradusov:
            say_message('На родине Кремля сейчас ' + w.detailed_status + ', температура примерно ' + str(
                round(numb_round)) + ' градусов')
        elif round(numb_round) in gradusa:
            say_message('На родине Кремля сейчас ' + w.detailed_status + ', температура примерно ' + str(
                round(numb_round)) + ' градусa')
        elif round(numb_round) in gradus:
            say_message('На родине Кремля сейчас ' + w.detailed_status + ', температура примерно ' + str(
                round(numb_round)) + ' градус')
        elif round(numb_round) == 0:
            say_message('На родине Кремля сейчас ' + w.detailed_status + ', не тепло не холодно')
    else:
        if round(numb_round) in gradusov:
            say_message(
                'Там сейчас ' + w.detailed_status + ', температура примерно ' + str(round(numb_round)) + ' градусов')
        elif round(numb_round) in gradusa:
            say_message(
                'Там сейчас ' + w.detailed_status + ', температура примерно ' + str(round(numb_round)) + ' градусa')
        elif round(numb_round) in gradus:
            say_message(
                'Там сейчас ' + w.detailed_status + ', температура примерно ' + str(round(numb_round)) + ' градус')
        elif round(numb_round) == 0:
            say_message('Там сейчас ' + w.detailed_status + ', не тепло не холодно')


def say_weather_home():  # функция для определения погоды в Череповце
    gradus = [-31, -21, -1, 1, 21, 31]
    gradusa = [-2, 2, -3, 3, -4, 4, -22, 22, -23, 23, -24, 24, -32, 32, -33, 33, -34, 34]
    gradusov = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, -5, -6, -7, -8,
                -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -25, -26, -27, -28, -29, -30, -35]
    url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/DmkJecT1AQFLiNzjelrM0O2eCwd3I6A1'
    response = requests.get(url)
    print(response)
    #url = f'http://api.openweathermap.org/geo/1.0/direct?q=Череповец&appid=5f4f8634f13a4d83e88fc3970c8a7caf'
    #response = requests.get(url)
    #print(response.json()[0]['lat'])
    #print(response.json()[0]['lon'])
    #time.sleep(2)
    #link = 'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=5f4f8634f13a4d83e88fc3970c8a7caf'
    #result = requests.get(link)
    #print(result.json())

    # # config_dict = get_default_config()
    # # config_dict['language'] = 'ru'
    # # owm = OWM('5f4f8634f13a4d83e88fc3970c8a7caf', config_dict)
    # owm = OWM('5f4f8634f13a4d83e88fc3970c8a7caf')
    # mgr = owm.weather_manager()
    # observation = mgr.weather_at_place('Череповец')
    # w = observation.weather
    # temp_dict_celsius = w.temperature('celsius')
    # numb_round = temp_dict_celsius['temp']
    # if round(numb_round) in gradusov:
    #     say_message(
    #         'У нас сейчас ' + w.detailed_status + ', температура примерно ' + str(round(numb_round)) + ' градусов')
    # elif round(numb_round) in gradusa:
    #     say_message(
    #         'У нас сейчас ' + w.detailed_status + ', температура примерно ' + str(round(numb_round)) + ' градусa')
    # elif round(numb_round) in gradus:
    #     say_message(
    #         'У нас сейчас ' + w.detailed_status + ', температура примерно ' + str(round(numb_round)) + ' градус')
    # elif round(numb_round) == 0:
    #     say_message('У нас сейчас ' + w.detailed_status + ', не тепло не холодно')


def say_message(message):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(message)
    engine.runAndWait()
