

#step 1: sending requests

from bs4 import BeautifulSoup
import requests
import csv


url =BeautifulSoup("https://www.worldometers.info/coronavirus/","html.parser")
soup=requests.get(url)

#step 2 parsing the data

soup=soup.text

soup = BeautifulSoup(soup,"lxml")
soup = soup.find_all('tr')
text = []
for i in soup:
    text.append(i.text.split('\n')[1:-1])

# print(text)
file1=open("file1.csv","w")
writer = csv.writer(file1)
for i in text:
    if len(i) ==20:
        writer.writerow(i)

