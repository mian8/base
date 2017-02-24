from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://wwww.youdao.com")
driver.find_element_by_id('translateContent').send_keys('hello')
sleep(3)
#提交输入框的内容
driver.find_element_by_id('translateContent').send_keys(Keys.ENTER)
