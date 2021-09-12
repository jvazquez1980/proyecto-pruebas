# Created by javit at 21/10/2020
Feature: Pruebas2

  @Element
  Scenario: Desplegable
    Given Abrir la aplicacion
    And Cargo el DOM de la App: pruebbas2
    And  Hago clic en d
    And En el combobox drop selecciono 1
    And En el combobox drop selecciono 2
    And Tomar Captura: Drop
    Then cierro la app