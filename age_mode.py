import pyttsx3
from datetime import datetime


def get_age():
    birth_day = datetime(2021, 9, 22)
    now_date = datetime.now()
    delta = birth_day - now_date
    count_days = str(delta.days).strip('-')
    count_hours = str(delta)
    say_message(count_days + 'дней')


def get_our_age():
    birth_day = datetime(1995, 7, 15, 0, 15, 0)
    now_date = datetime.now()
    delta = now_date - birth_day
    say_message(f'Анатолий, вы живёте {str(delta).split()[0]} день, /'
        f' {(str(delta).split()[2]).split(":")[0]} часов /'
        f'{(str(delta).split()[2]).split(":")[1]} /'
        f'минут и {((str(delta).split()[2]).split(":")[2]).split(".")[0]} секунд')

    say_message(f'Анатолий, вы живёте {str(delta).split()[0]} дней, /'
                f' {(str(delta).split()[2]).split(":")[0]} часов /'
                f'{(str(delta).split()[2]).split(":")[1]} /'
                f'минут и {((str(delta).split()[2]).split(":")[2]).split(".")[0]} секунд')

    birth_day = datetime(1998, 7, 21, 14, 55, 0)
    now_date = datetime.now()
    delta = now_date - birth_day
    say_message(f'Алина, вы живёте {str(delta).split()[0]} дней, /'
                f' {(str(delta).split()[2]).split(":")[0]} часа /'
                f'{(str(delta).split()[2]).split(":")[1]} минут и /'
                f'{((str(delta).split()[2]).split(":")[2]).split(".")[0]} секунд')


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
