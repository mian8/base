#coding=utf-8
'''
Created on 2016年11月29日

@author: lenovo
'''

from selenium import webdriver
import unittest,time

class base(unittest.TestCase):
    def setUp(self):
        self.base_url="http://113.204.68.206:2501/m/mall/views/main/index.html"
        self.account='18140154995'
        self.pwd='qwer1234'
        
    def tearDown(self):
        self.driver.close()

    def etest_login(self):
        self.open_window()
        self.login_account(self.account, self.pwd)
        self.driver.find_element_by_link_text("我的").click()
        time.sleep(1)
        self.driver.find_element_by_id('exitlogin').click()
 
    def test_qd(self):
        self.open_window()
        self.login_account(self.account, self.pwd)
        time.sleep(1)
        qd=self.driver.find_element_by_class_name('col_03').text
        self.assertEqual('签到', qd)
        #self.driver.find_element_by_link_text("我的").click()
        #self.money=self.driver.find_element_by_id(id_)
        #self.driver.find_element_by_id('qd').click()
        #self.driver.find_element_by_link_text("我的").click()
        #self.assertEqual(first, second)

    def open_window(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get(self.base_url)
        
    def login_account(self,account,pwd):
        self.driver.find_element_by_link_text("我的").click()
        #self.driver.find_element_by_class_name("modal-buttons ").click()
        self.driver.find_element_by_id("loginAccount").send_keys(account)
        self.driver.find_element_by_id("loginPwd").send_keys(pwd)
        self.driver.find_element_by_id("loginBtn").click()

if __name__=="__main__":
    unittest.main()