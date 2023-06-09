# url shortner v1.0

import requests
from tkinter import *

api_url = "https://api.shrtco.de/v2/shorten"

import urllib.request


def internet_on(host="http://google.com"):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False

on = internet_on()
print(on)


def api_call():
    param = {"url": user_input.get()}
    response = requests.get(url=api_url, params=param)
    all = response.json()
    # print(all)
    print(response.status_code)
    try:
        shrt2 = all["result"]["short_link2"]
    except:
        output.delete('1.0',END)
        output.insert("1.0", "Link Invalid")
    else:
        output.config(background="yellow", border=2, width=15, height=1)
        output.delete('1.0',END)
        output.insert("1.0", shrt2)


window = Tk()

window.title(string="Teja's Url Shortner")

ask_input = Label(text="Enter your link here : ")
ask_input.grid(column=0, row=2)
user_input = Entry(width=20)
user_input.grid(column=1, row=2)

generate = Button(
    text="Generate", foreground="yellow", background="green", command=api_call
)
# generate.config(fo)
generate.grid(column=0, row=3)

show_op = Label(text="Shorten url : ")
show_op.grid(column=0, row=4)

output = Text()
output.config(width=15, height=1)
output.grid(column=1, row=4)

exit = Button(
    foreground="yellow", background="red", text="exit", command=window.destroy
)
exit.grid(row=5, column=0)

window.mainloop()
