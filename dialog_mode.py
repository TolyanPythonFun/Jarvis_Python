import pyttsx3
import random
import speech_recognition as sr

def dialog_how_are_you():
    good_responses = ['всё прекрасно',
                      'все нормально',
                      'всё хорошо',
                      'хорошо',
                      'живу',
                      'дышу',
                      'жевём',
                      'дышим']
    neitral_responses = ['ничего не меняется',
                         'не так и не так',
                         'даже не знаю, что ответить',
                         'да как то непонятно']
    bad_responses = ['бывало и лучше',
                     'так себе',
                     'плохо',
                     'в последнее время не очень']
    say_message(random.choice(['Всё прекрасно, а как у вас?',
                               'Всё нормально, а как у вас?',
                               'Всё хорошо, а как у вас?',
                               'Хорошо, а как у вас?']))
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    our_speech = r.recognize_google(audio, language="ru")

    if our_speech in ['что хорошего',
                      'что прекрасного',
                      'что нового',
                      'что нормального']:
        say_message(random.choice(['вас услышал',
                                   'зависать перестал',
                                   'разработчик наконец-то за меня взялся',
                                   'прочитал смешной анекдот',
                                   'я работаю и это уже само по себе хорошо',]))
    elif our_speech in good_responses:
        say_message(random.choice(['хорошо, когда всё хорошо',
                                   'мне бы ваш настрой',
                                   'рад за вас',
                                   'по кайфу']))
    elif our_speech in neitral_responses:
        say_message(random.choice(['я могу чем то помочь?',
                                   'даже не знаю, что и сказать на это',
                                   'вам надо развеяться, сходите погуляйте например',
                                   'какое то у вас подвешенное состояние']))






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

dialog_how_are_you()

