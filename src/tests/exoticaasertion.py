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
@allure.testcase(u"Caso de Prueba ", u'https://www.exoticca.com/es')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Intentamos el login:</br>
DEror en el login </br>
 </br></br>""")

class loginexxo(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'Home: Asercion de login'):
            Selenium.abrir_navegador(self)
            Selenium.get_json_file(self, "exxotica")


    def test_001(self):
        with allure.step(u'FB'):
            Selenium.get_elements(self, "cookies").click()
            Selenium.get_elements(self, "Acceder").click()
            Selenium.get_elements(self, "Accederclick").click()
            Selenium.get_elements(self, "Accederboton").click()
            Selenium.get_entity(self, "Assertmail")
            Selenium.assert_text(self, "Assertmail", "Campo obligatorio")
            Selenium.send_key_text(self, "Campomail", "mail@prueba.com")
            Selenium.send_key_text(self, "Campopasswrod", "Pruebaerror001")
            Selenium.scroll_to(self, "Accederboton")
            Selenium.get_elements(self, "Accederboton").click()
            Selenium.get_elements(self, "cerrarmodal").click()
            Selenium.check_element(self, "Assertionmailincorrecto")



    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la app'):
            Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
