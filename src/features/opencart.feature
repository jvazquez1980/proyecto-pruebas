# Created by javit at 20/10/2020
Feature: compramac

  @Mac
  Scenario: Comprar Mac
    Given Abrir la aplicacion
    And Cargo el DOM de la App: cart
    And Hago clic en iphone
    Then Hago clic en anadir
    And Hago clic en inicio
    And Hago clic en mac
    Then Espero 3 segundos
    And Hago clic en mac4
    Then Envio escape: mac4
    And Hago clic en carrito
    Then Hago clic en vercarrito
    And Hago clic en inicio
    And Tomar Captura: TestCart<string>
    Then cierro la app