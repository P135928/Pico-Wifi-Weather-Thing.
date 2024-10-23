import time
from machine import Pin, SoftI2C
import ssd1306
import socket
import struct
import os
import ntptime

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

oled.fill(0)
oled.text("Attempting to",0,0)
oled.text("Connect",0,10)
oled.show()

city = 'Litchfield%20Park' # This is the city you live in
country_code = 'US' # This is your 2 letter country code, I think it can be more too.
#example
#city = 'Lahore'
#country_code = 'PAK'

open_weather_map_api_key = '99a33c64ef66e5607ef0675742a490de' # Your API Key, make sure to put this there! Otherwise the program wont be able to communicate to OWM.


NTP_DELTA = 4318988400
host = "pool.ntp.org"

led = Pin("LED", Pin.OUT)

ssid = ' '
password = 'password'

def set_time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_DELTA    
    tm = time.gmtime(t)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    oled.fill(0)
    oled.text("Connected!",0,0)
    oled.show()

oled.fill(0)
oled.show()
set_time()
while True:
    current_time = time.localtime()
    # Remove             This                                          and this if you dont want seconds.
    time_str = "%02d:%02d:%02d" % (current_time[3], current_time[4], current_time[5])
    open_weather_map_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country_code + '&APPID=' + open_weather_map_api_key

    weather_data = requests.get(open_weather_map_url)

    # Location (City and Country code)
    location = weather_data.json().get('name') + ' - ' + weather_data.json().get('sys').get('country')

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
    oled.fill(0)
    oled.text(wind , 0 ,0)
    oled.text(pressure,0,10)
    oled.text(temperature,0,20)
    oled.text(description,0,30)
    oled.text(location,0,40)
    oled.text(time_str, 0, 50)
    oled.show()
    #print("###################################################") If you need these Uncomment them!
    #print(wind) Its making my IDE laggy so im removing them.
    #print(pressure)
    #print(temperature)
    #print(description)
    #print(location)
    #print("###################################################")
