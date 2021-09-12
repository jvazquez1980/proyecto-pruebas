# Created by javit at 29/07/2021
Feature: Bay shower pruebas
  # Enter feature description here

   @baby
  Scenario: Comprar producto baby shower con error mail
    Given Inicilizo la app en la URL https://www.babyshower.es/es/
    And Cargo el DOM de la App: baby
    And Hago clic en Cookies
    Then Hago clic en casa
    Then Hago scroll hacia el elemento: producto2
    Then Espero el elemento: producto1
    And Hago clic en producto1
    And Hago clic en cesta
    Then En el campo paso1mail tecleo javitxuelo@gmail.com
    Then Hago clic en continuar
    Then Espero el elemento: contrasena
    Then En el campo contrasena tecleo Prueba400
    And En el campo nombre tecleo Pruebafallida
    And En el campo nombre tecleo apellidos
    Then Hago clic en checkboxacepto
    Then Hago clic en continuar
    And Espero 2 segundos 
    And Tomar Captura: baby1
    Then cierro la app

   @baby
   Scenario: Comprar producto baby shower sin error mail
    Given Inicilizo la app en la URL https://www.babyshower.es/es/
    And Cargo el DOM de la App: baby
    And Hago clic en Cookies
    Then Hago clic en casa
    Then Hago scroll hacia el elemento: producto2
    Then Espero el elemento: producto1
    And Hago clic en producto1
    And Hago clic en cesta
    Then En el campo paso1mail tecleo mailo@gmail.com
    Then Hago clic en continuar
    Then Espero el elemento: contrasena
    Then En el campo contrasena tecleo Prueba400
    And En el campo nombre tecleo Prueba
    And En el campo apellidos tecleo Valida
    Then Hago clic en checkboxacepto
    Then Hago clic en continuar
    And Espero 2 segundos
    And Tomar Captura: baby1
    Then cierro la app