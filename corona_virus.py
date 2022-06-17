from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# url = BeautifulSoup("https://www.worldometers.info/coronavirus/","html.parser")
# soup = requests.get(url)

# soup = soup.text
# soup = BeautifulSoup(soup,"lxml")
# soup = soup.find_all('tr')
# text = []

# for i in soup:
#     text.append(i.text.split("\n")[1:-1])
# text = [i for i in text if i[0]!=""]
# file = open("covid.csv","w")
# writer = csv.writer(file)
# for i in text:
#     writer.writerow(i)
# file.close()

# df = pd.read_csv("covid.csv",encoding="iso-8859-1")
# countries = df['Country,Other'][:2]
# totalcase = df['TotalCases'][:2]
# contient = df["Continent"][:2]
# final_totalcase=[]
# for i in totalcase:
#     x=i.replace(",","")
#     final_totalcase.append(int(x))

# print(final_totalcase)
dx ={"countries":["USA","India"],"case":[87549563,43245517],"continent":["North America","Asia"],"iso_alpha":["USA","IND"]}
import plotly.express as px
# df = px.data.gapminder()
# x=df
# # print(type(x))
# file = open("hello.csv","w")
# writer = csv.writer(file)
# writer.writerow(df)
# for i in df.values:
#     writer.writerow(i)
# import plotly.express as px
df = px.data.gapminder()
fig = px.scatter_geo(dx, locations="iso_alpha",
                     hover_name="countries", size="case",
                     projection="natural earth")
fig.show()