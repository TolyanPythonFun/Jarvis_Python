import pyttsx3
from time import sleep
import speech_recognition as sr
from random import choice


def get_word(start: int, finish: int):
    words = []
    with open('russian_nouns.txt', encoding='utf-8') as file:
        for line in file.readlines():
            if len(line) > start and len(line) < finish and '-' not in line:
                words.append(line)
        w = choice(words)
        print(w)
        say_message(w)



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
