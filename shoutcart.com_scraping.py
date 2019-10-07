import requests
from bs4 import BeautifulSoup

allInOne_names = []
allInOne_followers=[]
for i in range(1,68):
    url="https://shoutcart.com/browse?page="+str(i)
    print (url)
    page = requests.get(url,verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    addressList = soup.find_all(class_='teg')
    followers=soup.find_all('tr')
    for i in followers:
        followers_1=i.find_all('td')
        if len(followers_1)>0:
            allInOne_names.append((followers_1[0].text).strip())
            allInOne_followers.append((followers_1[1].text).strip())
    with open('address_list.csv', 'w', encoding='utf-8') as z:
        for bb in range(len(allInOne_names)):
            z.write(','.join([allInOne_names[bb].strip(),allInOne_followers[bb].replace('\n','')]))
            z.write('\n')
