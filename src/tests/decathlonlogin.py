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
        self.driver = webdriver.Chrome(executable_path= "C:\pycharm\src\drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.decathlon.es/es/create")

    def test_102(self):
        Selenium.page_has_loaded(self)
        Selenium.get_json_file(self, "decath")
        Selenium.scroll_to(self, "mail")
        Selenium.get_elements(self, "mail").send_keys("jmail@mail.com")
        Selenium.get_elements(self, "mail").send_keys(Keys.ENTER)
        Selenium.esperar(self, 2)
        Selenium.get_elements(self, "hombre").click()
        Selenium.esperar_elemento(self, "nombre")
        Selenium.get_elements(self, "nombre").send_keys("Javi")
        Selenium.get_elements(self, "apellido").send_keys("Vazquez")
        Selenium.get_elements(self, "apellido1").send_keys("Taboada")
        Selenium.esperar(self, 2)
        Selenium.scroll_to(self, "dni")
        Selenium.get_elements(self, "dni").send_keys("14612399Q")
        Selenium.scroll_to(self, "contra")
        Selenium.get_elements(self, "contra").send_keys("Mateo2021")
        Selenium.get_elements(self, "si").click()
        Selenium.check_element(self, "aceptar")
        Selenium.capturar_pantalla(self)

    def tearDown(self):
        Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
