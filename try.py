# import plotly.express as px
# df = px.data.gapminder()

# df = dict(df)

# country = df["country"]
# country = list(country)
# c="Nepal"
# for i in df["country"]:
#     # if i ==c:
#         # x=1

#  iso = list(dx["iso_alpha"])
#         alliso_alpha.append(iso[di])

# print(len(alliso_alpha))


from bs4 import BeautifulSoup
import requests
import plotly.express as px
import pandas as pd
import csv

url = BeautifulSoup("https://www.worldometers.info/coronavirus/","html.parser")
soup = requests.get(url)


soup = soup.text
soup = BeautifulSoup(soup,"lxml")
soup = soup.find_all("tr")
data = []
for i in soup:
    data.append(i.text.split('\n')[1:-1])
data = [x for x in data if x[0]!=""]

countries = []

for i in data:
    countries.append(i[1])

dx = px.data.gapminder()
dx = dict(dx)
di = 0 #data index
alliso_alpha = []
iso = 0
print(len(countries))
# for i in countries:
#     x = list(dx["country"])
#     if i in x:
#         di =x.index(i)
#         print(type(di))
        # alliso_alpha.append(di)

# print(len(alliso_alpha))
