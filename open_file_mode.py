import pyttsx3
import os


def open_telegram():
    say_message('Открываю телеграм')
    os.startfile('C:\\Users\\ASUS\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe')


def open_virtual_vox():
    say_message('Открываю Virtual Box')
    os.startfile('C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe')


def open_elpy():
    os.startfile('C:\\Users\\ASUS\\OneDrive\\Desktop\\Elpy.lnk')


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
