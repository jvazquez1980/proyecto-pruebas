# -*- coding: utf-8 -*-
from functions.Functions import Functions as Selenium
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import allure

@allure.feature(u'elementosllamar')
@allure.story(u'051: Llamar y SobreNosotrosHeader Nosotros links')
@allure.testcase(u"Caso de Prueba 051", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Pedir que nos llamen:</br>
SobreNosotrosHeader nosotros </br>
 </br></br>""")

class tellamamos(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Ibero'):
            Selenium.abrir_navegador(self)

    def test_051(self):
        with allure.step(u'PASO 2: llamame'):
            Selenium.page_has_loaded(self)
            Selenium.get_json_file(self, "elements")
            Selenium.get_elements(self, "SobreNosotrosHeader").click()
            Selenium.get_elements(self, "SobreNosotrosHeader").click()
            Selenium.switch_to_windows_name(self, "Principal")
            Selenium.get_elements(self, "llamar").click()
            Selenium.get_elements(self, "text","Te llamamos gratisassert text ahora").click()
            Selenium.scroll_to(self, "formulario")
            self.driver.back()
            Selenium.capturar_pantalla(self)

    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la app'):
            Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()