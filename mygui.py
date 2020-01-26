from tkinter import *


def get_weather():
    zip = input_window.get()
    output_window['text'] = f"Gathering weather report for {zip}"


def get_news():
    search = input_window.get()
    output_window['text'] = f"Fetching {search} headlines"


def get_stocks():
    company = input_window.get()
    output_window['text'] = f"Getting stock quote for {company}"


root = Tk()


output_label = Label(root, text="Output: ")
output_label.grid(row=0, column=0)

output_window = Label(root, width=30, bg="black", fg="green")
output_window.grid(row=0, column=1)

button_weather = Button(root, text="Weather", command=get_weather)
button_weather.grid(row=1, column=0)

button_news = Button(root, text="News", command=get_news)
button_news.grid(row=1, column=1)

button_stocks = Button(root, text="Stocks", command=get_stocks)
button_stocks.grid(row=1, column=2)

input_label = Label(root, text="Input: ")
input_label.grid(row=2, column=0)

input_window = Entry(root, width=20, bg="black", fg="green", borderwidth=5)
input_window.grid(row=2, column=1)



root.mainloop()