# -*- coding: utf-8 -*-

import unittest
import time
from functions.Functions import Functions as Selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
horaGlobal = time.strftime("%H%M%S")

class test_008(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.iberostar.com/")
        Selenium.page_has_loaded(self)

    def test_008(self):

        localizador = self.driver.find_element(By.ID,"agree-cookies")
        self.driver.execute_script("arguments[0].click();", localizador)
        # self.driver.find_element_by_id("agree-cookies").click()
        localizador = self.driver.find_element(By.XPATH,"//*[contains(@class,'fake-select') and contains(.,'Escribe')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
        self.driver.execute_script("arguments[0].click();", localizador)
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element_by_xpath("(//div[@class='option'][contains(.,'Cala Millo')])[1]").click()
        localizador = self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'Entrada')]")
        self.driver.execute_script("arguments[0].click();", localizador)
        localizador = self.driver.find_element(By.XPATH, "//div[contains(@data-id,'24082020')]")
        self.driver.execute_script("arguments[0].click();", localizador)
        localizador = self.driver.find_element(By.XPATH, "//div[contains(@data-id,'30082020')]")
        self.driver.execute_script("arguments[0].click();", localizador)
        localizador = self.driver.find_element(By.XPATH, "//span[contains(@class,'book-now')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
        self.driver.execute_script("arguments[0].click();", localizador)

        time.sleep(5)


        title = "Test_008"
        self.driver.get_screenshot_as_file(f"../data/capturas/{title}-{horaGlobal}.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
