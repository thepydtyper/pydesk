from tkinter import *
import json
from urllib.request import urlopen
import ssl

#ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_weather():
    zip = input_window.get()
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip}&APPID=19b28d8185e272acbb4751d900d9db03"
    data = urlopen(weather_url, context=ctx).read()
    js = json.loads(data)
    weather_desc = js['weather'][0]['description']
    temp_kel = js['main']['temp']
    weather_temp = int((temp_kel - 273.15) * (9/5) + 32)
    output_window['text'] = f"Gathering weather report for {zip}:\n\tCurrent Temp: {weather_temp}°F\n\tConditions: {weather_desc}"
    #print(weather_url)


def get_news():
    search = input_window.get()
    output_window['text'] = f"Fetching {search} headlines"


def get_stocks():
    company = input_window.get()
    output_window['text'] = f"Getting stock quote for {company}"


root = Tk()
root.title("Deskpy")
root.iconbitmap("P:/Programming/Apps/_Mine/Desktop-Scraper/pycon.ico")

input_label = Label(root, text="Input: ")
input_label.grid(row=0, column=0)

input_window = Entry(root, width=50, bg="black", fg="green", bd=5)
input_window.grid(row=0, column=1, columnspan=3)

button_weather = Button(root, text="Weather",
                        command=get_weather, padx=30, pady=20)
button_weather.grid(row=1, column=1)

button_news = Button(root, text="News", command=get_news, padx=30, pady=20)
button_news.grid(row=1, column=2)

button_stocks = Button(root, text="Stocks",
                       command=get_stocks, padx=30, pady=20)
button_stocks.grid(row=1, column=3)

output_label = Label(root, text="Output: ")
output_label.grid(row=2, column=0)

output_window = Label(root, bg="black", fg="green", relief=SUNKEN, width=44)
output_window.grid(row=2, column=1, columnspan=3)


root.mainloop()
