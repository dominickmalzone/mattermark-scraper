from bs4 import BeautifulSoup
from selenium import webdriver
import urllib
import re
import csv
import time

driver = webdriver.Chrome(executable_path=r'/Users/dom/Desktop/dev/chromedriver')


#log in first

driver.get("https://mattermark.com/app/")
raw_input("Mattermark login page opened! >>PRESS ENTER HERE<< after you have logged in")

c = csv.writer(open("YOUR-NEW-DATA.csv", "wb"))
c.writerow(['Name', 'Growth Score','Mindshare','Score','Employee Count','Employee Growth Last Mo',	'Employee Growth Last 6 Months','Monthly Uniques Month Over Month Growth','Stage','Total Funding','Last Funding','Last Funding Amount',	'Location','Company Url','Facebook Page','Twitter','Linkedin', 'Angel','Crunchbase','ProductHunt','Mattermark Page'])

def get_company_details(mattermark_url,row):
    print 'getting page details for ', mattermark_url
    driver.get(url=mattermark_url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    s = str(soup)
    link_bar = soup.find('span',class_='social-icons')
    social_links = link_bar.find_all('a')

    co_website = ""
    company_fb = ""
    company_tw = ""
    company_lk = ""
    company_angel = ""
    company_cb = ""
    company_ph = ""

    webicon = link_bar.find('i',class_='fa fa-globe')
    webLink = webicon.find_parent('a')
    co_website = webLink['href']
    print 'COMPANY SITE: ', co_website

    for i in social_links:
        print 'filtering link and saving', i['href']
        if 'facebook' in i['href']:
            company_fb = i['href']
        if 'twitter' in i['href']:
            company_tw = i['href']
        if 'linkedin' in i['href']:
            company_lk = i['href']
        if 'angel' in i['href']:
            company_angel = i['href']
        if 'crunch' in i['href']:
            company_cb = i['href']
        if 'producthunt' in i['href']:
            company_ph = i['href']

    c.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[8],row[9],row[10],row[11],row[10],row[11],co_website,company_fb,company_tw,company_lk, company_angel,company_cb,company_ph,row[12]])
    time.sleep(3)

print 'starting file iteration, please wait'
time.sleep(5)

f = open('REPLACE-WITH-MM-LINK-FILE.csv')
csv_f = csv.reader(f)

for row in csv_f:
    if row[0] not in ['Name']:
        print 'parsing', row[0]
        get_company_details(row[12], row)
