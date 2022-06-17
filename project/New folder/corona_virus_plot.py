from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import plotly.express as px


url = BeautifulSoup("https://www.worldometers.info/coronavirus/","html.parser")
soup = requests.get(url)

soup = soup.text
soup = BeautifulSoup(soup,"lxml")
soup = soup.find_all("tr")
text = []

for i in soup:
    text.append(i.text.split("\n")[1:-1])

text = [i for i in text if i[0]!=""]

file = open("data.csv","w")
writer = csv.writer(file)
text = text[:230]
for i in text:
    writer.writerow(i)
file.close()

df = pd.read_csv("data.csv",encoding="iso-8859-1")
df = dict(df)

case = []
for i in df["TotalCases"]:
    x=i.replace(",","")
    case.append(int(x))
df["TotalCases"].update(case)

countries= df["Country,Other"]
countries = list(countries)

dx = px.data.gapminder()
dx=dict(dx)

commoncountries=[]
for i in dx['country']:
    if (i in countries )and (i not in commoncountries):
        commoncountries.append(i)
ci = 0  
total_case = []    
for i in commoncountries:
    if i in countries:
        ci = countries.index(i)
        total_case.append(case[ci])
        continue

di = 0#this is the data index
alliso_apha = []
for i in commoncountries:
    x=list(dx["country"])
    iso = list(dx["iso_alpha"])
    if i in x:
        di = x.index(i)
        x = iso[di]
        alliso_apha.append(x)

printing_data = {"iso_alpha":alliso_apha,"country":commoncountries,"TotalCases":total_case}
fig = px.scatter_geo(printing_data, locations="iso_alpha",
                     hover_name="country", size="TotalCases",
                     projection="natural earth")
fig.show()
