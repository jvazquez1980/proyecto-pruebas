# -*- coding: utf-8 -*-


from functions.Functions import Functions as Selenium
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class test_102(Selenium, unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.melia.com/es/home.htm")

    def test_102(self):
        Selenium.page_has_loaded(self)
        Selenium.get_json_file(self, "melia")
        Selenium.get_elements(self, "destino").click()
        Selenium.get_elements(self, "destino").send_keys("Bilbao")
        Selenium.get_elements(self, "fechas").click()
        Selenium.scroll_to(self, "Fi")
        Selenium.get_elements(self, "Fi").click()
        Selenium.get_elements(self, "Ff").click()
        Selenium.esperar_elemento(self, "search")
        Selenium.scroll_to(self, "search")
        Selenium.get_elements(self, "search").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self, "menu").click()
        Selenium.esperar_elemento(self, "Colec")
        Selenium.get_elements(self, "Colec").click()
        Selenium.capturar_pantalla(self)

    def tearDown(self):
        Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
