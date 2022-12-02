import pyttsx3
import speech_recognition as sr
import time
from datetime import datetime


def get_current_time():
    now = datetime.now()
    chasov = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    chas = [1, 21]
    chasa = [2, 3, 4, 22, 23]
    minut = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40,
             45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59]
    minuti = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]
    minuta = [1, 21, 31, 41, 51]
    if now.hour in chasov and now.minute in minut:
        say_message(f'Сейчас {str(now.hour)} часов {str(now.minute)} минут')
    elif now.hour in chasov and now.minute in minuti:
        say_message(f'Сейчас {str(now.hour)} часов {str(now.minute)} минуты')
    elif now.hour in chasov and now.minute in minuta:
        say_message(f'Сейчас {str(now.hour)} часов {str(now.minute)} минута')
    elif now.hour in chas and now.minute in minut:
        say_message(f'Сейчас {str(now.hour)} час {str(now.minute)} минут')
    elif now.hour in chas and now.minute in minuti:
        say_message(f'Сейчас {str(now.hour)} час {str(now.minute)} минуты')
    elif now.hour in chas and now.minute in minuta:
        say_message(f'Сейчас {str(now.hour)} час {str(now.minute)} минута')
    elif now.hour in chasa and now.minute in minut:
        say_message(f'Сейчас {str(now.hour)} часа {str(now.minute)} минут')
    elif now.hour in chasa and now.minute in minuti:
        say_message(f'Сейчас {str(now.hour)} часа {str(now.minute)} минуты')
    elif now.hour in chasa and now.minute in minuta:
        say_message(f'Сейчас {str(now.hour)} часа {str(now.minute)} минута')
    elif now.hour in chas and now.minute == 0:
        say_message(f'Сейчас {str(now.hour)} час ровно')
    elif now.hour in chasov and now.minute == 0:
        say_message(f'Сейчас {str(now.hour)} часов ровно')
    elif now.hour in chasa and now.minute == 0:
        say_message(f'Сейчас {str(now.hour)} часа ровно')


def get_seconds_count_in_year():
    now = datetime.now()
    say_message(f'В году {365 * 24 * 60 * 60} секунд')


def get_minutes_count_in_month():
    now = datetime.now()
    say_message(f'Ну если взять средний месяц продолжительностью в 30 дней, то в нём {30 * 24 * 60 * 60} секунд')


def turn_on_timer():
    say_message('Сколько засечь?')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    our_speech = r.recognize_google(audio, language="ru")
    if 'минут' in our_speech or 'минуты' in our_speech:
        time_value = int(str(our_speech).split()[0])
        say_message('Засекаю')
        time.sleep(time_value * 60)
        say_message('Время вышло')
    elif 'секунд' in our_speech or 'секунды' in our_speech:
        time_value = int(str(our_speech).split()[0])
        say_message('Засекаю')
        time.sleep(time_value)
        say_message('Время вышло')
    elif 'минуту' in our_speech:
        say_message('Засекаю')
        time.sleep(61)
        say_message('Время вышло')


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
