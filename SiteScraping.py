import requests
import csv
from bs4 import BeautifulSoup

allInOne = []
for i in range(1,5):
        url="https://www.independentpharmacydirectory.com/page/"+str(i)
        print (url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        addressList = soup.find_all(class_='listing-address')
        for j in addressList:
            allInOne.append(j.text)
        with open ('address_list.csv', 'w',) as f:
            for x in allInOne:
                f.write(x)
                f.write('\n')