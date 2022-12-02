import requests
from bs4 import BeautifulSoup
import random
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def value_word(message):
    try:
        # say_message(random.choice(['секунду', 'один момент']))
        url = f'https://makeword.ru/dictionary/{message}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        dicts_name = soup.find_all('p')
        items = []
        plus = [items.append(str(item.text).replace('—', 'это')) for item in dicts_name if
                message.title() in item.text and '...' not in item.text]
        say_message(random.choice(items))
    except:
        say_message(random.choice(['не могу найти', 'к сожалению я не знаю']))
        say_message('Могу посмотреть в интернете')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        our_speech = r.recognize_google(audio, language="ru")
        speeches = ['давай', 'ну давай', 'посмотри']
        if our_speech in speeches:
            url = 'https://www.google.com'
            driver = webdriver.Firefox(executable_path='C:\\Программирование\\Jarvis\\geckodriver.exe')
            driver.get(url=url)
            try:
                search_input = driver.find_element(By.NAME, 'q')
                search_input.clear()
                search_input.send_keys(f'define:{message}')
                search_input.send_keys(Keys.ENTER)
                sleep(2)
                description_word = driver.find_element(By.CLASS_NAME, 'kno-rdesc').find_element(By.TAG_NAME, 'span')
                say_message(description_word.text)
            except:
                search_input = driver.find_element(By.NAME, 'q')
                search_input.clear()
                search_input.send_keys(f'define:{message}')
                search_input.send_keys(Keys.ENTER)
                sleep(2)
                description_word = driver.find_element(By.XPATH, '/html/body/div[8]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/span/div/div/div[3]/div/div[3]/div/div/ol/li/div/div/div[1]/div/div/div/div[1]/span')
                say_message(description_word.text)
            driver.close()


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
