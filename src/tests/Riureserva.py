# -*- coding: utf-8 -*-


from functions.Functions import Functions as Selenium
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class test_300(Selenium, unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.riu.com/es/home.jsp")

    def test_300(self):
        Selenium.page_has_loaded(self)
        Selenium.get_json_file(self, "riu")
        Selenium.get_elements(self,"cockies").click()
        Selenium.get_elements(self, "texto").send_keys("Mallorca")
        Selenium.get_elements(self, "calendario").click()
        Selenium.get_elements(self, "buscar").click()
        Selenium.esperar(self, 5)
        Selenium.scroll_to(self, "seleccionar")
        Selenium.get_elements(self, "seleccionar")
        Selenium.capturar_pantalla(self)

    def tearDown(self):
        Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
