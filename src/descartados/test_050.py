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
@allure.feature(u'chequeo elementos CRM')
@allure.story(u'050: Mouse over CRM landing principal')
@allure.testcase(u"Caso de Prueba 050", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""ELEMENTOS:</br>
MOUSE: </br>
 </br></br>""")

class Elementos1(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Ibero'):
           Selenium.abrir_navegador(self)

    def test_050(self):
        with allure.step(u'PASO 2: mouseover'):
            Selenium.page_has_loaded(self)
            Selenium.get_json_file(self, "elements")
            Selenium.get_elements(self, "SobreNosotrosHeader").click()
            Selenium.switch_to_windows_name(self, "Principal")
            Selenium.esperar(self, 1)
            Selenium.get_elements(self, "oferta")
            Selenium.scroll_to(self, "oferta")
            Selenium.mouse_over(self, "oferta")
            Selenium.scroll_to(self, "hoteles")
            Selenium.mouse_over(self, "hoteles")
            Selenium.esperar_elemento(self, "hoteleuropa")
            Selenium.get_elements(self, "hoteleuropa").click()
            Selenium.mouse_over(self, "Gestionarre")
            Selenium.mouse_over(self, "mibusqueda")
            Selenium.scroll_to(self, "entornoseguro")
            Selenium.mouse_over(self, "entornoseguro")
            Selenium.esperar_elemento(self, "higiene")
            Selenium.mouse_over(self, "higiene")
            Selenium.mouse_over(self, "social")
            Selenium.mouse_over(self, "entornoseguro")
            Selenium.scroll_to(self, "Destacado2")
            Selenium.mouse_over(self, "Destacado2").click()
            Selenium.capturar_pantalla(self)

    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la app'):
            Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()