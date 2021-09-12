# Created by javit at 01/08/2021
Feature: #Pruebas de qa tjhe internet

  @Pruebatheinternet
  Scenario: Key
    Given Inicilizo la app en la URL https://the-internet.herokuapp.com
    And Cargo el DOM de la App: theinternet
    And Hago clic en key
    And Hago clic en target
    Then Hago ENTER en el elemento: target
    And Hago clic en target
    Then Hago TAB en el elemento: target
    And Hago clic en target
    Then Hago TAB en el elemento: target
    And Retroceder
    Then Espero 2 segundos
    Then cierro la app

  @Pruebatheinternet
  Scenario: Key
    Given Inicilizo la app en la URL https://the-internet.herokuapp.com
    And Cargo el DOM de la App: theinternet
    And Hago clic en key
    And Hago clic en target
    Then Hago ENTER en el elemento: target
    And Hago clic en target
    Then Hago TAB en el elemento: target
    And Hago clic en target
    Then Hago TAB en el elemento: target
    And Retroceder
    Then Espero 2 segundos
    Then cierro la app
    
  @Pruebatheinternet
  Scenario: Controles dinamicos
    Given Inicilizo la app en la URL https://the-internet.herokuapp.com
    And Cargo el DOM de la App: theinternet
    And Hago clic en Dinamic
    And Hago clic en Remove
    Then Espero el elemento: Checkbox
    And Hago clic en Checkbox
    And Hago clic en Remove
    Then Espero el elemento: Enable
    And Hago clic en Enable
    And Espero el elemento: Escribir
    Then En el campo Escribir tecleo Prueba
    And Hago clic en Disable
    Then Espero el elemento: Enable
    And Hago clic en Enable
    And Espero el elemento: Escribir
    Then En el campo Escribir tecleo Valida
    Then Espero 1 segundos
    Then cierro la app
    
  @Pruebatheinternet
  Scenario: Cargar foto con botón seleccionar
    Given Inicilizo la app en la URL https://the-internet.herokuapp.com
    And Cargo el DOM de la App: theinternet
    And Hago clic en File
    And Cargo foto subirarchivo en C:\Users\javit\Documents\ShareX\Screenshots\2021-08\prueba.png
    And Hago clic en Subir
    And Espero 2 segundos
    Then Retroceder
    And Avanzar
    Then Retroceder
    Then Retroceder
    Then Tomar Captura: SubirArchivo
    Then cierro la app

  @Pruebatheinternet
  Scenario: menu despegable
    Given Inicilizo la app en la URL https://the-internet.herokuapp.com/jqueryui/menu
    And Cargo el DOM de la App: theinternet
    And Pongo el cursor sobre elemento: Enable
    And Pongo el cursor sobre elemento: descargas
    And Pongo el cursor sobre elemento: PDF
    Then Hago clic en PDF
    And Espero 2 segundos
    Then Retroceder
    Then Tomar Captura: menu despegable
    Then cierro la app

  @Pruebatheinternet
  Scenario: Slider
    Given Inicilizo la app en la URL https://the-internet.herokuapp.com/horizontal_slider
    And Cargo el DOM de la App: theinternet
    Then Arrastro elemento Valor1source sobre Valor2target
    Then Tomar Captura: Slider
    Then cierro la app

  @PruebaSeleniumeasy
  Scenario: Doble Clic
    Given Inicilizo la app en la URL https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html
    And Cargo el DOM de la App: theinternet
    Then Hago double clic en el elemento: pruebadobleclic
    And Espero 2 segundos
    Then Tomar Captura: Slider
    Then cierro la app