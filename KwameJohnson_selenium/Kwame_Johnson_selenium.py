import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import os

csvPath="C:/Users/Ashunik/Desktop/Python_yuril/KwameJohnson_selenium/"
x = datetime.datetime.now()
nowDate=(str(x.day)+"-"+(str(x.strftime("%b")).upper())+"-"+str(x.year))
todayCSV=str(nowDate)+".csv"
todayCSVpath=(str(csvPath)+todayCSV)
print (nowDate)

# 190902462
# 190901280

while True:
    try:
        caseIDinput=input("Please input Case ID: ")
        print ("Processing ...")
        break
    except:
        print("something is wrong!")
        exit()

chrome_options = Options()
chrome_options.add_argument("--headless")
# chromedriver.exe path
browser = webdriver.Chrome(executable_path=r"C:\Users\Ashunik\Downloads\chromedriver.exe",options=chrome_options)
browser.get("https://fjdefile.phila.gov/efsfjd/zk_fjd_prvt_efile_00.secured_logon?tid=&redir=_Mn")
#
#while True:
#    try:
#        browser.get("https://fjdefile.phila.gov/efsfjd/zk_fjd_prvt_efile_00.secured_logon?tid=&redir=_Mn")
#        break
#    except:
#        print("Browser do not response, trying to conect ...")
#        browser.refresh()
#        time.sleep(10)

browser.find_element_by_name("username").send_keys("cjohnson18")
browser.find_element_by_name("passwd").send_keys("CcpvoB")
browser.find_element_by_name("pin").send_keys("62166")
browser.find_element_by_xpath("/html/body/center[1]/font/blockquote/form/table/tbody/tr[3]/td/font/input").click()
browser.find_element_by_link_text("Display Civil Docket Report").click()
browser.find_element_by_name("case_id").send_keys(caseIDinput)
browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/blockquote/form/input[3]").click()

##CSV inputs##

CaseID=(browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[2]/table/tbody/tr[1]/td[3]").text)
CaseCaption=(browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[2]/table/tbody/tr[2]/td[3]").text)
Court = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[2]/table/tbody/tr[4]/td[3]").text)
FillingDate = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[2]/table/tbody/tr[3]/td[3]").text)
CaseType = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[2]/table/tbody/tr[7]/td[3]").text)
CaseStatus = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[2]/table/tbody/tr[8]/td[3]").text)
Plaintiff = (browser.find_element_by_xpath("//html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[5]/td[5]").text+","+browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[6]/td[2]").text)


if browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[8]/td[4]").text=="DEFENDANT":
    Defendant1 = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[8]/td[5]").text+","+browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[9]/td[2]").text)
    Defendant1AddressLine1 = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[9]/td[1]").text)
else:
    Defendant1 = "N/A"
    Defendant1AddressLine1= "N/A"

if browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[11]/td[4]").text=="DEFENDANT":
    Defendant2 = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[11]/td[5]").text+","+browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[12]/td[2]").text)
    Defendant2AddressLine1 = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[12]/td[1]").text)
else:
    Defendant2 = "N/A"
    Defendant2AddressLine1 = "N/A"

if browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[14]/td[4]").text=="DEFENDANT":
    Defendant3 = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[14]/td[5]").text+","+browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[15]/td[2]").text)
    Defendant3AddressLine1 = (browser.find_element_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[6]/table/tbody/tr[15]/td[1]").text)
else:
    Defendant3 = "N/A"
    Defendant3AddressLine1 = "N/A"

list=browser.find_elements_by_xpath("/html/body/font/table[3]/tbody/tr/td/font/a[7]/table[1]/tbody/tr/td[4]")
for i in list:
    if "$" in i.text:
        JudgementAmount=(i.text).strip('\n')
        break
    else:
        JudgementAmount="N/A"
browser.__exit__()
if todayCSV in (os.listdir(csvPath)):
    with open(csvPath+todayCSV, 'a',newline='') as z: #.csv file path
        writer = csv.writer(z)
        data = [CaseID,CaseCaption,Court,FillingDate,CaseType,CaseStatus,Plaintiff,Defendant1,Defendant1AddressLine1,Defendant2,Defendant2AddressLine1,Defendant3,Defendant3AddressLine1,JudgementAmount]
        writer.writerow(data)
    z.close()
else:
    with open(csvPath+todayCSV, 'w',newline='') as z: #.csv file path
        writer = csv.writer(z)
        data = [CaseID,CaseCaption,Court,FillingDate,CaseType,CaseStatus,Plaintiff,Defendant1,Defendant1AddressLine1,Defendant2,Defendant2AddressLine1,Defendant3,Defendant3AddressLine1,JudgementAmount]
        writer.writerow(["Case ID","Case Caption","Court","Filling Date","Case Type","Case Status","Plaintiff","Defendant 1","Defendant 1 Address Line 1","Defendant 2","Defendant 2 Address Line 1","Defendant 3","Defendant 3 Address Line 1","Judgement Amount ($)"])
        writer.writerow(data)
    z.close()
print ("Done")
time.sleep(2)