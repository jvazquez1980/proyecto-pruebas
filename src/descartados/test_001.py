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
@allure.story(u'001: Reserva desde la web inicio')
@allure.testcase(u"Caso de Prueba 001", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(u"""Se requiere visitar el sitio iberostar:</br>
Deseamos introducir datos de busqueda </br>
 </br></br>""")

class reservapaso1(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Ibero'):
            Selenium.abrir_navegador(self)
            Selenium.get_json_file(self, "ibero")

    def test_001(self):
        with allure.step(u'PASO 2: valores de la reserva'):
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
            Selenium.esperar(self, 1)
            Selenium.scroll_to(self, "Reser")
            Selenium.get_elements(self, "Reser").click()
            self.driver.back()
            Selenium.captura(self, "reserva")


    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la app'):
            Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
