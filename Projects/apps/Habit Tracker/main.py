#---------------------------Modules----------------------------------#

import tkinter as tk
import webbrowser
import requests
import datetime

#---------------------------Constants--------------------------------#

USERNAME = "<>"
TOKEN = "<>"
GRAPH_ID = "<>"
ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

APP_TITLE = "<custom name>"

curr = datetime.datetime.now()
format_date = curr.strftime("%Y%m%d")

#---------------------------Functions--------------------------------#

def Put():
    endpoint = f"{ENDPOINT}/{format_date}"

    user_value = float(input("Enter Value : "))

    request_body = {"quantity": str(user_value)}
    print(request_body)

    request_headers = {"X-USER-TOKEN": TOKEN}
    response = requests.put(url=endpoint, json=request_body,headers=request_headers)
    print(response.text)
    
def Post():
    endpoint=ENDPOINT
    user_value = float(user_val_entry.get())

    request_body = {"date": format_date, "quantity": str(user_value)}
    print(request_body)

    request_headers = {"X-USER-TOKEN": TOKEN}
    response = requests.post(url=endpoint, json=request_body,headers=request_headers)
    print(response.text)

 
def openWindow():
    webbrowser.open(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}")
    
#-------------------------------GUI--------------------------------#

window = tk.Tk()
window.title(APP_TITLE)

i=0
# Create label and entry for "eff hrs"
eff_hrs_label = tk.Label(window, text="Enter val:")
eff_hrs_label.grid(row=i, column=0, sticky="w")
user_val_entry = tk.Entry(window)
user_val_entry.grid(row=i, column=1)

i+=1
# Create submit button
post_btn = tk.Button(window, text="Post", command=Post, foreground='white',background='green')
post_btn.grid(row=i, column=1, pady=10)

i+=1
put_btn = tk.Button(window, text="Put", command=Put, foreground='white',background='blue')
put_btn.grid(row=i, column=1, pady=10)

i+=1
# Create view button
view_button = tk.Button(window, text="View", command=openWindow, foreground='white',background='blue')
view_button.grid(row=i, column=1, pady=10)

i+=1
exit_btn = tk.Button(window, text="Exit", command=window.destroy,foreground='white',background='red')
exit_btn.grid(row=i, column=1, pady=10)
window.mainloop()