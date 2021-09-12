# Created by javit at 18/07/2021
Feature: #Comrobar paso1

  @Paso1
  Scenario: Comprobar paso 1 en Español
    Given Abrir en Chrome la aplicaciónhttps://booking.barcelo.com/?adult=2&arrive=2021-09-16&chain=24876&child=2&childages=2|5&configcode=GROSS&currency=EUR&currency_def=EUR&depart=2021-09-19&filter=EUR&hotel=7390&level=hotel&locale=es-ES&market=ES&rooms=1&segment=BED%20AND%20BREAKFAST&themecode=initialTheme&usc=ES&usercurrency=EUR
    And Cargo el DOM de la App: iberostarpaso1
    Then Espero el elemento: Cockies
    And Hago clic en Cockies
    Then Hago scroll hacia el elemento: name
    And En el campo name tecleo Xavi
    And Tomar Captura: Iberopaso1
    Then cierro la app