# -*- coding: utf-8 -*-


from src.functions.Functions import Functions as Selenium
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import allure
@allure.feature(u'Exotica')
@allure.story(u'020: Intento de login')
@allure.testcase(u"Caso de Prueba 020", u'https://www.exoticca.com/es')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Fb</br>
DEror en el login </br>
 </br></br>""")

class loginexxo(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Exotica'):
            Selenium.abrir_navegador(self)
            Selenium.get_json_file(self, "exxoticareserva")


    def test_001(self):
        with allure.step(u'FB'):

            Selenium.get_elements(self, "cookies").click()
            Selenium.get_elements(self, "Selectorpais").click()
            Selenium.get_elements(self, "GBP").click()
            Selenium.get_elements(self, "FBOOKING").click()
            Selenium.send_key_text(self, "FBOOKING", "hun")
            Selenium.get_elements(self, "IDdeFB3").click()

    def test_002(self):
        with allure.step(u'Resevapaso1'):
            Selenium.get_elements(self, "cookies").click()
            Selenium.get_elements(self, "mail").click()
            Selenium.send_key_text(self, "FBOOKING", "mail@prueba.com")




    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la app'):
            Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
