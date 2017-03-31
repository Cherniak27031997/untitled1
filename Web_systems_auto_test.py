import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, re

class Test(unittest.TestCase):

    def Test(self):
        self.driver = webdriver.Firefox()

    def test_newclient(self):
        driver = self.driver
        driver.get("http://www.web-systems.solutions")
        time.sleep(5)


        elem = driver.find_element_by_xpath('//*[@id="btn-colorful"]')
        elem.click()
        time.sleep(5)

        elem1 = driver.find_element_by_xpath('//*[@id="q1"]')
        elem1.send_keys('test')

        elem2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button')
        elem2.click()
        time.sleep(5)

        elem3 = driver.find_element_by_xpath('//*[@id="q2"]')
        elem3.send_keys('test@mail.com')

        elem4 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button')
        elem4.click()
        time.sleep(5)

        elem5 = driver.find_element_by_xpath('//*[@id="Слой_1"]')
        elem5.click()

        elem6 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button')
        elem6.click()
        time.sleep(4)

        elem7 = driver.find_element_by_xpath('//*[@id="q4"]')
        elem7.send_keys('testtetstestetsetsetestestestestetsetse')

        elem8 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button')
        elem8.click()
        time.sleep(5)

        elem9 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/form/ol/li[5]')
        elem9.send_keys('1000')

        elem10 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/button')
        elem10.click()
        time.sleep(5)

        elem11 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/form/button')
        elem11.location_once_scrolled_into_view
        time.sleep(5)



        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()
