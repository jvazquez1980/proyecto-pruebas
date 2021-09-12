# -*- coding: utf-8 -*-
from selenium import webdriver
from functions.Functions import Functions as Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re



class CambiarMoneda(Selenium, unittest.TestCase):
    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_100(self):
        driver = self.driver
        driver.find_element_by_name("currency").click()
        Select(driver.find_element_by_name("currency")).select_by_visible_text("USD")
        driver.find_element_by_link_text("Cambiar CambiarMoneda").click()
        Selenium.esperar(self, 1)
        driver.find_element_by_name("currency").click()
        Select(driver.find_element_by_name("currency")).select_by_visible_text("CLP")
        Selenium.esperar(self, 1)
        driver.find_element_by_name("currency").click()
        Select(driver.find_element_by_name("currency")).select_by_visible_text("EUR")
        Selenium.esperar(self, 1)
        driver.find_element_by_name("currency").click()
        Select(driver.find_element_by_name("currency")).select_by_visible_text("GBP")
        Selenium.esperar(self, 1)
        driver.find_element_by_name("currency").click()
        Select(driver.find_element_by_name("currency")).select_by_visible_text("RUB")
        Selenium.esperar(self, 1)
        driver.find_element_by_name("currency").click()
        Select(driver.find_element_by_name("currency")).select_by_visible_text("MXN")
        Selenium.esperar(self, 1)
        driver.find_element_by_name("currency").click()
        Select(driver.find_element_by_name("currency")).select_by_visible_text("ARS")
        Selenium.esperar(self, 1)
        driver.find_element_by_name("currency").click()
        Select(driver.find_element_by_name("currency")).select_by_visible_text("CAD")
        Selenium.esperar(self, 1)
        Selenium.capturar_pantalla(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
