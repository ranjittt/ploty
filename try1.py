from bs4 import BeautifulSoup
import requests
import plotly.express as px


url = BeautifulSoup("https://www.worldometers.info/coronavirus/","html.parser")
soup = requests.get(url)
import csv

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
df=dict(dx)
commoncountries=[]
for i in df['country']:
    if (i in countries )and (i not in commoncountries):
        commoncountries.append(i)

print(len(commoncountries))

di = 0#this is the data index
alliso_apha = []
for i in commoncountries:
    x=list(df["country"])
    iso = list(df["iso_alpha"])
    if i in x:
        di = x.index(i)
        x = iso[di]
        alliso_apha.append(x)

