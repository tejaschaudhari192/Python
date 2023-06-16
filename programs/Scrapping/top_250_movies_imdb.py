
import csv
csv_file = 'C:/programming/Python/programs/Scrapping/top_250_movies_imdb.csv'
fields = ['No','Movie']
rows = []

from bs4 import BeautifulSoup
import requests

website = 'https://www.imdb.com/chart/top/'
response = requests.get(website)
web = response.text

soup = BeautifulSoup(web,'html.parser')

movies_td = soup.find_all(name='td',class_='titleColumn')
# for item in movies_td:
#     print(item.getText)
movies_a = [movie.find(name='a') for movie in movies_td]
movies_list_text = [item.getText() for item in movies_a]
# movies_list = []
# for i in movies_list_text:
#     # movie = 
#     movies_list.append(i.replace('\n', ''))
print(len(movies_list_text))

no = 1
for movie in movies_list_text:
    # print(movie)
    rows.append([no, movie])
    no += 1
# print(rows)

with open(csv_file, 'w',newline='') as table:
    writer = csv.writer(table)
    writer.writerow(fields)
    writer.writerows(rows)

    

