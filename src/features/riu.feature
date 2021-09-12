# Created by javit at 13/10/2020
Feature:Reserva en RIU hoteles

  @Riureserva
  Scenario: Introducir fechas y buscar reserva
    Given Inicilizo la app en la URL https://www.riu.com/es/
    And Cargo el DOM de la App: riu
    Then Yo hago clic cockies con el texto Aceptar Cookies
    Then En el campo texto tecleo Mallorca
    And Hago clic en calendario
    And Hago clic en buscar
    Then Espero 3 segundos
    And Hago scroll hacia el elemento: seleccionar
    Then Hago clic en seleccionar
    And Tomar Captura: Testriu1
    Then cierro la app