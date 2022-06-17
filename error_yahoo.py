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
soup  =soup.find_all('tr')
text=[]
for i in soup:
    text.append(i.text.split('\n'))
print(text)