#step 1 : importing the files

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import plotly.graph_objects as go 
#step 2: requesting the site

url = BeautifulSoup("https://finance.yahoo.com/cryptocurrencies/","html.parser")
soup = requests.get(url)

#step 3: parsing the data
soup=soup.text
soup = BeautifulSoup(soup,"lxml")

#for saving the heading
theader = soup.find_all('th')
txt=[]
for i in theader:
    txt.append(i.text)
txt = txt[:12]

file = open("cypto1.csv","w")
writer = csv.writer(file)
writer.writerow(txt)
file.close()



data = soup.find_all('td')
text = []
for i in data:
    text.append(i.text)


first = 0
last = 12
best_data=[]
while last<=300:
    best_data.append(text[first:last])
    first = last
    last = last +12

file= open("cypto1.csv","a")
writer = csv.writer(file)
for i in best_data:
    writer.writerow(i)
file.close()

#step 5 fetching the data

df =pd.read_csv("cypto1.csv")
name  = df['Name']
price= df['Price (Intraday)']
final_price=[]
for i in price:
    x=i.replace(",","")
    final_price.append(float(x))

fig = go.Figure([go.Bar(x=name, y=final_price)])
fig.show()