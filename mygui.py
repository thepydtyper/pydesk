from tkinter import *
from tkinter import font
import json
from urllib.request import urlopen
import ssl

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_weather():
    zip = input_window.get()
    api = "19b28d8185e272acbb4751d900d9db03"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip}&APPID=" + api
    try:
        data = urlopen(weather_url, context=ctx).read()
        js = json.loads(data)
        weather_desc = js['weather'][0]['description']
        temp_kel = js['main']['temp']
        weather_temp = int((temp_kel - 273.15) * (9/5) + 32)
        output_window['text'] = f"Gathering weather report for {zip}.."
        output_window['text'] += f"\nCurrent Temp: {weather_temp}°F\nConditions: {weather_desc}"
    except:
        output_window["text"] = f"Sorry, but '{zip}' is not recognized by the system.\nTry another ZIP."


def get_news():
    search = input_window.get()
    api = "b24fda3c46cb4fc69599efdb5aadcbc1"
    news_url = f"https://newsapi.org/v2/everything?q={search}&apiKey=" + api
    data = urlopen(news_url, context=ctx).read()
    js = json.loads(data)
    headline_dict = {}
    for _ in range(3):
        title = js['articles'][_]['title']
        url = js['articles'][_]['url']
        headline_dict.update({title: url})
    output_window['text'] = f"Fetching '{search}' headlines.."
    for title, url in headline_dict.items():
        output_window['text'] += f"\n\t{title}: {url}"


def get_stocks():
    company = input_window.get().upper()
    api = "KXWH1RPNH5432DUJ"
    stock_url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + company + "&apikey=" + api
    data = urlopen(stock_url, context=ctx).read()
    js = json.loads(data)
    opening = js['Global Quote']['02. open']
    high = js["Global Quote"]["03. high"]
    low = js["Global Quote"]["04. low"]
    price = js["Global Quote"]["05. price"]
    output_window['text'] = f"Getting stock quote for {company}:..\n"
    output_window['text'] += f"Open: {opening}\n"
    output_window['text'] += f"Low: {low}\n"
    output_window['text'] += f"High: {high}\n"
    output_window['text'] += f"Price: {price}\n"


root = Tk()
root.title("Deskpy")
icon = PhotoImage(file="pycon.png")
root.iconphoto(False, icon)

input_label = Label(root, text="Input: ")
input_label.grid(row=0, column=0)

input_window = Entry(root, width=50, bg="black", fg="green", bd=5)
input_window.grid(row=0, column=1, columnspan=3)

button_weather = Button(root, text="Weather", command=get_weather, padx=30, pady=20)
button_weather.grid(row=1, column=1)

button_news = Button(root, text="News", command=get_news, padx=30, pady=20)
button_news.grid(row=1, column=2)

button_stocks = Button(root, text="Stocks", command=get_stocks, padx=30, pady=20)
button_stocks.grid(row=1, column=3)

button_quit = Button(root, text="Exit", command=root.quit, padx=30, pady=20)
button_quit.grid(row=2, column=3)

output_label = Label(root, text="Output: ")
output_label.grid(row=3, column=0)

output_window = Label(root, bg="black", fg="green", relief=SUNKEN, width=44)
output_window.grid(row=3, column=1, columnspan=3)

pyd_label = Label(root, text="Crafted by the Py'd Typer", bd=1, relief=SUNKEN, font="bold", anchor=E)
pyd_label.grid(row=4, column=0, columnspan=4, sticky=W+E)

root.mainloop()
