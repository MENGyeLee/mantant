import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://kyfw.12306.cn/otn/resources/login.html/')

driver.find_element_by_xpath('//li[@class="login-hd-account"]').click()
driver.find_element_by_xpath('//input[@id="J-userName"]').send_keys('account')
driver.find_element_by_xpath('//input[@id="J-password"]').send_keys('password',Keys.ENTER)
time.sleep(10)
cookies=driver.get_cookies()
print(cookies)


s=requests.session()
c=requests.cookies.RequestsCookieJar()
for item in cookies:
    c.set(item["name"],item["value"])
print(c)
s.cookies.update(c)