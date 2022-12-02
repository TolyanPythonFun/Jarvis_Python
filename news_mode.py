import requests
import pyttsx3
import speech_recognition as sr

from bs4 import BeautifulSoup
from time import sleep


def get_world_news():
    '''
    Получает последние мировые новости
    '''
    url = 'https://ria.ru/world/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    link_list = []
    block_content = soup.find('div', class_='list list-tags').find_all('div', class_='list-item')

    for item in block_content:
        item_title = item.find('a', class_='list-item__title color-font-hover-only').text
        item_link = item.find('a', class_='list-item__title color-font-hover-only').get('href')
        link_list.append(item_link)
        say_message(item_title)

    say_message('Хотите узнать подробности?}')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    our_speech = r.recognize_google(audio, language="ru")

    if 'давай все по очереди' in str(our_speech).lower():

        for link in link_list:
            req = requests.get(url=link)
            soup = BeautifulSoup(req.text, 'lxml')
            content = soup.find_all('div', {'class': 'article__block', 'data-type': 'text'})

            for i in content:
                say_message(str(i.text).split('.')[1:])
                sleep(1)
            say_message('Следующая новость')
            sleep(1)

    elif 'давай только последнюю' in str(our_speech).lower():
        req = requests.get(url=link_list[0])
        soup = BeautifulSoup(req.text, 'lxml')
        content = soup.find_all('div', {'class': 'article__block', 'data-type': 'text'})

        for i in content:
            say_message(str(i.text).split('.')[1:])
            sleep(1)

    elif 'давай последние 5 новостей' in str(our_speech).lower() or \
            'давай последние пять новостей' in str(our_speech).lower():

        for link in link_list[:6]:
            req = requests.get(url=link)
            soup = BeautifulSoup(req.text, 'lxml')
            content = soup.find_all('div', {'class': 'article__block', 'data-type': 'text'})

            for i in content:
                say_message(str(i.text).split('.')[1:])
                sleep(1)

            say_message('Следующая новость')
            sleep(1)


def get_social_news():
    '''
    Получает последние новости общества
    '''
    url = 'https://ria.ru/society/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    link_list = []
    block_content = soup.find('div', class_='list list-tags').find_all('div', class_='list-item')

    for item in block_content:
        item_title = item.find('a', class_='list-item__title color-font-hover-only').text
        item_link = item.find('a', class_='list-item__title color-font-hover-only').get('href')
        link_list.append(item_link)
        say_message(item_title)

    say_message('Хотите узнать подробности?}')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    our_speech = r.recognize_google(audio, language="ru")

    if 'давай все по очереди' in str(our_speech).lower():

        for link in link_list:
            req = requests.get(url=link)
            soup = BeautifulSoup(req.text, 'lxml')
            content = soup.find_all('div', {'class': 'article__block', 'data-type': 'text'})

            for i in content:
                say_message(str(i.text).split('.')[1:])
                sleep(1)

            say_message('Следующая новость')
            sleep(1)

    elif 'давай только последнюю' in str(our_speech).lower():
        req = requests.get(url=link_list[0])
        soup = BeautifulSoup(req.text, 'lxml')
        content = soup.find_all('div', {'class': 'article__block', 'data-type': 'text'})

        for i in content:
            say_message(str(i.text).split('.')[1:])
            sleep(1)

    elif 'давай последние 5 новостей' in str(our_speech).lower() or \
            'давай последние пять новостей' in str(our_speech).lower():

        for link in link_list[:6]:
            req = requests.get(url=link)
            soup = BeautifulSoup(req.text, 'lxml')
            content = soup.find_all('div', {'class': 'article__block', 'data-type': 'text'})

            for i in content:
                say_message(str(i.text).split('.')[1:])
                sleep(1)

            say_message('Следующая новость')
            sleep(1)


def get_economy_news():
    '''
    Получает последние новости общества
    '''
    url = 'https://ria.ru/economy/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    link_list = []
    block_content = soup.find('div', class_='list list-tags').find_all('div', class_='list-item')

    for item in block_content:
        item_title = item.find('a', class_='list-item__title color-font-hover-only').text
        item_link = item.find('a', class_='list-item__title color-font-hover-only').get('href')
        link_list.append(item_link)
        say_message(item_title)

    say_message('Хотите узнать подробности?}')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    our_speech = r.recognize_google(audio, language="ru")

    if 'давай все по очереди' in str(our_speech).lower():

        for link in link_list:
            req = requests.get(url=link)
            soup = BeautifulSoup(req.text, 'lxml')
            content = soup.find_all('div', {'class': 'article__block', 'data-type': 'text'})

            for i in content:
                say_message(str(i.text).split('.')[1:])
                sleep(1)
            say_message('Следующая новость')
            sleep(1)

    elif 'давай только последнюю' in str(our_speech).lower():
        req = requests.get(url=link_list[0])
        soup = BeautifulSoup(req.text, 'lxml')
        content = soup.find_all('div', {'class': 'article__block', 'data-type': 'text'})

        for i in content:
            say_message(str(i.text).split('.')[1:])
            sleep(1)

    elif 'давай последние 5 новостей' in str(our_speech).lower() or \
            'давай последние пять новостей' in str(our_speech).lower():

        for link in link_list[:6]:
            req = requests.get(url=link)
            soup = BeautifulSoup(req.text, 'lxml')
            content = soup.find_all('div', {'class': 'article__block', 'data-type': 'text'})

            for i in content:
                say_message(str(i.text).split('.')[1:])
                sleep(1)

            say_message('Следующая новость')
            sleep(1)


def get_formula_1_news():
    '''
    Получает новости формулы-1
    '''
    url = 'https://www.f1news.ru/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    block_content = soup.find('ul', class_='list list_striped b-news-list__roll').find_all('li',                                                                                       class_='b-news-list__item')
    links = []

    for item in block_content:
        item_title = item.find('a', class_='b-news-list__title').text
        item_link = 'https://www.f1news.ru' + item.find('a', class_='b-news-list__title').get('href')
        links.append(item_link)
        say_message('Хотите узнать подробности?')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        our_speech = r.recognize_google(audio, language="ru")

        if 'давай все по очереди' in str(our_speech).lower():

            for link in links:
                response = requests.get(url=link)
                soup = BeautifulSoup(response.text, 'lxml')
                content = soup.find_all('p')

                for i in content:
                    say_message(i)

        elif 'давай только последнюю' in str(our_speech).lower():
            response = requests.get(url=links[0])
            soup = BeautifulSoup(response.text, 'lxml')
            content = soup.find_all('p')

            for i in content:
                say_message(i)

        elif 'давай последние 5 новостей' in str(our_speech).lower() or \
                'давай последние пять новостей' in str(our_speech).lower():

            for link in links[:6]:
                response = requests.get(url=link)
                soup = BeautifulSoup(response.text, 'lxml')
                content = soup.find_all('p')

                for i in content:
                    say_message(i)


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
