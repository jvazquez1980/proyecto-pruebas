# Created by javit at 18/07/2021
Feature: #Comprobar LANDINGS ofertas automaticas filtros

  @Landingsofertas
  Scenario: Comprbar todos los Filtros de fechas
    Given Abrir en Chrome la aplicación https://www.iberostar.com/ofertas/ofertas-flash-hoteles/
    And Cargo el DOM de la App: ofertasflash
    Then Espero el elemento: Aceotarcoo
    And Hago clic en Aceotarcoo
    And Hago scroll hacia el elemento: Mes2
    And Hago clic en Mes3
    And Hago clic en Mes4
    And Tomar Captura: fechas


  @Landingsofertas
  Scenario: Comprobar todos los Filtros de destinos
    Given Abrir en Chrome la aplicación https://www.iberostar.com/ofertas/ofertas-flash-hoteles/
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
  Scenario: Comprobar Filtros acumulativos Fechas+Destino
    Given Abrir en Chrome la aplicación https://www.iberostar.com/ofertas/ofertas-flash-hoteles/
    And Cargo el DOM de la App: ofertasflash
    Then Espero el elemento: Aceotarcoo
    And Hago clic en Aceotarcoo
    And Hago scroll hacia el elemento: Mes2
 And Hago scroll hacia el elemento: Mes2
    And Hago clic en Mes3
    And Hago clic en Mes4
    Then Espero 1 segundos
    And Hago scroll hacia el elemento: Montenegro
    And Hago clic en Montenegro
    And Hago clic en portugal
    And Hago clic en brasil
    Then Hago clic en Tunez
    Then Hago clic en jamaica
    Then Hago clic en mexico
    Then Hago clic en Espana
    And  Hago clic en RD
    And Tomar Captura: Fechas+Destino
    Then cierro la app

  @Landingsofertas
  Scenario: Comprobar Filtros de Fechas+ Filtros generales
    Given Abrir en Chrome la aplicación https://www.iberostar.com/ofertas/ofertas-flash-hoteles/
    And Cargo el DOM de la App: ofertasflash
    Then Espero el elemento: Aceotarcoo
    And Hago clic en Aceotarcoo
    And Hago scroll hacia el elemento: portugal
    Then Hago clic en Filtrosgenerales
    And Hago clic en 4estrellas
    And Tomar Captura: Filtros
    Then cierro la app


  @Landingsofertas
  Scenario: Comprobar CTA oferta
    Given Abrir en Chrome la aplicación https://www.iberostar.com/ofertas/ofertas-flash-hoteles/
    And Cargo el DOM de la App: ofertasflash
    Then Espero el elemento: Aceotarcoo
    And Hago clic en Aceotarcoo
    And Hago scroll hacia el elemento: mes9
    Then Espero el elemento: reservar
    Then Hago clic en reservar
    And Tomar Captura: CTA oferta
    Then cierro la app

