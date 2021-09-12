# -*- coding: utf-8 -*-
from functions.Functions import Functions as Selenium
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class selectidioma(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_010(self):
        Selenium.get_elements(self, "llamar").click()
        self.driver.find_element_by_xpath("//a[contains(.,'Te llamamos gratis ahora')]").click()
        Selenium.esperar(self, 2)
        self.driver.find_element_by_xpath("//button[contains(.,'✕')]").click()
        self.driver.find_element_by_xpath("//a[contains(.,'Te llamamos gratis ahora')]").click()
        self.driver.find_element_by_xpath("//input[@type='tel']").send_keys("661111111")
        self.driver.find_element_by_xpath("/input[@type='tel']").send_keys(Keys.ESCAPE)
        self.driver.find_element_by_xpath("//a[contains(.,'Te llamamos gratis ahora')]").click()


    def tearDown(self):
        Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
