import requests
from bs4 import BeautifulSoup
import time

def get_info_about_film():
    for i in range(1, 11):
        url = f'https://www.kinoafisha.info/rating/movies/?page={i - 1}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        titles = soup.find_all('a', class_='movieItem_title')
        for title in titles:
            print(title.text)
            link = title.get('href')
            req = requests.get(link)
            sup = BeautifulSoup(req.text, 'lxml')
            desc = sup.find('div', class_='visualEditorInsertion filmDesc_editor more_content').text
            print(desc)
            time.sleep(1)
        i += 1
        time.sleep(1)

get_info_about_film()

