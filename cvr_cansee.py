from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import random
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-gpu')
options.add_experimental_option('useAutomationExtension', False)
#options.add_argument('--user-data-dir=C:\\Users\\Shuichi\\Desktop\\userprofile_main')#user
#options.add_argument('--profile-directory=Default')
options.add_argument('--disable-desktop-notifications')
options.add_argument("--disable-extensions")
options.add_argument('--lang=ja')
options.add_argument('--user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/532.36 (KHTML, like Gecko) Chrome/80.0.4430.93 Safari/532.36')
#options.add_argument('--blink-settings=imagesEnabled=false')

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=options)
stealth(driver,
vendor="Google Inc.",
platform="Win32",
webgl_vendor="Intel Inc.",
renderer="Intel Iris OpenGL Engine",
fix_hairline=True,
)


url = "https://twitter.com/600k_labo"

l = ".css-4rbku5.css-18t94o4.css-901oao.css-16my406.r-1n1174f.r-1loqt21.r-poiln3.r-bcqeeo.r-qvutc0"
for root in range(2):
    driver.get(url)
    time.sleep(5)
    time.sleep(random.random()*1.5 + 2)
    elements = driver.find_elements_by_css_selector(l)
    p = 0
    q = 0
    for i in range(2):
        while True:
            try:
                elements[i*2+1].click()
                time.sleep(random.random()*1.5 + 2)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(random.random()*1.5 + 2)
                break
            except:
                driver.execute_script("window.scrollTo(0, "+str(p*200)+");")
                p += 1
        while True:
            try:
                elements[i*2+2].click()
                time.sleep(random.random()*1.5 + 2)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(random.random()*1.5 + 2)
                break
            except:
                driver.execute_script("window.scrollTo(0, "+str(q*200)+");")
                q += 1
    for k in range(len(driver.window_handles)-1):
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])

driver.quit()







import json

t = datetime.datetime.now()
fname = "aa.json"
with open(fname, "w", encoding="utf-8") as f:
        f.write(str(t.strftime('%Y-%m-%d %H:%M:%S')))
