# v1.0
import csv

csv_file = "C:/programming/Python/Projects/scrapping/top_40_webseries_imdb.csv"
fields = ["No", "Series"]
rows = []

from bs4 import BeautifulSoup
import requests

file_path = "C:/programming/Python/programs/Scrapping/top_40_webseries_imdb.txt"
website = "https://www.imdb.com/list/ls026690132/"
response = requests.get(website)
web = response.text

soup = BeautifulSoup(web, "html.parser")
series_div = soup.find_all(name="div", class_="lister-item-content")

h3_list = [series.find(name="h3") for series in series_div]

series_list_text = [text.getText() for text in h3_list]

no = 1
for text in series_list_text:
    show_txt = text.replace("\n", "")
    show = show_txt.split(".")
    rows.append(show)
    no += 1
    # print(show)


with open(csv_file, "w", newline="") as table:
    writer = csv.writer(table)
    writer.writerow(fields)
    writer.writerows(rows)


# print(op)
# with open(file_path, 'w') as f:
#     f.write(op)
