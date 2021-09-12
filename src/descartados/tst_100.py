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

class test_100(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_100(self):
        Selenium.page_has_loaded(self)
        Selenium.get_json_file(self, "ibero")
        localizador = self.driver.find_element(By.ID, "agree-cookies")
        self.driver.execute_script("arguments[0].click();", localizador)
        localizador = self.driver.find_element(By.XPATH,"//*[contains(@class,'fake-select') and contains(.,'Escribe')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
        self.driver.execute_script("arguments[0].click();", localizador)
        Selenium.get_elements(self, "write").send_keys("Iberostar Cristina")
        Selenium.get_elements(self, "write").send_keys(Keys.ENTER)
        localizador = self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'Entrada')]")
        self.driver.execute_script("arguments[0].click();", localizador)
        localizador = self.driver.find_element(By.XPATH, "//div[contains(@data-id,'26072020')]")
        self.driver.execute_script("arguments[0].click();", localizador)
        localizador = self.driver.find_element(By.XPATH, "//div[contains(@data-id,'30082020')]")
        self.driver.execute_script("arguments[0].click();", localizador)
        localizador = self.driver.find_element(By.XPATH, "//button[contains(@id,'book-now')]")
        self.driver.execute_script("arguments[0].click();", localizador)

        time.sleep(5)


        title = "Test_100"
        self.driver.get_screenshot_as_file(f"../data/capturas/{title}-{horaGlobal}.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
