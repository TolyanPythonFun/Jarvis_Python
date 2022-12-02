import pyttsx3
import speech_recognition as sr
import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def translate():
    key_words_translate = ['хорошо', 'открываю браузер', 'секунду', 'мне нужно немного времени',
                                       'сейчас переведу']
    key_words_translate_1 = ['спрошу у гугла', 'google в помощь', 'сейчас найду google переводчик',
                             'пусть google переводит']
    key_words_translate_2 = ['что нужно перевести?', 'что перевести?', 'что переводим?',
                             'назовите слово или фразу для перевода']
    say_message(random.choice(key_words_translate))
    url = 'https://www.google.com'
    driver = webdriver.Firefox(executable_path='C:\\Программирование\\Jarvis\\geckodriver.exe')
    driver.get(url=url)
    say_message(random.choice(key_words_translate_1))
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    our_speech = r.recognize_google(audio, language="ru", show_all=True)
    search_input = driver.find_element(By.NAME, 'q')
    search_input.clear()
    search_input.send_keys('google переводчик')
    search_input.send_keys(Keys.ENTER)
    say_message(random.choice(key_words_translate_2))
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        our_speech = r.recognize_google(audio, language="en")
        eng_input = driver.find_element(By.ID, 'tw-source-text-ta')
        eng_input.send_keys(our_speech)
        time.sleep(2)
        transleted_word_teg = driver.find_element(By.XPATH, '//*[@id="tw-target-text"]/span')
        transleted_word = transleted_word_teg.text
        say_message(our_speech + ' переводится ' + transleted_word)
        driver.close()
    except sr.UnknownValueError:
        return "Не распознано"
    except sr.RequestError as ex:
        return "Не распознано"

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
