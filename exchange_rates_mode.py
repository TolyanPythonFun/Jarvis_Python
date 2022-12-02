import pyttsx3
import speech_recognition as sr
from datetime import datetime
import requests
import time


def get_current_rate():
    now = datetime.now()
    rubl = [1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131]
    rubley = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39,
              40,
              45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86,
              87, 88, 89, 90, 95, 96, 97, 98, 99, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
              118, 119, 120]
    rublya = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94,
              102, 103, 104, 122, 123, 124]
    kopeek = [0, 00, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38,
              39, 40,
              45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86,
              87, 88, 89, 90, 95, 96, 97, 98, 99]
    kopeyka = [1, 21, 31, 41, 51, 61, 71, 81, 91]
    kopeyki = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]
    today = datetime.today().strftime("%Y-%m-%d")
    yesterday = time.strftime('%Y-%m-%d', time.gmtime(time.time() - 86400))
    say_message('Назовите валюту для конвертации')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    our_speech = str(r.recognize_google(audio, language="ru")).lower()
    if now.hour > 0 and now.hour < 6:
        say_message('Сейчас ночь и курс на сегоднешний календарный день еще не определён. Могу сказать вчерашний курс')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        speech = r.recognize_google(audio, language="ru")
        if speech in ['давай', 'давай за вчера', 'ну давай', 'давай за вчерашний день', 'ну давай так', 'ну давай за вчера', 'скажи тогда за вчера']:
            if our_speech == 'доллар':
                url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{yesterday}/currencies/usd.json'
                response = requests.get(url)
                result = response.json()
                rub = int(str(result['usd']['rub']).split('.')[0])
                kop = int(str(int(str(result['usd']['rub']).split('.')[1]))[:2])
                if rub in rubl and kop in kopeek:
                    say_message(f'1 доллар это {rub} рубль {kop} копеек')
                elif rub in rubl and kop in kopeyka:
                    say_message(f'1 доллар это {rub} рубль {kop} копейка')
                elif rub in rubl and kop in kopeyki:
                    say_message(f'1 доллар это {rub} рубль {kop} копейки')
                elif rub in rubley and kop in kopeek:
                    say_message(f'1 доллар это {rub} рублей {kop} копеек')
                elif rub in rubley and kop in kopeyka:
                    say_message(f'1 доллар это {rub} рублей {kop} копейка')
                elif rub in rubley and kop in kopeyki:
                    say_message(f'1 доллар это {rub} рублей {kop} копейки')
                elif rub in rublya and kop in kopeek:
                    say_message(f'1 доллар это {rub} рубля {kop} копеек')
                elif rub in rublya and kop in kopeyka:
                    say_message(f'1 доллар это {rub} рубля {kop} копейка')
                elif rub in rublya and kop in kopeyki:
                    say_message(f'1 доллар это {rub} рубля {kop} копейки')
            elif our_speech == 'евро':
                url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{yesterday}/currencies/eur.json'
                response = requests.get(url)
                result = response.json()
                rub = int(str(result['eur']['rub']).split('.')[0])
                kop = int(str(int(str(result['eur']['rub']).split('.')[1]))[:2])
                if rub in rubl and kop in kopeek:
                    say_message(f'1 евро это {rub} рубль {kop} копеек')
                elif rub in rubl and kop in kopeyka:
                    say_message(f'1 евро это {rub} рубль {kop} копейка')
                elif rub in rubl and kop in kopeyki:
                    say_message(f'1 евро это {rub} рубль {kop} копейки')
                elif rub in rubley and kop in kopeek:
                    say_message(f'1 евро это {rub} рублей {kop} копеек')
                elif rub in rubley and kop in kopeyka:
                    say_message(f'1 евро это {rub} рублей {kop} копейка')
                elif rub in rubley and kop in kopeyki:
                    say_message(f'1 евро это {rub} рублей {kop} копейки')
                elif rub in rublya and kop in kopeek:
                    say_message(f'1 евро это {rub} рубля {kop} копеек')
                elif rub in rublya and kop in kopeyka:
                    say_message(f'1 евро это {rub} рубля {kop} копейка')
                elif rub in rublya and kop in kopeyki:
                    say_message(f'1 евро это {rub} рубля {kop} копейки')
            elif our_speech == 'аргентинский песо':
                url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{yesterday}/currencies/ars.json'
                response = requests.get(url)
                result = response.json()
                rub = int(str(result['ars']['rub']).split('.')[0])
                kop = int(str(int(str(result['ars']['rub']).split('.')[1]))[:2])
                if rub in rubl and kop in kopeek:
                    say_message(f'1 аргентинский песо это {rub} рубль {kop} копеек')
                elif rub in rubl and kop in kopeyka:
                    say_message(f'1 аргентинский песо это {rub} рубль {kop} копейка')
                elif rub in rubl and kop in kopeyki:
                    say_message(f'1 аргентинский песо это {rub} рубль {kop} копейки')
                elif rub in rubley and kop in kopeek:
                    say_message(f'1 аргентинский песо это {rub} рублей {kop} копеек')
                elif rub in rubley and kop in kopeyka:
                    say_message(f'1 аргентинский песо это {rub} рублей {kop} копейка')
                elif rub in rubley and kop in kopeyki:
                    say_message(f'1 аргентинский песо это {rub} рублей {kop} копейки')
                elif rub in rublya and kop in kopeek:
                    say_message(f'1 аргентинский песо это {rub} рубля {kop} копеек')
                elif rub in rublya and kop in kopeyka:
                    say_message(f'1 аргентинский песо это {rub} рубля {kop} копейка')
                elif rub in rublya and kop in kopeyki:
                    say_message(f'1 аргентинский песо это {rub} рубля {kop} копейки')
            elif our_speech == 'белорусский рубль':
                url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{yesterday}/currencies/byr.json'
                response = requests.get(url)
                result = response.json()
                rub = int(str(result['byr']['rub']).split('.')[0])
                kop = int(str(int(str(result['byr']['rub']).split('.')[1]))[:2])
                if rub in rubl and kop in kopeek:
                    say_message(f'1 белорусский рубль это {rub} рубль {kop} копеек')
                elif rub in rubl and kop in kopeyka:
                    say_message(f'1 белорусский рубль это {rub} рубль {kop} копейка')
                elif rub in rubl and kop in kopeyki:
                    say_message(f'1 белорусский рубль это {rub} рубль {kop} копейки')
                elif rub in rubley and kop in kopeek:
                    say_message(f'1 белорусский рубль это {rub} рублей {kop} копеек')
                elif rub in rubley and kop in kopeyka:
                    say_message(f'1 белорусский рубль это {rub} рублей {kop} копейка')
                elif rub in rubley and kop in kopeyki:
                    say_message(f'1 белорусский рубль это {rub} рублей {kop} копейки')
                elif rub in rublya and kop in kopeek:
                    say_message(f'1 белорусский рубль это {rub} рубля {kop} копеек')
                elif rub in rublya and kop in kopeyka:
                    say_message(f'1 белорусский рубль это {rub} рубля {kop} копейка')
                elif rub in rublya and kop in kopeyki:
                    say_message(f'1 белорусский рубль это {rub} рубля {kop} копейки')
                else:
                    say_message(f'1 белорусский рубль примерно равен одному рублю')
            elif our_speech == 'фунт стерлингов':
                url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{yesterday}/currencies/gbp.json'
                response = requests.get(url)
                result = response.json()
                rub = int(str(result['gbp']['rub']).split('.')[0])
                kop = int(str(int(str(result['gbp']['rub']).split('.')[1]))[:2])
                if rub in rubl and kop in kopeek:
                    say_message(f'1 фунт стерлингов это {rub} рубль {kop} копеек')
                elif rub in rubl and kop in kopeyka:
                    say_message(f'1 фунт стерлингов это {rub} рубль {kop} копейка')
                elif rub in rubl and kop in kopeyki:
                    say_message(f'1 фунт стерлингов это {rub} рубль {kop} копейки')
                elif rub in rubley and kop in kopeek:
                    say_message(f'1 фунт стерлингов это {rub} рублей {kop} копеек')
                elif rub in rubley and kop in kopeyka:
                    say_message(f'1 фунт стерлингов это {rub} рублей {kop} копейка')
                elif rub in rubley and kop in kopeyki:
                    say_message(f'1 фунт стерлингов это {rub} рублей {kop} копейки')
                elif rub in rublya and kop in kopeek:
                    say_message(f'1 фунт стерлингов это {rub} рубля {kop} копеек')
                elif rub in rublya and kop in kopeyka:
                    say_message(f'1 фунт стерлингов это {rub} рубля {kop} копейка')
                elif rub in rublya and kop in kopeyki:
                    say_message(f'1 фунт стерлингов это {rub} рубля {kop} копейки')
                else:
                    say_message(f'1 фунт стерлингов примерно равен одному рублю')
            elif our_speech == 'датская крона':
                url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{yesterday}/currencies/dkk.json'
                response = requests.get(url)
                result = response.json()
                rub = int(str(result['dkk']['rub']).split('.')[0])
                kop = int(str(int(str(result['dkk']['rub']).split('.')[1]))[:2])
                if rub in rubl and kop in kopeek:
                    say_message(f'одна датская крона это {rub} рубль {kop} копеек')
                elif rub in rubl and kop in kopeyka:
                    say_message(f'одна датская крона это {rub} рубль {kop} копейка')
                elif rub in rubl and kop in kopeyki:
                    say_message(f'одна датская крона это {rub} рубль {kop} копейки')
                elif rub in rubley and kop in kopeek:
                    say_message(f'одна датская крона это {rub} рублей {kop} копеек')
                elif rub in rubley and kop in kopeyka:
                    say_message(f'одна датская крона это {rub} рублей {kop} копейка')
                elif rub in rubley and kop in kopeyki:
                    say_message(f'одна датская крона это {rub} рублей {kop} копейки')
                elif rub in rublya and kop in kopeek:
                    say_message(f'одна датская крона это {rub} рубля {kop} копеек')
                elif rub in rublya and kop in kopeyka:
                    say_message(f'одна датская крона это {rub} рубля {kop} копейка')
                elif rub in rublya and kop in kopeyki:
                    say_message(f'одна датская крона это {rub} рубля {kop} копейки')
            elif our_speech == 'кувейтский динар':  # пока не работает
                url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{yesterday}/currencies/kwd.json'
                response = requests.get(url)
                result = response.json()
                rub = int(str(result['kwd']['rub']).split('.')[0])
                kop = int(str(int(str(result['kwd']['rub']).split('.')[1]))[:2])
                if rub in rubl and kop in kopeek:
                    say_message(f'1 кувейтский динар это {rub} рубль {kop} копеек')
                elif rub in rubl and kop in kopeyka:
                    say_message(f'1 кувейтский динар это {rub} рубль {kop} копейка')
                elif rub in rubl and kop in kopeyki:
                    say_message(f'1 кувейтский динар это {rub} рубль {kop} копейки')
                elif rub in rubley and kop in kopeek:
                    say_message(f'1 кувейтский динар это {rub} рублей {kop} копеек')
                elif rub in rubley and kop in kopeyka:
                    say_message(f'1 кувейтский динар это {rub} рублей {kop} копейка')
                elif rub in rubley and kop in kopeyki:
                    say_message(f'1 кувейтский динар это {rub} рублей {kop} копейки')
                elif rub in rublya and kop in kopeek:
                    say_message(f'1 кувейтский динар это {rub} рубля {kop} копеек')
                elif rub in rublya and kop in kopeyka:
                    say_message(f'1 кувейтский динар это {rub} рубля {kop} копейка')
                elif rub in rublya and kop in kopeyki:
                    say_message(f'1 кувейтский динар это {rub} рубля {kop} копейки')
            elif our_speech == 'турецкая лира':
                url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/try.json'
                response = requests.get(url)
                result = response.json()
                rub = int(str(result['try']['rub']).split('.')[0])
                kop = int(str(int(str(result['try']['rub']).split('.')[1]))[:2])
                if rub in rubl and kop in kopeek:
                    say_message(f'одна турецкая лира это {rub} рубль {kop} копеек')
                elif rub in rubl and kop in kopeyka:
                    say_message(f'одна турецкая лира это {rub} рубль {kop} копейка')
                elif rub in rubl and kop in kopeyki:
                    say_message(f'одна турецкая лира это {rub} рубль {kop} копейки')
                elif rub in rubley and kop in kopeek:
                    say_message(f'одна турецкая лира это {rub} рублей {kop} копеек')
                elif rub in rubley and kop in kopeyka:
                    say_message(f'одна турецкая лира это {rub} рублей {kop} копейка')
                elif rub in rubley and kop in kopeyki:
                    say_message(f'одна турецкая лира это {rub} рублей {kop} копейки')
                elif rub in rublya and kop in kopeek:
                    say_message(f'одна турецкая лира это {rub} рубля {kop} копеек')
                elif rub in rublya and kop in kopeyka:
                    say_message(f'одна турецкая лира это {rub} рубля {kop} копейка')
                elif rub in rublya and kop in kopeyki:
                    say_message(f'одна турецкая лира это {rub} рубля {kop} копейки')
            elif our_speech == 'гривна':
                url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/uah.json'
                response = requests.get(url)
                result = response.json()
                rub = int(str(result['uah']['rub']).split('.')[0])
                kop = int(str(int(str(result['uah']['rub']).split('.')[1]))[:2])
                if rub in rubl and kop in kopeek:
                    say_message(f'одна гривна это {rub} рубль {kop} копеек')
                elif rub in rubl and kop in kopeyka:
                    say_message(f'одна гривна это {rub} рубль {kop} копейка')
                elif rub in rubl and kop in kopeyki:
                    say_message(f'одна гривна это {rub} рубль {kop} копейки')
                elif rub in rubley and kop in kopeek:
                    say_message(f'одна гривна это {rub} рублей {kop} копеек')
                elif rub in rubley and kop in kopeyka:
                    say_message(f'одна гривна это {rub} рублей {kop} копейка')
                elif rub in rubley and kop in kopeyki:
                    say_message(f'одна гривна это {rub} рублей {kop} копейки')
                elif rub in rublya and kop in kopeek:
                    say_message(f'одна гривна это {rub} рубля {kop} копеек')
                elif rub in rublya and kop in kopeyka:
                    say_message(f'одна гривна это {rub} рубля {kop} копейка')
                elif rub in rublya and kop in kopeyki:
                    say_message(f'одна гривна это {rub} рубля {kop} копейки')
            else:
                say_message('Я пока что не обладаю информацией о данной валюте')
    else:
        if our_speech == 'доллар':
            url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/usd.json'
            response = requests.get(url)
            result = response.json()
            rub = int(str(result['usd']['rub']).split('.')[0])
            kop = int(str(int(str(result['usd']['rub']).split('.')[1]))[:2])
            if rub in rubl and kop in kopeek:
                say_message(f'1 доллар это {rub} рубль {kop} копеек')
            elif rub in rubl and kop in kopeyka:
                say_message(f'1 доллар это {rub} рубль {kop} копейка')
            elif rub in rubl and kop in kopeyki:
                say_message(f'1 доллар это {rub} рубль {kop} копейки')
            elif rub in rubley and kop in kopeek:
                say_message(f'1 доллар это {rub} рублей {kop} копеек')
            elif rub in rubley and kop in kopeyka:
                say_message(f'1 доллар это {rub} рублей {kop} копейка')
            elif rub in rubley and kop in kopeyki:
                say_message(f'1 доллар это {rub} рублей {kop} копейки')
            elif rub in rublya and kop in kopeek:
                say_message(f'1 доллар это {rub} рубля {kop} копеек')
            elif rub in rublya and kop in kopeyka:
                say_message(f'1 доллар это {rub} рубля {kop} копейка')
            elif rub in rublya and kop in kopeyki:
                say_message(f'1 доллар это {rub} рубля {kop} копейки')
        elif our_speech == 'евро':
            url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/eur.json'
            response = requests.get(url)
            result = response.json()
            rub = int(str(result['eur']['rub']).split('.')[0])
            kop = int(str(int(str(result['eur']['rub']).split('.')[1]))[:2])
            if rub in rubl and kop in kopeek:
                say_message(f'1 евро это {rub} рубль {kop} копеек')
            elif rub in rubl and kop in kopeyka:
                say_message(f'1 евро это {rub} рубль {kop} копейка')
            elif rub in rubl and kop in kopeyki:
                say_message(f'1 евро это {rub} рубль {kop} копейки')
            elif rub in rubley and kop in kopeek:
                say_message(f'1 евро это {rub} рублей {kop} копеек')
            elif rub in rubley and kop in kopeyka:
                say_message(f'1 евро это {rub} рублей {kop} копейка')
            elif rub in rubley and kop in kopeyki:
                say_message(f'1 евро это {rub} рублей {kop} копейки')
            elif rub in rublya and kop in kopeek:
                say_message(f'1 евро это {rub} рубля {kop} копеек')
            elif rub in rublya and kop in kopeyka:
                say_message(f'1 евро это {rub} рубля {kop} копейка')
            elif rub in rublya and kop in kopeyki:
                say_message(f'1 евро это {rub} рубля {kop} копейки')
        elif our_speech == 'аргентинский песо':
            url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/ars.json'
            response = requests.get(url)
            result = response.json()
            rub = int(str(result['ars']['rub']).split('.')[0])
            kop = int(str(int(str(result['ars']['rub']).split('.')[1]))[:2])
            if rub in rubl and kop in kopeek:
                say_message(f'1 аргентинский песо это {rub} рубль {kop} копеек')
            elif rub in rubl and kop in kopeyka:
                say_message(f'1 аргентинский песо это {rub} рубль {kop} копейка')
            elif rub in rubl and kop in kopeyki:
                say_message(f'1 аргентинский песо это {rub} рубль {kop} копейки')
            elif rub in rubley and kop in kopeek:
                say_message(f'1 аргентинский песо это {rub} рублей {kop} копеек')
            elif rub in rubley and kop in kopeyka:
                say_message(f'1 аргентинский песо это {rub} рублей {kop} копейка')
            elif rub in rubley and kop in kopeyki:
                say_message(f'1 аргентинский песо это {rub} рублей {kop} копейки')
            elif rub in rublya and kop in kopeek:
                say_message(f'1 аргентинский песо это {rub} рубля {kop} копеек')
            elif rub in rublya and kop in kopeyka:
                say_message(f'1 аргентинский песо это {rub} рубля {kop} копейка')
            elif rub in rublya and kop in kopeyki:
                say_message(f'1 аргентинский песо это {rub} рубля {kop} копейки')
        elif our_speech == 'белорусский рубль':
            url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/byr.json'
            response = requests.get(url)
            result = response.json()
            rub = int(str(result['byr']['rub']).split('.')[0])
            kop = int(str(int(str(result['byr']['rub']).split('.')[1]))[:2])
            if rub in rubl and kop in kopeek:
                say_message(f'1 белорусский рубль это {rub} рубль {kop} копеек')
            elif rub in rubl and kop in kopeyka:
                say_message(f'1 белорусский рубль это {rub} рубль {kop} копейка')
            elif rub in rubl and kop in kopeyki:
                say_message(f'1 белорусский рубль это {rub} рубль {kop} копейки')
            elif rub in rubley and kop in kopeek:
                say_message(f'1 белорусский рубль это {rub} рублей {kop} копеек')
            elif rub in rubley and kop in kopeyka:
                say_message(f'1 белорусский рубль это {rub} рублей {kop} копейка')
            elif rub in rubley and kop in kopeyki:
                say_message(f'1 белорусский рубль это {rub} рублей {kop} копейки')
            elif rub in rublya and kop in kopeek:
                say_message(f'1 белорусский рубль это {rub} рубля {kop} копеек')
            elif rub in rublya and kop in kopeyka:
                say_message(f'1 белорусский рубль это {rub} рубля {kop} копейка')
            elif rub in rublya and kop in kopeyki:
                say_message(f'1 белорусский рубль это {rub} рубля {kop} копейки')
            else:
                say_message(f'1 белорусский рубль примерно равен одному рублю')
        elif our_speech == 'фунт стерлингов':
            url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/gbp.json'
            response = requests.get(url)
            result = response.json()
            rub = int(str(result['gbp']['rub']).split('.')[0])
            kop = int(str(int(str(result['gbp']['rub']).split('.')[1]))[:2])
            if rub in rubl and kop in kopeek:
                say_message(f'1 фунт стерлингов это {rub} рубль {kop} копеек')
            elif rub in rubl and kop in kopeyka:
                say_message(f'1 фунт стерлингов это {rub} рубль {kop} копейка')
            elif rub in rubl and kop in kopeyki:
                say_message(f'1 фунт стерлингов это {rub} рубль {kop} копейки')
            elif rub in rubley and kop in kopeek:
                say_message(f'1 фунт стерлингов это {rub} рублей {kop} копеек')
            elif rub in rubley and kop in kopeyka:
                say_message(f'1 фунт стерлингов это {rub} рублей {kop} копейка')
            elif rub in rubley and kop in kopeyki:
                say_message(f'1 фунт стерлингов это {rub} рублей {kop} копейки')
            elif rub in rublya and kop in kopeek:
                say_message(f'1 фунт стерлингов это {rub} рубля {kop} копеек')
            elif rub in rublya and kop in kopeyka:
                say_message(f'1 фунт стерлингов это {rub} рубля {kop} копейка')
            elif rub in rublya and kop in kopeyki:
                say_message(f'1 фунт стерлингов это {rub} рубля {kop} копейки')
            else:
                say_message(f'1 фунт стерлингов примерно равен одному рублю')
        elif our_speech == 'датская крона':
            url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/dkk.json'
            response = requests.get(url)
            result = response.json()
            rub = int(str(result['dkk']['rub']).split('.')[0])
            kop = int(str(int(str(result['dkk']['rub']).split('.')[1]))[:2])
            if rub in rubl and kop in kopeek:
                say_message(f'одна датская крона это {rub} рубль {kop} копеек')
            elif rub in rubl and kop in kopeyka:
                say_message(f'одна датская крона это {rub} рубль {kop} копейка')
            elif rub in rubl and kop in kopeyki:
                say_message(f'одна датская крона это {rub} рубль {kop} копейки')
            elif rub in rubley and kop in kopeek:
                say_message(f'одна датская крона это {rub} рублей {kop} копеек')
            elif rub in rubley and kop in kopeyka:
                say_message(f'одна датская крона это {rub} рублей {kop} копейка')
            elif rub in rubley and kop in kopeyki:
                say_message(f'одна датская крона это {rub} рублей {kop} копейки')
            elif rub in rublya and kop in kopeek:
                say_message(f'одна датская крона это {rub} рубля {kop} копеек')
            elif rub in rublya and kop in kopeyka:
                say_message(f'одна датская крона это {rub} рубля {kop} копейка')
            elif rub in rublya and kop in kopeyki:
                say_message(f'одна датская крона это {rub} рубля {kop} копейки')
        elif our_speech == 'кувейтский динар': # пока не работает
            url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{yesterday}/currencies/kwd.json'
            response = requests.get(url)
            result = response.json()
            rub = int(str(result['kwd']['rub']).split('.')[0])
            kop = int(str(int(str(result['kwd']['rub']).split('.')[1]))[:2])
            if rub in rubl and kop in kopeek:
                say_message(f'1 кувейтский динар это {rub} рубль {kop} копеек')
            elif rub in rubl and kop in kopeyka:
                say_message(f'1 кувейтский динар это {rub} рубль {kop} копейка')
            elif rub in rubl and kop in kopeyki:
                say_message(f'1 кувейтский динар это {rub} рубль {kop} копейки')
            elif rub in rubley and kop in kopeek:
                say_message(f'1 кувейтский динар это {rub} рублей {kop} копеек')
            elif rub in rubley and kop in kopeyka:
                say_message(f'1 кувейтский динар это {rub} рублей {kop} копейка')
            elif rub in rubley and kop in kopeyki:
                say_message(f'1 кувейтский динар это {rub} рублей {kop} копейки')
            elif rub in rublya and kop in kopeek:
                say_message(f'1 кувейтский динар это {rub} рубля {kop} копеек')
            elif rub in rublya and kop in kopeyka:
                say_message(f'1 кувейтский динар это {rub} рубля {kop} копейка')
            elif rub in rublya and kop in kopeyki:
                say_message(f'1 кувейтский динар это {rub} рубля {kop} копейки')
        elif our_speech == 'турецкая лира':
            url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/try.json'
            response = requests.get(url)
            result = response.json()
            rub = int(str(result['try']['rub']).split('.')[0])
            kop = int(str(int(str(result['try']['rub']).split('.')[1]))[:2])
            if rub in rubl and kop in kopeek:
                say_message(f'одна турецкая лира это {rub} рубль {kop} копеек')
            elif rub in rubl and kop in kopeyka:
                say_message(f'одна турецкая лира это {rub} рубль {kop} копейка')
            elif rub in rubl and kop in kopeyki:
                say_message(f'одна турецкая лира это {rub} рубль {kop} копейки')
            elif rub in rubley and kop in kopeek:
                say_message(f'одна турецкая лира это {rub} рублей {kop} копеек')
            elif rub in rubley and kop in kopeyka:
                say_message(f'одна турецкая лира это {rub} рублей {kop} копейка')
            elif rub in rubley and kop in kopeyki:
                say_message(f'одна турецкая лира это {rub} рублей {kop} копейки')
            elif rub in rublya and kop in kopeek:
                say_message(f'одна турецкая лира это {rub} рубля {kop} копеек')
            elif rub in rublya and kop in kopeyka:
                say_message(f'одна турецкая лира это {rub} рубля {kop} копейка')
            elif rub in rublya and kop in kopeyki:
                say_message(f'одна турецкая лира это {rub} рубля {kop} копейки')
        elif our_speech == 'гривна':
            url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{today}/currencies/uah.json'
            response = requests.get(url)
            result = response.json()
            rub = int(str(result['uah']['rub']).split('.')[0])
            kop = int(str(int(str(result['uah']['rub']).split('.')[1]))[:2])
            if rub in rubl and kop in kopeek:
                say_message(f'одна гривна это {rub} рубль {kop} копеек')
            elif rub in rubl and kop in kopeyka:
                say_message(f'одна гривна это {rub} рубль {kop} копейка')
            elif rub in rubl and kop in kopeyki:
                say_message(f'одна гривна это {rub} рубль {kop} копейки')
            elif rub in rubley and kop in kopeek:
                say_message(f'одна гривна это {rub} рублей {kop} копеек')
            elif rub in rubley and kop in kopeyka:
                say_message(f'одна гривна это {rub} рублей {kop} копейка')
            elif rub in rubley and kop in kopeyki:
                say_message(f'одна гривна это {rub} рублей {kop} копейки')
            elif rub in rublya and kop in kopeek:
                say_message(f'одна гривна это {rub} рубля {kop} копеек')
            elif rub in rublya and kop in kopeyka:
                say_message(f'одна гривна это {rub} рубля {kop} копейка')
            elif rub in rublya and kop in kopeyki:
                say_message(f'одна гривна это {rub} рубля {kop} копейки')
        else:
            say_message('Я пока что не обладаю информацией о данной валюте')


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
