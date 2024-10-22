import time
from machine import Pin, SoftI2C
import ssd1306

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

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

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
location = 'Loc:' + weather_data.json().get('name') + ' - ' + weather_data.json().get('sys').get('country')

# Weather Description
description = 'Desc:' + weather_data.json().get('weather')[0].get('main')

# Temperature
raw_temperature = weather_data.json().get('main').get('temp')-273.15

# Temperature in Celsius
#temperature = 'Temperature: ' + str(raw_temperature) + '*C'
#uncomment for temperature in Fahrenheit
temperature = 'Temp:' + str(raw_temperature*(9/5.0)+32)

# Pressure
pressure = 'Pres:' + str(weather_data.json().get('main').get('pressure')) + 'hPa'

# Humidity
humidity = 'Humid:' + str(weather_data.json().get('main').get('humidity')) + '%'

# Wind
wind = 'Wind:' + str(weather_data.json().get('wind').get('speed')) + 'mps ' + str(weather_data.json().get('wind').get('deg')) + '*'

print("###################################################")
print(wind)
print(pressure)
print(temperature)
print(description)
print(location)
print("###################################################")

oled.text(wind , 0 ,0)
oled.text(pressure,0,10)
oled.text(temperature,0,20)
oled.text(description,0,30)
oled.text(location,0,40)
oled.show()
