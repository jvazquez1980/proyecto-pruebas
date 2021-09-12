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
@allure.feature(u'CambiarMonedayidioma')
@allure.story(u'002: Cambiar CambiarMoneda e idioma')
@allure.testcase(u"Caso de Prueba 052", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Elegir CambiarMoneda:</br>
Elegir CambiarMoneda: </br>
 </br></br>""")


class CambiarMoneda(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Ibero'):
            Selenium.abrir_navegador(self)

    def test_052(self):
        with allure.step(u'PASO 2: probar valores'):
            Selenium.page_has_loaded(self)
            Selenium.get_json_file(self, "elements")
            Selenium.get_elements(self, "Cockies").click()
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("USD")
            Selenium.get_elements(self, "cambiarCambiarMoneda").click()
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("GBP")
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("CAD")
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("CHF")
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("CLP")
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("BRL")
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("ARS")
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("MXN")
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("RUB")
            Selenium.get_select_elements(self, "CambiarMoneda").select_by_value("DEF")
            Selenium.esperar(self, 2)
            Selenium.get_select_elements(self, "idioma").select_by_value("en")
            Selenium.get_select_elements(self, "idioma").select_by_value("de")
            Selenium.get_select_elements(self, "idioma").select_by_value("fr")
            Selenium.get_select_elements(self, "idioma").select_by_value("it")
            Selenium.get_select_elements(self, "idioma").select_by_value("pt")
            Selenium.get_select_elements(self, "idioma").select_by_value("ru")
            Selenium.get_select_elements(self, "idioma").select_by_value("mx")
            Selenium.get_select_elements(self, "idioma").select_by_value("he")
            Selenium.get_select_elements(self, "idioma").select_by_value("ar")
            Selenium.get_select_elements(self, "idioma").select_by_value("zh")
            Selenium.esperar(self, 2)
            Selenium.capturar_pantalla(self)

    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la app'):
            Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
