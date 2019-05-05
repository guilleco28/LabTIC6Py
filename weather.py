import requests
import pandas as pd
import time

reduced_cities = pd.read_json('reduced_cities.json')
reduced_cities_id = reduced_cities['id']
data = []

start = time.time()

for id in reduced_cities_id:
    url = 'http://api.openweathermap.org/data/2.5/weather?id='+str(id)\
          +'&appid=914d0fb2b811eadd0aa84cb68f95264e'
    name = requests.get(url).json()['name']
    temperature = requests.get(url).json()['main']['temp']
    humidity = requests.get(url).json()['main']['humidity']
    city_to_add = [name, temperature, humidity]
    data.append(city_to_add)

dataframe = pd.DataFrame(data, columns=['Name', 'Temperature',
                                        'Humidity'])
print(dataframe)

end = time.time()

print(end-start)  # 25 segundos
