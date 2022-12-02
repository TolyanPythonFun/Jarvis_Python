from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import speech_recognition as sr
import random
import pyttsx3
import wikipedia


def open_google():
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

def open_youtube():
    say_message("Открываю youtube")
    url = 'https://www.youtube.com'
    driver = webdriver.Firefox(executable_path='C:\\Программирование\\Jarvis\\geckodriver.exe', )
    driver.get(url=url)
    time.sleep(1)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        say_message('Что нужно найти на YouTube?')
        audio = r.listen(source)
    our_speech = r.recognize_google(audio, language="ru")
    print("[log] Распознано " + our_speech)
    search_input = driver.find_element(By.NAME, 'search_query')
    search_input.clear()
    search_input.send_keys(our_speech)
    time.sleep(5)
    search_input.send_keys(Keys.ENTER)


def open_wiki():
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