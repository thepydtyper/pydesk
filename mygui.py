from tkinter import *
import json
import requests


def get_input():
    """
    Called by button functions to grab user-entered data
    :return: a string of the user-inputed data
    """
    return input_window.get()


def get_api_key(info):
    """
    Called by button functions to grab appropriate API keys
    :param info: a string denoting type of info the calling function will return
    :return: a string of the API key needed by each type of function ['weather', 'news', etc]
    """
    if info == "weather":
        return "19b28d8185e272acbb4751d900d9db03"
    elif info == "news":
        return "b24fda3c46cb4fc69599efdb5aadcbc1"
    elif info == "stocks":
        return "KXWH1RPNH5432DUJ"


def get_weather():
    """
    Called upon user-click of the 'Weather' button.
    Gets user-inputed zip code as text from the Input field to generate an API call to openweathermap.org
    :return: prints weather stats for the provided zip code to the output window
    """
    zipc = get_input()
    api_key = get_api_key("weather")
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?"
    params = {"APPID": api_key, "zip": zipc}
    try:
        data = requests.get(weather_url, params=params)
        js = data.json()
        weather_desc = js['weather'][0]['description']
        temp_kel = js['main']['temp']
        weather_temp = int((temp_kel - 273.15) * (9/5) + 32)
        city = js['name']
        output_window['text'] = f"Gathering weather report for {zipc}..\n"
        output_window['text'] += f"\nCity: {city}"
        output_window['text'] += f"\nCurrent Temp: {weather_temp}°F"
        output_window['text'] += f"\nConditions: {weather_desc}"
    except:
        output_window["text"] = f"Sorry, but '{zipc}' is not recognized by the system.\n"
        output_window["text"] += "Try a different ZIP."


def get_news():
    """
    Called upon user-click of the 'News' button.
    Gets user-inputed subject as text from the Input field to generate an API call to newsapi.org
    :return: prints headlines for the provided topic to the output window
    """
    search = get_input()
    api_key = get_api_key("news")
    news_url = f"https://newsapi.org/v2/everything?"
    params = {"q": search, "apiKey": api_key}
    try:
        data = requests.get(news_url, params=params)
        js = data.json()
        headline_dict = {}
        for _ in range(5):
            title = js['articles'][_]['title']
            url = js['articles'][_]['url']
            headline_dict.update({title: url})
        output_window['text'] = f"Fetching '{search}' headlines..\n"
        for title, url in headline_dict.items():
            output_window['text'] += f"\n{title}: {url}"
    except:
        output_window["text"] = f"Sorry, but '{search}' is not recognized by the system.\n"
        output_window["text"] += "Try a different topic."


def get_stocks():
    """
    Called upon user-click of the 'Stocks' button.
    Gets user-inputed company ticker symbol as text from the Input field to generate an API call to alphavantage.co
    :return: prints stock stats for the provided company to the output window
    """
    company = get_input()
    api_key = get_api_key("stocks")
    stock_url = "https://www.alphavantage.co/query?"
    params = {"apikey": api_key, "symbol": company, "function": "GLOBAL_QUOTE"}
    try:
        data = requests.get(stock_url, params=params)
        js = data.json()
        symbol = js["Global Quote"]["01. symbol"]
        opening = js['Global Quote']['02. open']
        high = js["Global Quote"]["03. high"]
        low = js["Global Quote"]["04. low"]
        price = js["Global Quote"]["05. price"]
        output_window['text'] = f"Getting stock quote for {symbol}..\n"
        output_window['text'] += f"\nOpen: {opening}"
        output_window['text'] += f"\nLow: {low}"
        output_window['text'] += f"\nHigh: {high}"
        output_window['text'] += f"\nPrice: {price}"
    except:
        output_window["text"] = f"Sorry, but '{company}' is not recognized by the system.\n"
        output_window["text"] += "Try a different company/symbol."


# Create the main window with title and icon
root = Tk()
root.title("Pydesk v0.5")
icon = PhotoImage(file="pycon.png")
root.iconphoto(False, icon)

HEIGHT = 400
WIDTH = 500
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Input Frame
input_frame = Frame(root, bd=5)
input_frame.place(relx=0.3, rely=0.1, relwidth=1, relheight=0.1, anchor=N)

# Label and window for user input
input_label = Label(input_frame, text="Input:", font=("Monospaced", 17))
input_label.place(relwidth=0.55, relheight=1)

input_window = Entry(input_frame, font=("Monospaced", 17), bg="black", fg="green")
input_window.place(relx=0.4, relwidth=1, relheight=1)

# Button Frame
button_frame = Frame(root, bd=5)
button_frame.place(relx=0.3, rely=0.25, relwidth=1, relheight=0.1, anchor=N)

# Buttons for weather, stocks, news, quit
button_weather = Button(button_frame, text="Weather", command=get_weather)
button_weather.place(relx=0.25, relwidth=0.15, relheight=1)

button_news = Button(button_frame, text="News", command=get_news)
button_news.place(relx=0.45, relwidth=0.15, relheight=1)

button_stocks = Button(button_frame, text="Stocks", command=get_stocks)
button_stocks.place(relx=0.65, relwidth=0.15, relheight=1)

button_quit = Button(button_frame, text="Exit", command=root.quit)
button_quit.place(relx=0.85, relwidth=0.15, relheight=1)

# Output Frame
output_frame = Frame(root, bd=5)
output_frame.place(relx=0.3, rely=0.35, relwidth=1, relheight=0.5, anchor=N)

# # Label and window for the output
output_label = Label(output_frame, text="Output:", font=("Monospaced", 17))
output_label.place(relwidth=0.55, relheight=1)

output_window = Label(output_frame, bg="black", fg="green", anchor=NW, justify="left")
output_window.place(relx=0.4, relwidth=1, relheight=1)

# # 'Crafted by' banner at the bottom
pyd_label = Label(root, text="Crafted by the Py'd Typer", bd=1, relief=SUNKEN, font=("Monospaced", 12), anchor=E)
pyd_label.place(rely=0.9, relwidth=1, relheight=0.1)

root.mainloop()
