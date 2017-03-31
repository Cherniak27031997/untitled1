import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class my_setup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.halliver.crcl.cf/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_holliver_search(self):
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("Интернет магазин часов", driver.title)
        element1 = driver.find_element_by_css_selector("button[type=\"submit\"]")
        element1.click()
        element2 = driver.find_element_by_name("Filter[query]")
        element2.clear()
        element2.send_keys("Logo")
        assert "No results found." not in driver.page_source
        element2.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
