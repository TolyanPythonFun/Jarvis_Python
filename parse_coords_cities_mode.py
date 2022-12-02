import requests
import time
import json
from bs4 import BeautifulSoup


main_url = 'https://time-in.ru/coordinates'

response = requests.get(url=main_url)
soup = BeautifulSoup(response.text, 'lxml')

data = []

coords_list_countries = soup.find('ul', class_='coordinates-list').find_all('li')
# with open(file='cities_coords.json', mode='w', encoding='utf-8') as file:
for country in coords_list_countries:
    country_name = country.find('a').text
    link_contry = country.find('a').get('href')
    #print(f'---{country_name}---')
    req = requests.get(url=link_contry)
    soup = BeautifulSoup(req.text, 'lxml')
    #time.sleep(1)
    try:
        coords_cities_list = soup.find('ul', class_='coordinates-items').find_all('li')

        for city in coords_cities_list:

            city_name = city.find('a').text
            city_coords = city.find('div', class_='coordinates-items-right').text
            lat = str(city_coords).split(',')[0].strip()
            lon = str(city_coords).split(',')[-1].strip()
            #print(f'{city_name} --> Широта - {lat}, Долгота - {lon}')

            data = {
                country_name : {
                    city_name : {
                        'Широта' : lat,
                        'Долгота' : lon
                    }
                }
            }




    except:
        coords_cities_list = ''



print(data)



