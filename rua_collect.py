from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
import time
import re
import random
import collections
from urllib.parse import urlparse
from sqlalchemy import create_engine
import pandas as pd
import MySQLdb

usedb = 'sql'

if usedb == 'sql':
    server_list = ['527','553','573','543','531','535','587','530','526','574']
    already_list_before = []
    db_path = "mysq
    url_sql = urlparse(db_path)
    conn = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(host = url_sql.hostname, port=url_sql.port, user = url_sql.username, password= url_sql.password, database = url_sql.path[1:]))
    for server in server_list:
        le= 'select * from Amazon.Rua'+server
        df = pd.read_sql(le, conn)
        for asin in df['ASIN']:
            already_list_before.append(asin)







counter = collections.Counter(already_list_before)



already_list = []



for key in counter.most_common():
    if key[1] >= 10:
        already_list.append(key[0])
    else:
        break

url_list_before = []

url = "https://salehon.com/kindle100"

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
stealth(driver,
vendor="Google Inc.",
platform="Win32",
webgl_vendor="Intel Inc.",
renderer="Intel Iris OpenGL Engine",
fix_hairline=True,
)

driver.get(url)
time.sleep(2)

elements = driver.find_elements_by_css_selector('.wpap-tpl.wpap-tpl-with-detail')
for element in elements:
    el = element.find_element_by_class_name('wpap-link')
    try:
        atag = el.find_elements_by_tag_name('a')[1]
        url = atag.get_attribute('href')
    except:
        atag = el.find_elements_by_tag_name('a')[0]
        url = atag.get_attribute('href')
    place = url.find("/dp/")
    product_number = url[place+4:place+14]
    url_list_before.append("https://www.amazon.co.jp/dp/"+product_number)

url = "https://www.uragaminote.com/entry/post-9186/"

driver.get(url)
time.sleep(2)

elements = driver.find_elements_by_css_selector('.amazon-item-content.product-item-content.cf')
for element in elements:
    er = element.find_element_by_css_selector('.amazon-item-snippet.product-item-snippet')
    place = er.text.find('')
    num = er.text[place-3:place]
    if len(re.sub('\d+', '', num)) == 0:
        url = element.find_element_by_css_selector('.amazon-item-title.product-item-title').find_element_by_tag_name('a').get_attribute('href')
        place = url.find("/dp/")
        product_number = url[place+4:place+14]
        url_list_before.append("https://www.amazon.co.jp/dp/"+product_number)

url = 'https://gekiyasu-gekiyasu.doorblog.jp/book/1941281.html'
driver.get(url)
time.sleep(2)

element = driver.find_element_by_class_name('mainmore')

atag = element.find_elements_by_tag_name('a')

gekiyasu_list = []

count = 0
for a in atag:
    url = a.get_attribute('href')
    if url[:16] == 'https://amzn.to/' and count < 10: #10
        gekiyasu_list.append(url)
        count += 1
    elif count >=20:
        break
for url in gekiyasu_list:
    driver.get(url)
    element = driver.find_element_by_class_name('nav-search-field')
    inp = element.find_element_by_tag_name('input')
    letters = inp.get_attribute('value')
    letter_list = letters.split('|')
    for product_number in letter_list:
        url_list_before.append("https://www.amazon.co.jp/dp/"+product_number)


url = "http://gekiyasutoka.com/archives/80591983.html"

driver.get(url)
time.sleep(2)

article = driver.find_element_by_class_name('article-body-inner')

elements = article.find_elements_by_tag_name('a')

for element in elements:
    url = element.get_attribute("href")
    place = url.find("/dp/")
    if place != -1:
        product_number = url[place+4:place+14]
        url_list_before.append("https://www.amazon.co.jp/dp/"+product_number)

url = "https://work-outer.com/kindle-free/kindle_100cashback/"

driver.get(url)
time.sleep(2)

elements = driver.find_elements_by_css_selector('.amazon_item_container.row_item_1')

for element in elements:
    atag = element.find_element_by_tag_name('a')
    url = atag.get_attribute("href")
    place = url.find("/dp/")
    if place != -1:
        product_number = url[place+4:place+14]
        url_list_before.append("https://www.amazon.co.jp/dp/"+product_number)

driver.quit()

url_list_before = list(set(url_list_before))



url_list = []

for url in url_list_before:
    if not url[28:] in already_list:
        url_list.append(url)



while True:
    try:
        instructions = initialize_VPN(area_input=["Japan"])
        rotate_VPN(instructions)
        break
    except:
        pass

time.sleep(5)

check_list = []

ok_list = []

count = 0

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-desktop-notifications')
options.add_argument("--disable-extensions")
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

driver.get('https://t.co/RP19yTB5m2?amp=1')

time.sleep(8)
driver.find_element_by_xpath('/html/body/center/div[1]/a').click()
time.sleep(2)
for url in url_list:
    driver.get(url)
    series_flag = False
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID,"series-childAsin-item_1")))
        series_flag = True
    except:
        pass
    if series_flag:
        check_list.append(url[28:])
        tmp = []
        for i in range(1,11):
            try:
                element = driver.find_element_by_id("series-childAsin-item_"+str(i))
                price = element.find_element_by_css_selector(".a-size-large.a-color-price")
                price = re.sub("\\D", "", price.text)
                point_list = element.find_elements_by_css_selector(".a-size-base-plus.itemPoints")
                if len(point_list) != 0:
                    point = re.sub("\\D", "", point_list[0].text)
                else:
                    point_list = element.find_elements_by_css_selector('.a-size-base.a-color-price.itemPoints')
                    place = point_list[0].text.find('(')
                    point = re.sub("\\D", "", point_list[0].text[:place])
                if price == point:
                    atag = element.find_element_by_css_selector(".a-size-base-plus.a-link-normal.itemBookTitle.a-text-bold")
                    url_original = atag.get_attribute("href")
                    place = url_original.find("/product/")
                    product_number = url_original[place+9:place+19]
                    tmp.append(product_number)
                    print(product_number)
            except:
                pass
        check_list.append(tmp)
    else:
        price = 10000000
        point = 20000000
        count = 0
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,"tmm-olp-links")))
            add = driver.find_elements_by_class_name('tmm-olp-links')
        except:
            add = []

        for letters in add:
            if '' in letters.text:
                count += 1
                WebDriverWait(letters, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".extra-message.olp-link")))
                price_element = letters.find_element_by_css_selector(".extra-message.olp-link")
                if "Kindle " in price_element.text:
                    price = int(re.sub(r"\D", "", price_element.text))
                WebDriverWait(letters, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".a-size-mini.a-color-secondary.extra-message")))
                point_element = letters.find_element_by_css_selector(".a-size-mini.a-color-secondary.extra-message")
                if "" in point_element.text:
                    point = int(re.sub(r"\D", "", point_element.text))
        if count == 0 and len(add)!=0:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".a-button.a-button-selected.a-spacing-mini.a-button-toggle.format")))
            add_element = driver.find_element_by_css_selector(".a-button.a-button-selected.a-spacing-mini.a-button-toggle.format")
            try:
                WebDriverWait(add_element, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".a-size-base.a-color-price.a-color-price")))
                if "" in add_element.find_element_by_css_selector(".a-size-base.a-color-price.a-color-price").text:
                    price_element = add_element.find_element_by_css_selector(".a-size-base.a-color-price.a-color-price")
                    price = int(re.sub(r"\D", "", price_element.text))
                WebDriverWait(add_element, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".a-color-price.a-text-normal")))
                if "" in add_element.find_element_by_css_selector(".a-color-price.a-text-normal").text:
                    point_element = add_element.find_element_by_css_selector(".a-color-price.a-text-normal")
                    point = int(re.sub(r"\D", "", point_element.text))
            except:
                pass
        if price == point and price != 0:
            ok_list.append(url[28:])
            print(url[28:])

revive_list = []
matome_list = []



for i in range(len(check_list)//2):
    matome_list.append(check_list[2*i])
    for revive in check_list[2*i+1]:
        revive_list.append(revive)

final_list = revive_list + ok_list

letter = ""

final_list = list(set(final_list))

last = []

for fl in final_list:
    if not fl in already_list:
        last.append(fl)

for fin in last:
    letter += fin + "|"

print(letter)

driver.quit()

terminate_VPN(instructions)





