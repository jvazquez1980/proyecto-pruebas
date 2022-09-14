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
@allure.description(u"""Intentamos el login:</br>
DEror en el login </br>
 </br></br>""")

class loginexxo(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Exotica'):
            Selenium.abrir_navegador(self)
            Selenium.get_json_file(self, "exxotica")


    def test_001(self):
        with allure.step(u'FB'):
            Selenium.get_elements(self, "cookies").click()
            Selenium.get_elements(self, "verviaje").click()
            Selenium.get_elements(self, "CTA2").click()
            Selenium.get_elements(self, "cerrarmodal").click()
            Selenium.get_entity(self, "text")
            Selenium.get_elements(self, "text").click()
            Selenium.get_elements(self, "verprecios").click()
            Selenium.get_elements(self, "ElegirFecha").click()

    def test_002(self):
        with allure.step(u'FB'):
            Selenium.get_elements(self, "cookies").click()
            Selenium.double_clic(self, "Selectordestino")
            Selenium.get_elements(self, "Destino").click()
            Selenium.get_select_elements(self, "Selectordestino").select_by_visible_text("Madrid")



    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la app'):
            Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
