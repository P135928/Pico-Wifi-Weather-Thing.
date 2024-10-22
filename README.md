This is a project I grabbed of the internet that I'm going to be editing to make it better!

  Credit
The original project is located here : [https://microcontrollerslab.com/raspberry-pi-pico-w-openweathermap-api-sensorless-weather-station/]
This link will also provide on how to get an OpenWeatherMap API key.

I  just copied and pasted the code onto here and I am going to make it better by adding some quality of life features. If you can think you can make this code even better, do it! Submit a pull request or something, just make it better!

  Requirements:
Raspberry Pi Pico W
SSD1306 Screen
SSD1306 library
Internet Connectivity

  SSD1306 Pins:
SDA: Pin 4 or any other SDA pin, just make sure to change it in code if using anything other than P4  Line 20
SCL: Pin 5 or any other SCL pin, just make sure to change it in code if using anything other than P5  Line 20
VCC: 3.3V Power on the Pico
GND: GND on the Pico

  Setup!
Copy and paste the code, put in your WiFi credentials on lines 26-27, put your location on lines 34-35, and then last but not least put your location on lines 34-35!

Again like my last project thne screen is optional, just uncomment lines 95-101 and it will print in the terminal. Also make sure to add a small delay on line 94 so it will not lag as bad.
