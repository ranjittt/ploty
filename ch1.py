#step 0: install all the requirements
        # -- pip install bs4
        # -- pip install html5lib
        # -- pip install requests

#step 1: load all the install files

from bs4 import BeautifulSoup
import requests

#step 2:request the html
url= '''https://www.codewithharry.com/'''
r=requests.get(url)
htmlcontents = r.content
# print(htmlcontents)

#step 3: parsing the html meaing beautifing the requested html

soup = BeautifulSoup(htmlcontents,'lxml')

# print(soup.prettify())

# step4 : fetching the data from url

#To get the title 
title=soup.title
# print(title)

#to get all the paragraph
para=  soup.find_all('p')
# print(para)

#to get all the anchor tags
anchor = soup.find_all('a')
# print(anchor)


#to get the class
# print(soup.find('p')['class'])
# print(soup.find_all('p',class_='lead'))


#to get all the text
print(soup.find('p').get_text())
print(soup.find('html').get_text())