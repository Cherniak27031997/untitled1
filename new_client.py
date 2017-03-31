# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest, time, re
class Test_new_client_for_websystems(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://web-systems.solutions/"
    def test_new_client_for_websystems(self):
        driver = self.driver
        self.open_start_page(driver)
        self.star_creat_new_client(driver)
        self.method_name(driver)
        self.method_email(driver)
        self.method_profity(driver)
        driver.find_element_by_id('q4').send_keys('testetettetetettetetettetettetetteet')
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button').click()
        time.sleep(5)
        driver.find_element_by_id('q5').send_keys('55555')
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button').click()
        time.sleep(5)
        driver.find_element_by_id('q6').send_keys('city')
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/form/button').click()
        time.sleep(5)
        self.assertEqual("Thanks. We contact with you as soon as possible",driver.find_element_by_css_selector("p").text)

    def method_profity(self, driver):
        driver.find_element_by_id('Слой_1').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button').click()
        time.sleep(5)

    def method_email(self, driver):
        driver.find_element_by_id('q2').send_keys('test@mail.com')
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button').click()
        time.sleep(5)

    def star_creat_new_client(self, driver):
        driver.find_element_by_id("btn-colorful").click()
        time.sleep(5)

    def open_start_page(self, driver):
        driver.get(self.base_url)
        time.sleep(5)

    def method_name(self, driver):
        driver.find_element_by_id('q1').send_keys('test')
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
   unittest.main()
