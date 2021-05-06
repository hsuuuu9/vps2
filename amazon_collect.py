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
#from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-desktop-notifications')
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")
#options.add_argument('--headless')
options.add_argument('--lang=ja')
options.add_argument('--blink-settings=imagesEnabled=false')
def class_click(classname):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, classname)))
    try:
        driver.find_element_by_class_name(classname).click()
    except:
        print('fail')

def class_send(classname,chara):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, classname)))
    try:
        driver.find_element_by_class_name(classname).send_keys(chara)
    except:
        print('fail')

def id_click(idname):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, idname)))
    try:
        driver.find_element_by_id(idname).click()
    except:
        print('fail')

def id_send(idname,chara):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, idname)))
    try:
        driver.find_element_by_id(idname).send_keys(chara)
    except:
        print('fail')

def name_click(name):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, name)))
    try:
        driver.find_element_by_name(name).click()
    except:
        print('fail')

def name_send(name,chara):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, name)))
    try:
        driver.find_element_by_name(name).send_keys(chara)
    except:
        print('fail')

def name_click(name):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, name)))
    try:
        driver.find_element_by_name(name).click()
    except:
        print('fail')

def name_send(name,chara):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, name)))
    try:
        driver.find_element_by_name(name).send_keys(chara)
    except:
        print('fail')
def xpath_click(xpath):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    try:
        driver.find_element_by_xpath(xpath).click()
    except:
        print('fail')
def m(letter):
    list = letter.split(" ")
    answer = ""
    for i in list:
        answer += "."
        answer += i
    return answer

def css_click(queryname):
    y = False
    while y == False:
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, queryname)))
            driver.find_element_by_css_selector(queryname).click()
            y = True
        except:
            pass

driver = webdriver.Chrome(options=options)
stealth(driver,
vendor="Google Inc.",
platform="Win32",
webgl_vendor="Intel Inc.",
renderer="Intel Iris OpenGL Engine",
fix_hairline=True,
)

url = "https://www.amazon.co.jp/gp/product/B08T5TDQ1P/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1"
driver.get(url)


css_click(m("a-link-emphasis a-text-bold"))

sleep(5)


element = driver.find_element_by_id("filter-info-section")
before = element.text.find("|")
after = element.text.find("グローバルレビュー")
review_num_all = int(element.text[before+2:after-1])

url_list = []
name_list = []
star_list = []
original_url = driver.current_url
for root in range(review_num_all//10 + 1):
    driver.delete_all_cookies()
    driver.get(original_url + "&pageNumber="+str(root+1))
    sleep(2)
    elements = driver.find_elements_by_css_selector(m('a-row a-spacing-none'))
    for element in elements:
        try:
            aTag = element.find_element_by_tag_name("a")
            if 'gp/profile/' in aTag.get_attribute("href"):
                url_list.append(aTag.get_attribute("href"))
        except:
            pass
        try:
            star = element.find_element_by_class_name('a-link-normal')
            if '5つ星のうち' in star.get_attribute('title'):
                star_list.append(int(star.get_attribute('title')[6]))
        except:
            pass
        try:
            name = element.find_element_by_class_name('a-profile-name').text
            name_list.append(name)
        except:
            pass
driver.quit()


db_path = "mysql://shuichi:V3Bty@45.32.249.213:3306/Amazon"
url_sql = urlparse(db_path)
conn = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(host = url_sql.hostname, port=url_sql.port, user = url_sql.username, password= url_sql.password, database = url_sql.path[1:]))

for i in range(len(url_list)):
    sqlid = url_list[i][50:78]
    star = star_list[i]
    username = name_list[i]
    username = username.replace('"','')
    username = username.replace("'","")
    letter = 'insert into Amazon.B08JCGVDL1 values ("'+sqlid+'","'+username+'",'+str(star)+');'
    conn.execute(letter)
