from bs4 import BeautifulSoup
import pandas
import requests
import csv
# Step 1

url = BeautifulSoup("http://quotes.toscrape.com/tableful/","html.parser")
soup = requests.get(url)

#step 2

soup = soup.text
soup = BeautifulSoup(soup,"lxml")
quotes = soup.find_all('td')
text = []
for i in quotes:
    text.append(i.text.split('\n'))

text = [i for i in text if i[0]!=""]
text = text[::2]

file = open("quotes.txt","w")
writer = csv.writer(file)
for i in text:
    writer.writerow(i)
file.close()

file =open("quotes.txt","r")
print(file.read())
file.close()