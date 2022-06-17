from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import plotly.graph_objects as go 
#step 1: sending requests

# url = BeautifulSoup("https://www.worldometers.info/coronavirus/","html.parser")
soup = requests.get("https://www.worldometers.info/coronavirus/")


#step 2: parsing the data
soup=soup.text
soup=BeautifulSoup(soup,"lxml")

#step 3: fetching the data
x=soup.find_all('tr')
text=[]
for i in x:
    text.append(i.text.split('\n')[1:-1])

text = [x for x in text if x[0]!=""]

file = open("data.csv","w")
x=csv.writer(file)
x.writerows(text)

df=pd.read_csv("data.csv",encoding="iso-8859-1")
total_death=df['TotalDeaths'][:5]
final_total_death = []
for i in total_death:
    x=i.replace(",","")
    final_total_death.append(int(x))
countries=df['Country,Other'][:5]

fig = go.Figure([go.Bar(x=countries, y=final_total_death)])
fig.show()