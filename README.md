This is a project I grabbed of the internet that I'm going to be editing to make it better!

  Credit
  This link will also provide on how to get an OpenWeatherMap API key.
The original project is located here : [https://microcontrollerslab.com/raspberry-pi-pico-w-openweathermap-api-sensorless-weather-station/]

  I used this repo for the NTP portion of the code in my repo! I copied and pasted lines 8 to 49 by the way.
[https://gist.github.com/aallan/581ecf4dc92cd53e3a415b7c33a1147c]

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

Now for the confusing part setting the time... At face value this sounds simple, just change a paramater and done! Technically you would be right but its werid. The NTP_delta variable you have to change. I have no clue on how to change it properly so I changed a bunch of the numbers hoping eventually it would work, and it did! The time is set to +7 or MST but if you want to change it, your going to struggle so try your best! Unless you know how deltas work.

Again like my last project thne screen is optional, just uncomment lines 95-101 and it will print in the terminal. Also make sure to add a small delay on line 94 so it will not lag as bad.
