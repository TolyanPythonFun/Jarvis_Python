import pyttsx3
import json


def get_capital(message):
    with open(file='capitals_of_counties.json', mode='r', encoding='utf-8') as file:
        capitals = json.load(file)
    say_message(f'Столицей {message} является {capitals[message]}')


def get_country(message):
    with open(file='capitals_of_counties.json', mode='r', encoding='utf-8') as file:
        capitals = json.load(file)
        # print(message)
        for key, value in capitals.items():
            if message in value:
                say_message(f'Город {message} это столица {key}')
                break
        else:
            say_message(f'Мне неизвестна страна, столицей которой является город {message}. Возможно вы ошиблись и назвали не столицу, а просто город.')


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
