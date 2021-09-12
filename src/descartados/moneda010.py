# -*- coding: utf-8 -*-


from functions.Functions import Functions as Selenium
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
horaGlobal = time.strftime("%H%M%S")

class selectidioma(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_010(self):
        Selenium.page_has_loaded(self)
        Selenium.get_json_file(self, "elements")
        Selenium.get_entity(self, "CambiarMoneda").click()
        Selenium.esperar(self, 2)


        title = "Test_102"
        self.driver.get_screenshot_as_file(f"../data/capturas/{title}-{horaGlobal}.png")

    def tearDown(self):
        Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
