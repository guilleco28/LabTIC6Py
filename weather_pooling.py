import requests
import pandas as pd
import time
import json
from multiprocessing import Pool


def load_data(cities):
    data = []
    url = 'http://api.openweathermap.org/data/2.5/weather?id='\
          +str(cities['id'])+'&appid=914d0fb2b811eadd0aa84cb68f95264e'
    name = requests.get(url).json()['name']
    temperature = requests.get(url).json()['main']['temp']
    humidity = requests.get(url).json()['main']['humidity']
    city_to_add = [name, temperature, humidity]
    data.append(city_to_add)
    dataframe = pd.DataFrame(data, columns=['Name', 'Temperature',
                                            'Humidity'])
    print(dataframe)
    return data

if __name__ == '__main__':
    with open('reduced_cities.json') as json_file:
        reduced_cities = json.load(json_file)
    startTime = time.time()
    pool = Pool()
    pool.map(load_data, reduced_cities)
    endTime = time.time()
    print(endTime-startTime)  # 5,2 segundos
