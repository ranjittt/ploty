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
case = []
for i in data:
    countries.append(i[1])
    case.append(i[2])

#bellow
dx = px.data.gapminder()
df=dict(dx)
case = []
commoncountries=[]
total_case=[]
cx = df['country']
for i in range(len(df['country'])):
    if (cx[i] in countries )and (cx[i] not in commoncountries):
        commoncountries.append(cx[i])
        total_case.append(case[i])

print(len(total_case))        
        

print(len(commoncountries))
#above 
# di = 0#this is the data index
# alliso_apha = []
# for i in commoncountries:
#     x=list(df["country"])
#     iso = list(df["iso_alpha"])
#     if i in x:
#         di = x.index(i)
#         x = iso[di]
#         alliso_apha.append(x)

