import time

try:
  import urequests as requests
except:
  import requests
  
try:
  import ujson as json
except:
  import json

import network

import gc
gc.collect()

ssid = ' ' # Put your SSID here
password = 'password' # Put your WiFi Password here

city = 'Phoenix' # This is the city you live in
country_code = 'US' # This is your 2 letter country code, I think it can be more too.
#example
#city = 'Lahore'
#country_code = 'PAK'

open_weather_map_api_key = '' # Your API Key, make sure to put this there! Otherwise the program wont be able to communicate to OWM.

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#set your unique OpenWeatherMap.org URL
open_weather_map_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country_code + '&APPID=' + open_weather_map_api_key

weather_data = requests.get(open_weather_map_url)

# Location (City and Country code)
location = 'Location: ' + weather_data.json().get('name') + ' - ' + weather_data.json().get('sys').get('country')

# Weather Description
description = 'Description: ' + weather_data.json().get('weather')[0].get('main')

# Temperature
raw_temperature = weather_data.json().get('main').get('temp')-273.15

# Temperature in Celsius
#temperature = 'Temperature: ' + str(raw_temperature) + '*C'
#uncomment for temperature in Fahrenheit
temperature = 'Temperature: ' + str(raw_temperature*(9/5.0)+32) + '*F'

# Pressure
pressure = 'Pressure: ' + str(weather_data.json().get('main').get('pressure')) + 'hPa'

# Humidity
humidity = 'Humidity: ' + str(weather_data.json().get('main').get('humidity')) + '%'

# Wind
wind = 'Wind: ' + str(weather_data.json().get('wind').get('speed')) + 'mps ' + str(weather_data.json().get('wind').get('deg')) + '*'

print("###################################################")
print(wind)
print(pressure)
print(temperature)
print(description)
print(location)
print("###################################################")
