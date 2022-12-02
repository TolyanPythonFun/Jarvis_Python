import time
import time_mode
import translator_mode
import exchange_rates_mode
import web_browser_mode
import age_mode
import news_mode
import open_file_mode
import dictionary_mode
import russian_words_mode
import country_list_mode
import speech_recognition as sr
import os
import json
import pyaudio
import pyttsx3
import keyboard as kb
import requests
import wikipedia
import pyautogui
import random
import weather_mode
import subprocess

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

names = ['jarvis', 'Jarvis', 'Джарвис', 'джарвис', 'жарвис', 'Жарвис']
key_words_del = {
    'pause': ['подожди', 'погоди', 'подождём', 'перекур', 'покурим', 'помолчи']
}

option = webdriver.FirefoxOptions()
option.headless = True


def listen_command():  # функция для прослушивания команд
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Что вам угодно: ")
        audio = r.listen(source)
    try:
        our_speech = str(r.recognize_google(audio, language="ru-RU")).lower()
        for name in names:
            if name in our_speech:
                our_speech.replace(name, '')

        print("[log] Распознано " + our_speech)

        return our_speech
    except sr.UnknownValueError:
        listen_command()
    except AttributeError:
        listen_command()


action_words = [
    'включи', 'включай', 'открой', 'открывай', 'вруби', 'врубай', 'найди', 'ищи', 'считай', 'посчитай'
]

cmds = {
    'timer': ['включи таймер', 'засеки время', 'вруби таймер', 'надо засечь время', 'нужно засечь время',
              'засеки время пожалуйста', 'таймер'],
    'telegram': ['telegram', 'телеграм'],
    'virtual_box': ['virtualbox', 'virtual box', 'открой virtualbox', 'включи virtualbox'],
    'elpy': ['включи релакс', 'включи птичек', 'включи звуки природы', 'хочу послушать природу'],
    'age': ['сколько тебе лет', 'твой возраст', 'какой у тебя возраст', 'какой твой возраст', 'сколько лет тебе'],
    'youtube': ['открой youtube', 'youtube', 'ютуб', 'включи youtube', 'открой пожалуйста youtube',
                'открой youtube пожалуйста'],
    'photoshop': ['photoshop', 'открой фотошоп', 'открой photoshop', 'photoshop пожалуйста',
                  'открой photoshop пожалуйста'],
    'table': ['открой таблицу расходов', 'открой таблицу доходов', 'открой таблицу доходов расходов',
              'открой таблицу расходов доходов'],
    'now_time': ['сколько время', 'который час', 'текущее время', 'сколько на часах', 'что по времени'],
    'steam': ['вруби стим', 'включи steam', 'steam включи', 'врубай steam'],
    'appetit': ['мы пошли завтракать', 'мы пошли обедать', 'мы пошли ужинать', 'мы пошли кушать', 'мы кушать пошли'],
    'google': ['открой google', 'включи google', 'надо загуглить кое-что', 'google в помощь'],
    'shoutdown': ['выключай комп', 'выключи комп', 'вырубай комп', 'выруби комп', 'выключи компьютер',
                  'выключай компьютер', 'выключай ноутбук', 'выключи ноутбук', 'вырубай ноутбук', 'выруби ноутбук'],
    'translate': ['переведи', 'нужен переводчик', 'переведи кое-что', 'надо перевести кое-что',
                  'надо кое-что перевести'],
    'how_are_you': ['как дела', 'как оно', 'как делишки'],
    'what_you_can': ['что ты умеешь', 'что ты можешь', 'на что ты способен'],
    'notepad': ['открой блокнот', 'включи блокнот'],
    'write_to_notepad': ['хочу кое-что записать', 'хочу записать кое-что', 'нужно записать кое-что',
                         'нужно кое-что записать'],
    'wikipedia': ['включи википедию', 'включи wikipedia' 'нужна wikipedia', 'надо узнать значение слова',
                  'нужно узнать значение слова', 'открой википедию'],
    'bye': ['пока', 'до завтра', 'бывай'],
    'repeat': ['повторяй за мной', 'повтори', 'повторяй', 'режим попугая', 'врубай режим попугая',
               'включай режим попугая'],
    'exchange_rate': ['сколько валюта стоит', 'какой курс валют', 'сколько стоит валюта', 'курс валют',
                      'курс валюты', 'узнай курс валют'],
    'afisha': ['что сейчас в кино', 'что сейчас идёт в кино', 'что сейчас идёт в кинотеатрах',
               'что сейчас идёт в кинотеатре'],
    'what_your_name': ['как тебя зовут', 'как твоё имя', 'как тебя называют', 'у тебя есть имя', 'как твое имя'],
    'weather_home': ['какая сегодня погода', 'как погода', 'какая погода', 'как сегодня за окном', 'как на улице',
                     'как сегодня на улице'],
    'weather_world': ['как в мире погода', 'как погода в мире', 'что в мире с погодой', 'как погода за границей'],
    'jarvis_cool': ['ты молодец', 'красавчик', 'ты лучший', 'ты очень умный'],
    'igra_v_goroda': ['давай в города', 'сыграем в города', 'как насчёт в города сыграть', 'как насчёт в города',
                      'в города сыграем', 'а может в города'],
    'poschitay': ['посчитай', 'сосчитай'],
    'pause': ['на паузу', 'перерыв', 'пауза', 'помолчи немного', 'дай мне побыть одному', 'мне нужна тишина',
              'отдохни я позову']
}

how_are_you = [
    'спросите у моего разработчика',
    'неплохо, а как у вас?'
]

goodbye = ['всего хорошего', 'досвидания', 'зовите, если понадоблюсь']

my_affairs_good = ['хорошо', 'прекрасно', 'замечательно', 'лучше всех', 'good', 'супер', 'нормально']
my_affairs_no_good = ['плохо', 'всё плохо', 'очень плохо', 'так себе', 'не очень']


def do_this_command(message: str):
    if type(message) == None:
        message = str(message).lower()
    try:
        if len(str(message)) == 0:
            print('[log] --> Вы ничего не сказали')
        else:
            if 'включи' in message:
                message = str(message).split(' ')[1]
                if message in cmds['telegram']:
                    open_file_mode.open_telegram()

            elif 'открой' in message:
                if 'папку' in message:
                    message = str(message).split('папку')[-1]
                elif 'командную строку' in message:
                    with pyautogui.hold('win'):
                        pyautogui.press('r')
                    time.sleep(1)
                    pyautogui.moveTo(203, 277)
                    pyautogui.click()
                    say_message('Готово')
                elif 'настройки windows' in message or 'параметры windows' in message:
                    with pyautogui.hold('win'):
                        pyautogui.press('i')

            elif 'режим гибернации' in message:
                say_message('Режим гибернации')
                say_message(random.choice(goodbye))
                os.system("shutdown /h")
                exit()

            elif 'сколько' in message:
                if 'мы живём' in message.replace('сколько', ''):
                    age_mode.get_our_age()

            elif 'нужны последние новости' in message:
                if 'в мире' in message:
                    news_mode.get_world_news()
                elif 'в обществе' in message:
                    news_mode.get_social_news()
                elif 'в экономике' in message:
                    news_mode.get_economy_news()
                elif 'в формуле 1' in message or 'в формуле-1' in message:
                    news_mode.get_formula_1_news()

            elif 'столицей какой страны является город' in message:
                message = str(message).replace('столицей какой страны является город ', '').title().strip()
                print(message)
                country_list_mode.get_country(message)

            elif 'какая столица у' in message:
                message = str(message).replace('какая столица у ', '')
                country_list_mode.get_capital(message)

            elif 'столица' in message:
                message = str(message).replace('столица ', '')
                country_list_mode.get_capital(message)

            elif 'что является столицей' in message:
                message = str(message).replace('что является столицей ', '')
                country_list_mode.get_capital(message)

            elif 'кто такой' in message or 'кто такая' in message or 'кто такие' in message:
                message = str(message).replace('кто такой', '')
                message = str(message).replace('кто такая', '')
                message = str(message).replace('кто такие', '')
                key_phrases = ['сейчас найдём', 'мне даже самому интересно стало']
                say_message(random.choice(key_phrases))
                wikipedia.set_lang('ru')
                wiki_page = wikipedia.page(message)
                time.sleep(1)
                say_message(wiki_page.summary)

            elif 'назови' in message:
                if 'слово' in message:
                    if 'короткое' in message:
                        russian_words_mode.get_word(0, 10)
                    elif 'длинное' in message:
                        russian_words_mode.get_word(15, 40)
                    else:
                        say_message('Я полагаю, что вам нужно что-то среднее, например ...')
                        russian_words_mode.get_word(10, 15)

            elif 'что такое' in message or 'что значит' in message or 'что означает' in message:
                message = str(message.replace('что такое', '')).strip()
                dictionary_mode.value_word(message)

            for word in message.split(' '):
                if word in key_words_del['pause']:
                    message = message.replace(word, '')
                    count_minutes = int(message.split(' ')[1])
                    time.sleep(count_minutes)

            if message in cmds['photoshop']:
                say_message("Открываю фотошоп")
                os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe")

            elif message in cmds['notepad']:
                say_message('Открываю блокнот')
                os.startfile('C:\\Windows\\system32\\notepad.exe')

            elif message in cmds['age']:
                age_mode.get_age()

            elif message in cmds['timer']:
                time_mode.turn_on_timer()

            elif message in cmds['notepad']:
                say_message('Открываю блокнот')
                os.startfile('C:\\Windows\\system32\\notepad.exe')

            elif message in cmds['write_to_notepad']:
                screenWidth, screenHeight = pyautogui.size()
                notepad = ['notepad', 'блокнот', 'давай notepad', 'пожалуй notepad', 'давай блокнот', 'пожалуй блокнот']
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                our_speech = r.recognize_google(audio, language="ru")
                try:
                    if our_speech in notepad:
                        say_message('Открываю блокнот')
                        say_message('Диктуйте, что нужно записать, я запишу, озвучу и сохраню в файл')
                        os.startfile('C:\\Windows\\system32\\notepad.exe')
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            audio = r.listen(source)
                        our_speech = r.recognize_google(audio, language="ru")
                        new_our_speech = our_speech.replace(' запятая ', ', ')\
                            .replace(' точка ', '. ')\
                            .replace('тире ', '-')\
                            .replace('двоеточие ', ':')\
                            .replace('перенос строки', '\n')
                        try:
                            with open('text.txt', 'w') as file:
                                pyautogui.moveTo(screenWidth / 2, screenHeight / 2, duration=0.5)
                                kb.write(new_our_speech, delay=0.01)
                            say_message(our_speech)
                        except:
                            say_message('Продолжаем работу')
                    else:
                        say_message('Я не совсем понимаю вас')
                except sr.UnknownValueError:
                    return "Не распознано"
                except sr.RequestError as ex:
                    return "Не распознано"

            elif message in cmds['what_you_can']:
                say_message('так всего и не упомнишь')
                say_message('много чего могу')

            elif message in cmds['telegram']:
                open_file_mode.open_telegram()

            elif message in cmds['weather_home']:
                weather_mode.say_weather_home()

            elif message in cmds['weather_world']:
                weather_mode.say_weather_world()

            elif message in cmds['how_are_you']:
                say_message(how_are_you[1])
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                our_speech = r.recognize_google(audio, language="ru")
                if our_speech in my_affairs_good:
                    say_message('Рад за вас')
                elif our_speech in my_affairs_no_good:
                    say_message('Не переживайте, всё наладится')

            elif message in cmds['steam']:
                say_message('Открываю Steam')
                os.startfile('C:\\Program Files (x86)\\Steam\\Steam.exe')

            elif message in cmds['translate']:
                translator_mode.translate()

            elif message in cmds['shoutdown']:
                say_message('Компьютер выключится в течение минуты')
                os.system("shutdown -s")

            elif message in cmds['google']:
                say_message("Открываю браузер")
                url = 'https://www.google.com'
                driver = webdriver.Firefox(executable_path='C:\\Программирование\\Jarvis\\geckodriver.exe', )
                driver.get(url=url)
                time.sleep(1)
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    search_words = ['что ищем?', 'что нужно найти?', 'озвучте ваш запрос', 'что гуглим?']
                    say_message(random.choice(search_words))
                    audio = r.listen(source)
                our_speech = r.recognize_google(audio, language="ru")
                print("[log] Распознано " + our_speech)
                search_input = driver.find_element(By.NAME, 'q')
                search_input.clear()
                search_input.send_keys(our_speech)
                time.sleep(5)
                search_input.send_keys(Keys.ENTER)

            elif message in cmds['what_your_name']:
                Alina = ['Алина', 'Алинка', 'Лиса', 'Алиночка', 'Алина Андреевна']
                Tolya = ['Толя', 'Анатолий', 'Толян', 'Толик', 'Толянчик', 'Анатолий Андреевич']
                Jarvis = ['Меня зовут Jarvis', 'Мое имя Jarvis',
                          'Меня назвали Jarvis в честь одноимённого помощника из фильма железный человек', 'Я Jarvis',
                          'Jarvis']
                say_message(random.choice(Jarvis))
                say_message('А как зовут Вас?')
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                our_speech = r.recognize_google(audio, language="ru")
                if our_speech in Tolya:
                    say_message('Рад с вами познакомиться, создатель')
                elif our_speech in Alina:
                    say_message('Приятно познакомиться, у вас очень красивое имя')
                    say_message('Мой создатель очень много о вас рассказывал')
                    say_message('Ну разумеется, только хорошего')
                else:
                    say_message('Я вас не знаю')
                    say_message('Кем вы приходитесь моему создателю')

            elif message in cmds['exchange_rate']:
                exchange_rates_mode.get_current_rate()

            elif message in cmds['exchange_rate']:
                exchange_rates_mode.get_current_rate()

            elif message in cmds['wikipedia']:
                key_words_dict = ['что ищем?', 'что нужно найти?', 'ищете что-то конкретное?']
                say_message(random.choice(key_words_dict))
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                our_speech = r.recognize_google(audio, language="ru").lower()
                key_phrases = ['сейчас найдём', 'мне даже самому интересно стало', '']
                say_message(random.choice(key_phrases))
                wikipedia.set_lang('ru')
                wiki_page = wikipedia.page(our_speech)
                say_message('Заголовок страницы ' + wiki_page.title)
                time.sleep(2)
                say_message('Краткое содержание статьи ' + wiki_page.summary)

            elif message in cmds['youtube']:
                web_browser_mode.open_youtube()

            elif message in cmds['poschitay']:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    say_message('До скольки посчитать?')
                    audio = r.listen(source)
                our_speech = r.recognize_google(audio, language="ru")
                print("[log] Посчитать до " + our_speech)
                nums = 1
                while nums <= int(our_speech):
                    say_message(nums)
                    nums += 1
                say_message('Подсчёт окончен')

            elif message in cmds['now_time']:
                time_mode.get_current_time()

            elif message in cmds['appetit']:
                say_message('Приятного аппетита')

            elif message in cmds['bye']:
                say_message(random.choice(goodbye))
                exit()

            elif message in cmds['repeat']:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                our_speech = r.recognize_google(audio, language="ru")
                say_message(our_speech)
    except AttributeError:
        return 'Хьюстон, у нас проблемы'


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


if __name__ == '__main__':
    now = datetime.now()
    good_morning = ['Доброе утро', 'С добрым утром', 'Приветствую', 'Здравствуйте']
    good_afternoon = ['Добрый день', 'Приветствую', 'Здравствуйте']
    good_evening = ['Добрый вечер', 'Приветствую', 'Здравствуйте']

    if now.hour >= 4 and now.hour < 12:
        say_message(random.choice(good_morning) + ', Jarvis слушает')
    elif now.hour >= 12 and now.hour <= 16:
        say_message(random.choice(good_afternoon) + ', Jarvis слушает')
    elif now.hour >= 16 and now.hour <= 23:
        say_message(random.choice(good_evening) + ', Jarvis слушает')
    else:
        say_message('Приветствую, Jarvis слушает')
    while True:
        try:
            command = listen_command()
            do_this_command(command)
        except Exception as ex:
            print(ex)


