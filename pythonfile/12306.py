import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.zhihu.com//signin?next=%2F/')

driver.find_element_by_xpath('//button[@data-za-detail-view-id="2278"]').click()
driver.find_element_by_xpath('//input[@name="username"]').send_keys('account')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('password',Keys.ENTER)
time.sleep(10)
cookies=driver.get_cookies()
print(cookies)


s=requests.session()
c=requests.cookies.RequestsCookieJar()
for item in cookies:
    c.set(item["name"],item["value"])
print(c)
s.cookies.update(c)