# Created by javit at 29/10/2020
Feature: Comprobar elementos reserva web
  # Enter feature description here

  @ElementosIberostar
  Scenario: Elementos principales
    Given Inicilizo la app en la URL https://www.iberostar.com/es/
    And Cargo el DOM de la App: ibero
    And Comprobar elemento: Escribetudestino
    Then Comprobar elemento: Fastbooking
    And Hago scroll hacia el elemento: Seleccionarfechas
    Then Comprobar elemento: Seleccionarfechas
    And Tomar Captura: Iberoreserva
    Then cierro la app

  @ElementosIberostar
  Scenario: Elementos header
    Given Inicilizo la app en la URL https://www.iberostar.com/es/
    And Cargo el DOM de la App: elements
    And Hago clic en AceptarCockies
    And Comprobar elemento: ADE
    And Comprobar elemento: MiIberostar
    Then Comprobar elemento: GestionarReserva
    And Hago scroll hacia el elemento: ModuloBajoFastbooking1
    Then Comprobar elemento: ModuloBajoFastbooking1
    And Tomar Captura: Iberoreserva
    Then cierro la app

  @ElementosIberostar
  Scenario: Elementos secundarios
    Given Inicilizo la app en la URL https://www.iberostar.com/es/
    And Cargo el DOM de la App: elements
    And Hago clic en AceptarCockies
    And Hago scroll hacia el elemento: ModuloBajoFastbooking2
    Then Comprobar elemento: ModuloBajoFastbooking
    Then Comprobar elemento: ModuloBajoFastbooking3
    Then Comprobar elemento: ModuloBajoFastbooking1
    Then Comprobar elemento: ModuloBajoFastbooking4
    Then Comprobar elemento: ModuloBajoFastbooking2
    And Hago scroll hacia el elemento: Entornoseguro
    Then Comprobar elemento: Entornoseguro
    Then Comprobar elemento: Estandaresdehigiene
    Then Comprobar elemento: Espaciosocial
    Then Hago scroll hacia el elemento: FAQ
    Then Comprobar elemento: FAQ
    And Hago scroll hacia el elemento: WaveOfChange
    Then Comprobar elemento: WaveOfChange
    And Tomar Captura: Iberoreserva
    Then cierro la app

  @ElementosIberostar
  Scenario: Elementos ver hoteles SobreNosotrosHeader iberostar y otros elementos secundarios
    Given Inicilizo la app en la URL https://www.iberostar.com/es/
    And Cargo el DOM de la App: elements
    And Hago scroll hacia el elemento: VerHotelSugerido1
    Then Espero el elemento: VerHotelSugerido1
    Then Comprobar elemento: VerHotelSugerido2
    Then Comprobar elemento: VerHotelSugerido3
    Then Comprobar elemento: VerHotelSugerido4
    And Hago scroll hacia el elemento: ServiciosUnicosIberostar3
    Then Comprobar elemento: ServiciosUnicosIberostar3
    Then Comprobar elemento: ServiciosUnicosIberostar1
    Then Comprobar elemento: ServiciosUnicosIberostar4
    Then Hago scroll hacia el elemento: EligeTuExperienciaUnica1
    Then Comprobar elemento: EligeTuExperienciaUnica1
    Then Comprobar elemento: EligeTuExperienciaUnica2
    Then Comprobar elemento: EligeTuExperienciaUnica3
    Then Comprobar elemento: EligeTuExperienciaUnica4
    And Hago scroll hacia el elemento: FotterTipoDeHotel1
    Then Comprobar elemento: FotterTipoDeHotel1
    Then Comprobar elemento: FotterTipoDeHotel2
    Then Comprobar elemento: FotterTipoDeHotel3
    Then Comprobar elemento: FotterTipoDeHotel4
    And Tomar Captura: Iberoreserva
    Then cierro la app