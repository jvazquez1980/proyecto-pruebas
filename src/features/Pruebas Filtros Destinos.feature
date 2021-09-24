# Created by javit at 24/09/2021
Feature: #Comprobar LANDINGS ofertas automaticas filtros en otros idiomas

  @Landingsofertas
  Scenario: Comprobar todos los Filtros de destinos en Ingles
    Given Abrir en Chrome la aplicación https://www.iberostar.com/en/offers/flash-offers-hotels/
    And Cargo el DOM de la App: ofertasflash
    Then Espero el elemento: Aceotarcoo
    And Hago clic en Aceotarcoo
    And Hago scroll hacia el elemento: Montenegro
    And Hago clic en portugal
    And Hago clic en brasil
    And Hago clic en Tunez
    Then Hago clic en marruecos
    Then Hago clic en jamaica
    Then Hago clic en mexico
    Then Hago clic en Espana
    And  Hago clic en RD
    And Tomar Captura: destinos
    Then cierro la app

  @Landingsofertas
  Scenario: Comprobar todos los Filtros de destinos en DE
    Given Abrir en Chrome la aplicación https://www.iberostar.com/de/angebote/flash-angebote-hotels/
    And Cargo el DOM de la App: ofertasflash
    Then Espero el elemento: Aceotarcoo
    And Hago clic en Aceotarcoo
    And Hago scroll hacia el elemento: Montenegro
    And Hago clic en portugal
    And Hago clic en brasil
    And Hago clic en Tunez
    Then Hago clic en marruecos
    Then Hago clic en jamaica
    Then Hago clic en mexico
    Then Hago clic en Espana
    And  Hago clic en RD
    And Tomar Captura: destinos
    Then cierro la app

  @Landingsofertas
  Scenario: Comprobar CTA oferta
    Given Abrir en Chrome la aplicación https://www.iberostar.com/de/angebote/flash-angebote-hotels/
    And Cargo el DOM de la App: ofertasflash
    Then Espero el elemento: Aceotarcoo
    And Hago clic en Aceotarcoo
    And Hago scroll hacia el elemento: brasil
    Then Espero el elemento: reservar
    Then Hago clic en reservar
    And Tomar Captura: CTA oferta
    Then cierro la app