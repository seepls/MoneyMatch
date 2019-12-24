
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from datetime import datetime, timedelta
import regex as re
import calendar


# In[2]:


#Converts month abrreviations to month number to convert into datetime
def replace_month_by_number(date):
    date_copy = date[:]
    months = list(calendar.month_abbr)[1: ]
    for idx, month in enumerate(months, 1):
        if month in date:
            date_copy = date_copy.replace(month, str(idx))
    return date_copy


# In[3]:


def parse_date(date):
    date = date.strip()
    date = replace_month_by_number(date)
    date = re.sub(r'[^A-Za-z0-9 ]+', '', date).strip()
#     print(date)
    try:
        date_obj = datetime.strptime(date, '%m %d %Y')
    except ValueError:
        num = int(re.sub(r'[^0-9]+', '', date).strip())
#         print(num)
        hour_or_min = {'minutes' : num} if 'minutes' in date else {'hours' : num}
        date_obj = datetime.now() - timedelta(**hour_or_min)
        date_obj = date_obj.replace(second=0, microsecond=0)
        
    return date_obj


# In[4]:


parse_date('Dec 27, 2019')


# In[5]:


parse_date(' - 47 minutes ago')


# In[6]:


datetime.now() > (datetime.now() - timedelta(days=7))


# In[7]:


# url = 'https://www.investing.com/news/latest-news'
url = 'https://www.investing.com/news/forex-news'

headers = {
    'User-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
}
http_proxy  = ""
https_proxy = ""
ftp_proxy   = ""

proxyDict = {
    "http"  : http_proxy,
    "https" : https_proxy,
    "ftp"   : ftp_proxy
}
site = requests.get(url, headers=headers, proxies=proxyDict)


# In[8]:


soup = BeautifulSoup(site.content, 'html.parser')


# In[9]:


def getArticles(driver):
    while True:
        news_span = driver.find_element_by_xpath("//div[contains(@class, 'largeTitle')]")
        for article in news_span.find_elements_by_tag_name('article'):
            try:
                link = article.find_element_by_tag_name('a')
                title = link.find_element_by_tag_name('img').get_attribute('alt')
                link = link.get_attribute('href')
                date = parse_date(article.find_element_by_class_name('date').text)
                print(article.find_element_by_class_name('date').text, date)
                
                if date < (datetime.now() - timedelta(days=7)):
                    return
                
                print(link, date)
                print()
                yield title, link, date
            
            except Exception as e:
                print(e)
                print('A google ad')
                print()

        driver.find_elements_by_xpath("//div[contains(@class, 'sideDiv')]")[-1].click()


# In[10]:


driver = webdriver.Chrome(executable_path='/home/akash/drivers/chromedriver_linux64/chromedriver')
driver.get(url)


# In[11]:


columns = ['Title', 'Link', 'Date of Article']
df = pd.DataFrame(columns=columns)

for title, link, date in getArticles(driver):
    if 'usd' in title.lower():
        df = df.append(dict(zip(columns, [title, link, date])), ignore_index=True)


# In[12]:


df

