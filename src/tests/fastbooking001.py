# -*- coding: utf-8 -*-

from src.functions.Functions import Functions as Selenium
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class fastbooking(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self, "ibero")

    def test_001(self):
        Selenium.page_has_loaded(self)
        Selenium.get_elements(self, "Cockies").click()
        Selenium.scroll_to(self, "Escribe")
        Selenium.esperar_elemento(self, "Escribe")
        Selenium.get_elements(self, "Escribe").click()
        Selenium.get_elements(self, "write").send_keys("Iberostar Pinos Park")
        Selenium.get_elements(self, "write").send_keys(Keys.ENTER)
        Selenium.esperar_elemento(self, "fechas")
        Selenium.get_elements(self, "fechas").click()
        Selenium.get_json_file(self, "ibero")
        Selenium.get_elements(self, "I").click()
        Selenium.get_elements(self, "F").click()
        Selenium.scroll_to(self, "consultahotel")
        Selenium.esperar_elemento(self, "consultahotel")
        Selenium.esperar(self, 1)
        Selenium.scroll_to(self, "Reser")
        Selenium.get_elements(self, "Reser").click()
        self.driver.back()
        Selenium.capturar_pantalla(self)


    def tearDown(self):
        Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
