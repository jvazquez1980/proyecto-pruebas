# Created by javit at 28/07/21
Feature: Pruebas qa varias

  @Pruebaautomatic
  Scenario: Dropdown1
    Given Inicilizo la app en la URL http://testautomationpractice.blogspot.com/
    And Cargo el DOM de la App: pruebaautomatic3
    And Hago clic en Cookies
    Then Hago scroll hacia el elemento: date
    And En el combobox despegable selecciono 1
    And En el combobox despegable selecciono 2
    And En el combobox despegable selecciono 3
    And En el combobox despegable selecciono 4
    Then En el combobox despegable selecciono 2
    And Tomar Captura: Dropdown1
    Then cierro la app

  @Pruebaautomatic
  Scenario: Dropdown2
    Given Inicilizo la app en la URL http://testautomationpractice.blogspot.com/
    And Cargo el DOM de la App: pruebaautomatic3
    And Hago clic en Cookies
    Then Hago scroll hacia el elemento: Animal
    And En el dropdown Animal selecciono Cat
    And En el dropdown Animal selecciono Big Baby Cat
    And En el dropdown Animal selecciono Baby Cat
    And En el dropdown Animal selecciono Cat
    And Tomar Captura: Dropdown2
    Then cierro la app

  @Pruebaautomatic
  Scenario: Drag and drop
    Given Inicilizo la app en la URL http://testautomationpractice.blogspot.com/
    And Cargo el DOM de la App: pruebaautomatic3
    And Hago clic en Cookies
    Then Arrastro elemento Source sobre Target
    And Tomar Captura: Dropdown2
    Then cierro la app

  @Pruebaautomatic
  Scenario: Check box
    Given Inicilizo la app en la URL http://testautomationpractice.blogspot.com/
    And Esperar que finalice la carga
    And Cargo el DOM de la App: pruebaautomatic3
    And Hago clic en Cookies
    Then Hago scroll hacia el elemento: Animal
    Then Hago clic en Checkbox0
    And Tomar Captura: Checkbox0
    Then cierro la app

  @Pruebaautomatic
  Scenario: Check box otra prueba
    Given Inicilizo la app en la URL https://the-internet.herokuapp.com
    And Esperar que finalice la carga
    And Cargo el DOM de la App: pruebaautomatic3
    And Hago clic en Checknuevo
    And Hago clic en Checkbox1
    And Hago clic en Checkbox2
    Then Hago clic en Checkbox1
    Then Hago clic en Checkbox2
    And Hago clic en Checkbox2
    Then Espero 1 segundos
    And Tomar Captura: Checbok
    Then cierro la app


  @Pruebaautomatic
  Scenario: Drag and drop the internet
    Given Inicilizo la app en la URL https://the-internet.herokuapp.com
    And Cargo el DOM de la App: pruebatomatic3
    And Hago clic en dragdrop
    Then Arrastro elemento source2 sobre target2
    And Tomar Captura: Dropdowntheinternet
    Then cierro la app