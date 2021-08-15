from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import concurrent.futures
from time import sleep
import time 
import re
from datetime import timedelta
import random
from urllib.parse import urlparse
from sqlalchemy import create_engine
import pandas as pd
import MySQLdb



db_path = "mysql://Amazon"
url_sql = urlparse(db_path)
conn = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(host = url_sql.hostname, port=url_sql.port, user = url_sql.username, password= url_sql.password, database = url_sql.path[1:]))

def m(letter):
    list = letter.split(" ")
    answer = ""
    for i in list:
        answer += "."
        answer += i
    return answer
                          
def google(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-desktop-notifications')
    options.add_argument("--disable-extensions")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--lang=ja')
    options.add_argument('--blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=options)
    stealth(driver,
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
    )
    driver.get(url)
    sleep(10)
    elements = driver.find_elements_by_css_selector(".a-section.profile-at-no-contributions")
    if len(elements) == 0:
        num_review = int(driver.find_elements_by_css_selector(m('a-size-large a-color-base'))[1].text)
        for i in range(int(num_review)//10):
            driver.execute_script("window.scrollTo(0, 1000000);")
            sleep(max(2.5,random.random()*7))
        list = []
        sum = 0
        for j in range(5):
            selecter = m('a-icon a-icon-star a-star-'+str(j+1)+' profile-at-review-stars')
            checker = driver.find_elements_by_css_selector(selecter)
            list.append(len(checker))
        return list
        driver.quit()
    else:
        driver.quit()


df = pd.read_sql("select * from Amazon.B08JCGVDL1", conn)

count = 0
for user_id in df['id']:
    user_name = df['username'][count]
    url = "https://www.amazon.co.jp/gp/profile/amzn1.account."+user_id
    letter = 'select * from Amazon.User where username = "'+user_name+'"'
    dfu = pd.read_sql(letter, conn)
    flag = True
    if len(dfu) != 0:
        for each_id in dfu['id']:
            if each_id[:10] == user_id[:10]:
                flag = False
    if flag:
        glist = google(url)
        if(glist==None):
            glist = [-1,-1,-1,-1,-1]
        try:
            conn.execute('insert into Amazon.User values("'+user_id+'","'+user_name+'", '+str(glist[0])+' ,'+str(glist[1])+','+str(glist[2])+','+str(glist[3])+' ,'+str(glist[4])+')')
        except:
            pass
    count += 1
