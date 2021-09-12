# Created by javit at 18/07/2021
Feature:Reserva en Tui hoteles

  @Tuibusqueda
  Scenario: Realizar busqueda
    Given Abrir en Chrome la aplicación https://es.tui.com/
    And Cargo el DOM de la App: tui
    Then Hago clic en Cok
    Then En el campo texto tecleo Mallorca
    And Hago clic en search
    Then Pongo el cursor sobre elemento: Reservapaso1
    And Tomar Captura: Testtui1
    Then cierro la app

  @Tuibusqueda
  Scenario: Realizar busqueda
    Given Abrir en Chrome la aplicación https://es.tui.com/
    And Cargo el DOM de la App: tui
    Then Hago clic en Cok
    Then Hago scroll hacia el elemento: laponia
    Then Hago clic en laponia
    And Tomar Captura: Testtui1
    Then cierro la app