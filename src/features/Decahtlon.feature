# Created by javit at 27/07/2021
Feature: Contacta Decahtlon

  @Tuibusqueda
  Scenario: Rellenar formulario
    Given Abrir en Chrome la aplicación https://www.decathlon.es/es/help/app/ask/session/L3RpbWUvMTYyNzQ5MTY4Ny9nZW4vMTYyNzQ5MTY4Ny9zaWQvZlVfVlp4T01CX3R2RDFfSnRfNkclN0U2V0hSWFBqOWdrME0xNkU3S1lMcEhRZ0FDQ0hEMmdCNWZ0Mm4zS1lHb2tUaWUxQWgzdVppbGU2ZHkzb1UzbzBTWEliME9KX3N2azVqSTZDOXNuQSU3RTlVUGJPUm1kWXVCb0RTZyUyMSUyMQ==
    And Cargo el DOM de la App: decath
    Then Hago clic en Cockies
    Then Hago scroll hacia el elemento: mail1
    And Hago clic en mail1
    And Tomar Captura: Decahtlon1
    Then cierro la app