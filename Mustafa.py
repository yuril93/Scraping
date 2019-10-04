from time import gmtime, strftime
import time
import requests
import re
from xlsxwriter import Workbook
from bs4 import BeautifulSoup

from selenium import webdriver

workbook = Workbook('MUSTAFA.xlsx')
worksheet = workbook.add_worksheet('1')
worksheet.write(0,0,"Title")
worksheet.write(0,1,"Cost")
worksheet.write(0,2,"Style")
worksheet.write(0,3,"Stock")
worksheet.write(0,4,"Spec")
worksheet.write(0,5,"Images")
worksheet.write(0,6,"Images")



browser = webdriver.Chrome(executable_path=r"C:\Users\Ashunik\Downloads\chromedriver.exe")
browser.get("https://qgold.com/Login")

browser.find_element_by_name("username").send_keys("goldia")
browser.find_element_by_name("pass").send_keys("winston7")
browser.find_element_by_name("account").send_keys("52544")
browser.find_element_by_id("login_btn").click()
time.sleep(3)

all3000items=[]
z=0
for i in range(1,2):
    link ="https://qgold.com/ps/72728/charm/"+str(i)+str("/5?")
    browser.get(link)
    elements=browser.find_elements_by_xpath('//*[@id="main_product_list"]/li/div/a')
    time.sleep(2)
    for i in elements:
        all3000items.append(i.get_attribute('href'))

print (all3000items)
for x in all3000items:
    print (x)
    browser.get(x)

    try:
        attributes="<br>"+(browser.find_element_by_xpath('//*[@id="attributes_container"]/ul').text).replace('\n',"</br><br>")+"</br>"
    except:
        attributes="N/A"
    cost=int(float(((browser.find_element_by_xpath('//*[@id="features_info"]/p[2]/span[2]').text).replace('$',''))))
    specs=(browser.find_element_by_xpath('//*[@id="Specs"]/ul').text).replace('Status:','').replace('Active','').replace(':\n',': ').replace('\n',"</br><br>").replace('</br><br></br><br>','<br>')+"</br>"
    style=browser.find_element_by_xpath('//*[@id="features_info"]/p[3]/span[2]').text
    stock=browser.find_element_by_xpath('//*[@id="features_info"]/p[4]/span[2]').text
    productTitle=browser.find_element_by_id('product_title').text


    imagesList=[]
    for i in browser.find_elements_by_class_name("product_image"):
        imagesList.append((i.get_attribute('src').replace('500&h','1000&h').replace('=500','=1000')))

    aaa = str(imagesList[0])
    for a in range(0,len(imagesList)):
        if a <(len(imagesList)-1):
            aaa=aaa+"|"+str(imagesList[a+1])

    print(productTitle)
    print(stock)
    print(style)
    print(attributes)
    print(specs)
    print (aaa)
    print(cost)
    specPlusattributes = specs + "<br>" + attributes

    print(z)
    z=z+1
    worksheet.write(z,0,productTitle)
    worksheet.write(z,1,cost)
    worksheet.write(z,2,style)
    worksheet.write(z,3,stock)
    worksheet.write(z,4,specPlusattributes)
    worksheet.write(z,6,aaa)

workbook.close()