# -*- coding: utf-8 -*-
from behave import *
import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from behave import *
from selenium.webdriver.common.keys import Keys
from functions.Functions import Functions as Selenium
from functions.Inicializar import Inicializar

class StepsDefinitions():
    use_step_matcher("re")

    @given("Abrir la aplicacion")
    def abrir_navegador(self):
        Selenium.abrir_navegador(self)
        Selenium.page_has_loaded(self)

    @given("Abrir en Chrome la aplicación(.*)")
    def abrir_Chrome(self, URL):
        Selenium.abrir_CHROME(self, URL=URL)

    @given("Inicilizo la app en la URL (.*)")
    def step_impl(self, URL):
        Selenium.abrir_navegador(self, URL=URL)

    @step("Abro nueva ventana: (.*)")
    def step_impl(self, URL):
        Selenium.new_window((self, URL))

    @given("Abro la app con el navegador (.*)")
    def step_impl(self, navegador):
        Selenium.abrir_navegador(self, navegador=navegador)

    @then("cierro la app")
    def step_impl(self):
        Selenium.tearDown(self)

    @step("Cargo el DOM de la App: (.*)")
    def step_impl(self, DOM):
       Selenium.get_json_file(self, DOM)


    @step("En el campo (.*) hago clear y escribo (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.send_key_text(self, locator, text)

    @step("En el campo (.*) tecleo (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.get_elements(self, locator).send_keys(text)

    @step("Yo hago clic (.*) con el texto (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.get_elements(self, locator, text).click()

    @step("Capturo pantalla: (.*)")
    def step_impl(self, descripcion):
        Selenium.captura(self, descripcion)

    @step("Envio escape")
    def step_impl(self, descripcion):
        self.driver.send_keys(Keys.ESCAPE)

    @step("Espero el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.esperar_elemento(self, locator)

    @step("Hago Clear en el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.get_elements(self, locator).send_keys(Keys.CLEAR)

    @step("Hago TAB en el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.get_elements(self, locator).send_keys(Keys.TAB)

    @step("Hago Cancel en el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.get_elements(self, locator).send_keys(Keys.CANCEL)

    @step("Hago Clicderecho en el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.context_clic(self, locator)

    @step("Hago double clic en el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.double_clic(self, locator)

    @step("Hago ENTER en el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.get_elements(self, locator).send_keys(Keys.ENTER)

    @step("Hago BACK en el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.get_elements(self, locator).send_keys(Keys.BACKSPACE)

    @step("Retroceder")
    def step_impl(self,):
        self.driver.execute_script("window.history.go(-1)")

    @step("Avanzar")
    def step_impl(self, ):
        self.driver.execute_script("window.history.go(+1)")

    @step("Tomar Captura: (.*)")
    def step_impl(self, Captura):
        Selenium.capturar_pantalla(self, Captura)

    @step("En el dropdown (.*) selecciono (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.select_by_text(self, locator, text)

    @step("En el combobox (.*) selecciono (.*)")
    def step_impl(self, locator, value):
        Selenium.esperar_elemento(self, locator)
        Selenium.get_select_elements(self, locator).select_by_value(value)

    @step("Me desplazo al frame: (.*)")
    def step_impl(self, frame):
        Selenium.switch_to_iframe(self, frame)

    @step("Vuelvo al frame padre")
    def step_impl(self):
         Selenium.switch_to_parentFrame(self)

    @step("Me desplazo a la ventana: (.*)")
    def step_impl(self, ventana):
        Selenium.switch_to_windows_name(self, ventana)

    @step("Hago clic en (.*)")
    def step_impl(self, locator):
        Selenium.get_elements(self,locator).click()

    @step("Cliqueo en Texto: (.*)")
    def step_impl(self, Text):
        Selenium.get_elements(self, "text", MyTextElement=Text).click()

    @step("Hago scroll hacia el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.scroll_to(self, locator)

    @step("Pongo el cursor sobre elemento: (.*)")
    def step_impl(self, locator):
        Selenium.mouse_over(self, locator)

    @step("Doble clic sobre elemento: (.*)")
    def step_impl(self, locator):
        Selenium.double_clic(self, locator)

    @step("Esperar que finalice la carga")
    def step_impl(self):
        Selenium.page_has_loaded(self)

    @step("Espero (.*) segundos")
    def step_impl(self, segundos):
        segundos = int(segundos)
        Selenium.esperar(self, segundos)

    @step("Aceptar ventana emergente")
    def step_impl(self):
        Selenium.alert_windows(self,accept="accept")

    @step("ESCAPE")
    def step_impl(self):
        self.driver.send_keys(Keys.ESCAPE)

    @step("Enter")
    def step_impl(self):
        Selenium.send_especific_keys(Keys.ENTER)

    @step("Comprobar elemento: (.*)")
    def step_impl(self, locator):
        Selenium.check_element(self, locator)

    @step("Assertion de texto: (.*)")
    def step_impl(self, locator, TEXTO):
        Selenium.assert_text(self, locator, TEXTO)

    @step("Arrastro elemento (.*) sobre (.*)")
    def step_impls(self, source1, target1):
        Selenium.drag_and_drop(self, source1, target1)

    @step("Cargo foto (.*) en (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.get_elements(self, locator).send_keys(text)







