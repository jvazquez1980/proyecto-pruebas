# Created by javit at 21/10/2020
Feature:reserva en hotel

  @Riureserva
  Scenario: Compruebo elementos de la landing principal
    Given Inicilizo la app en la URL https://www.iberostar.com/es/
    And Cargo el DOM de la App: accord
    And En el campo texto hago clear y escribo Mallorca
    And Hago clic en opcion1
    And Hago clic en checkin
    Then Hago ENTER en el elemento: fechai
    And Hago clic en checkin2
    Then Hago ENTER en el elemento: fechaf
    And Hago clic en buscar
    Then Espero 3 segundos
    Then Hago clic en seleccionar
    And Tomar Captura: Accord
    Then cierro la app