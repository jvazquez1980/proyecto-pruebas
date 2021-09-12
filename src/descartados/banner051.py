# -*- coding: utf-8 -*-

import unittest
import time
from functions.Functions import Functions as Selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class banner(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_051(self):
        Selenium.page_has_loaded(self)
        Selenium.get_json_file(self, "elements")
        Selenium.scroll_to(self, "banner1")
        Selenium.check_element(self, "banner1")
        Selenium.check_element(self, "banner2")
        Selenium.check_element(self, "banner3")
        Selenium.check_element(self, "banner2")
        Selenium.get_elements(self, "banner4").click()
        Selenium.esperar(self, 5)

        Selenium.capturar_pantalla(self)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
