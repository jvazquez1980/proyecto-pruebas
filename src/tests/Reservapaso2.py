# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import allure
@allure.feature(u'Reserva')
@allure.story(u'002: Elegir hotel y regimen')
@allure.testcase(u"Caso de Prueba 001", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(u"""Elegir regimen:</br>
Continuar </br>
 </br></br>""")

class Reservapaso2(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Ibero'):
            Selenium.abrir_navegador(self)

    def test_001(self):
        with allure.step(u'PASO 2: valores de la reserva'):
            Selenium.page_has_loaded(self)
            Selenium.get_json_file(self, "ibero")
            Selenium.get_elements(self, "Cockies").click()
            Selenium.get_elements(self, "nodificar").click()
            Selenium.get_elements(self, "continuar").click()
            Selenium.scroll_to(self, "regimen")
            Selenium.get_elements(self, "regimen").click()
            Selenium.esperar_elemento(self, "tarifa")
            Selenium.scroll_to(self, "tarifa")
            Selenium.get_elements(self, "tarifa").click()
            Selenium.get_elements(self, "continuar").click()
            Selenium.capturar_pantalla(self)


    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la app'):
            Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
