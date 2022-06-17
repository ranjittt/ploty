#printing 1st page only

#step 0 import the files
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import plotly.graph_objects as go 
#step 1 : requesting the site
url = BeautifulSoup("http://nepalstock.com/todaysprice","html.parser")
soup = requests.get(url)

#step 2: parsing the data
soup=soup.text
soup = BeautifulSoup(soup,"lxml")
soup = soup.find_all('tr')
text = []
for i in soup:
    text.append(i.text.split('\n')[1:11])
text = [i for i in text if i[0]!=""]

file=open("nep.csv","w")
writer = csv.writer(file)
for i in text:
    writer.writerow(i)
file.close()
#step 3: fetching the data
df= pd.read_csv("nep.csv",encoding="iso-8859-1")
companies = df['Traded Companies'][:20]
max_price = df['Max Price'][:20]
final_max_price=[int(i) for i in max_price]

#step 5 displaying
fig = go.Figure([go.Bar(x=companies, y=final_max_price)])
fig.show()