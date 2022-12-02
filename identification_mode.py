import speech_recognition as sr
import pyttsx3


def identification_user():
    my_passwords = ['рыба-меч', 'рыба меч']
    passwords_Alina = ['Мумий Тролль', 'мумий тролль']
    say_message('Требуется идентификация')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    our_speech = r.recognize_google(audio, language="ru")
    print(our_speech)
    if our_speech in my_passwords:
        say_message('Идентификацияя пройдена успешно')
        say_message('Доступ разрешен')
        say_message('С возвращением, сэр!')
    elif our_speech in passwords_Alina:
        say_message('Идентификацияя пройдена успешно')
        say_message('Доступ разрешен')
        say_message('Алина, здравствуйте, я к вашим услугам')
    else:
        say_message('В доступе отказано')
        exit()


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
