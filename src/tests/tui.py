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

        # INGRESO A LA APP
        self.driver.get("https://es.tui.com/")

    def test_102(self):
        Selenium.page_has_loaded(self)
        Selenium.get_json_file(self, "tui")
        Selenium.get_elements(self, "Cok").click()
        Selenium.esperar_elemento(self, "log")
        Selenium.get_elements(self, "log").click()
        Selenium.get_elements(self, "name").send_keys("mallorca@gmail.com")
        Selenium.get_elements(self, "pass").send_keys("mallorca")
        Selenium.get_elements(self, "accede").click()
        Selenium.esperar(self,3)
        Selenium.capturar_pantalla(self)

    def tearDown(self):
        Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
