# Created by Javi at 10/08/2020
Feature:Comprobar elementos de la landing principal CMS

  @ElementosCMS
  Scenario: Seleccionar CambiarMoneda
    Given Abrir la aplicacion
    And Cargo el DOM de la App: elements
    And Hago clic en Cockies
    And En el combobox CambiarMoneda selecciono GBP
    And Hago clic en cambiarCambiarMoneda
    And En el combobox CambiarMoneda selecciono USD
    And En el combobox CambiarMoneda selecciono CAD
    And En el combobox CambiarMoneda selecciono CLP
    And En el combobox CambiarMoneda selecciono BRL
    And En el combobox CambiarMoneda selecciono ARS
    And En el combobox CambiarMoneda selecciono MXN
    And En el combobox CambiarMoneda selecciono RUB
    And En el combobox CambiarMoneda selecciono DEF
    And En el combobox CambiarMoneda selecciono CHF
    And Tomar Captura: Test051
    Then cierro la app

  @ElementosCMS
  Scenario: Seleccionar Idioma
    Given Abrir la aplicacion
    And Cargo el DOM de la App: elements
    And Hago clic en Cockies
    And En el combobox idioma selecciono en
    And En el combobox idioma selecciono de
    And En el combobox idioma selecciono fr
    And En el combobox idioma selecciono it
    And En el combobox idioma selecciono pt
    And En el combobox idioma selecciono ru
    And En el combobox CambiarMoneda selecciono mx
    And En el combobox CambiarMoneda selecciono he
    And En el combobox CambiarMoneda selecciono ar
    And En el combobox CambiarMoneda selecciono zh
    And Tomar Captura: Test052
    Then cierro la app

  @ElementosCMS
  Scenario: Comprobar modulos del CMS
    Given Abrir la aplicacion
    And Cargo el DOM de la App: elements
    And Hago clic en Cockies
    Then Hago scroll hacia el elemento: oferta
    And Desplazo Mouse SobreNosotrosHeader: oferta
    And Desplazo Mouse SobreNosotrosHeader: hoteles
    And Desplazo Mouse SobreNosotrosHeader: Gestionarre
    Then Hago scroll hacia el elemento: entornoseguro
    And Desplazo Mouse SobreNosotrosHeader: entornoseguro
    And Tomar Captura: Test053
    Then cierro la app