# Created by javit at 19/10/2020
Feature: Pruebas

  @Prueba
  Scenario: Rellenar formularios Text Box
    Given Inicilizo la app en la URL https://demoqa.com/
    And Cargo el DOM de la App: pruebas
    Then Hago scroll hacia el elemento: elementos
    And Espero el elemento: elementos
    And Hago clic en elementos
    And Hago clic en textbox
    And En el campo name tecleo Javier
    Then En el campo mail tecleo mallorca@gmail.com
    Then En el campo direccion tecleo Santa margalida
    Then En el campo perdireccion tecleo Sa torre
    And Hago scroll hacia el elemento: submit
    And Hago clic en submit
    And Espero 3 segundos
    And Tomar Captura: ElemmentoBox
    Then cierro la app

  @Prueba
  Scenario: Comprobar Check Box Radio Button webtables
    Given Inicilizo la app en la URL https://demoqa.com/
    And Cargo el DOM de la App: pruebas
    Then Hago scroll hacia el elemento: elementos
    And Espero el elemento: elementos
    And Hago clic en elementos
    And Hago clic en checkbox
    Then Hago clic en home
    Then Hago clic en desplegar
    And Hago clic en radiobutton
    Then Hago clic en Impresive
    And Hago clic en webtables
    And Espero el elemento: search
    Then Hago scroll hacia el elemento: search
    And En el campo search tecleo cierra
    Then Espero 3 segundos
    And Retroceder
    And Tomar Captura: ElemmentoBox1
    Then cierro la app

  @Prueba
  Scenario: Rellenar formulario inscripcion
    Given Inicilizo la app en la URL https://demoqa.com/
    And Cargo el DOM de la App: pruebas
    And Hago clic en forms
    Then Hago clic en practriceform
    And En el campo nombre tecleo Javier
    Then En el campo lastname tecleo Vazquez
    Then En el campo mailform tecleo mallorca@gmail.com
    And Hago clic en male
    And En el campo tlf tecleo 324545454
    And Hago clic en date
    Then Hago clic en octubre
    And Hago clic en sport
    Then En el campo adress tecleo narodona1
    And Hago scroll hacia el elemento: dropsatate
    And Yo hago clic dropsatate con el texto NCR
    And Yo hago clic dropscity con el texto Delhi
    And Hago scroll hacia el elemento: sub
    And Hago clic en sub
    Then Retroceder
    And Tomar Captura: form1
    Then cierro la app

  @Prueba
  Scenario:Hacer click en formulario Grid
    Given Inicilizo la app en la URL https://demoqa.com/
    And Cargo el DOM de la App: pruebas
    Then Hago scroll hacia el elemento: inter
    And Hago clic en inter
    Then Hago scroll hacia el elemento: soportable
    And Hago clic en soportable
    Then Hago clic en grid
    Then Hago clic en one
    Then Hago clic en dos
    Then Hago clic en 3
    And Tomar Captura: Grid
    Then cierro la app

  @Prueba
  Scenario:Hacer click en aceptar
    Given Inicilizo la app en la URL https://demoqa.com/
    And Cargo el DOM de la App: pruebas
    Then Hago scroll hacia el elemento: alertgeneral
    And Hago clic en alertgeneral
    And Hago clic en alertsopcion
    And Hago clic en aceptar
    And Aceptar ventana emergente
    And Espero el elemento: aceptar2
    And Hago clic en aceptar2
    Then Espero 6 segundos
    And Aceptar ventana emergente
    And Hago clic en aceptar3
    Then Aceptar ventana emergente
    And Hago clic en aceptar4
    Then Aceptar ventana emergente
    And Tomar Captura: 12
    Then cierro la app

  @Prueba
  Scenario:Hacer log in en aplicacion
    Given Inicilizo la app en la URL https://demoqa.com/
    And Cargo el DOM de la App: pruebas
    Then Hago scroll hacia el elemento: Bookstore
    And Hago clic en Bookstore
    Then Hago scroll hacia el elemento: Login
    And Espero el elemento: Login
    And Hago clic en Login
    And Hago clic en Usuario
    And Hago clic en Password
    And Hago clic en NuevoUsuario
    Then Retroceder
    And En el campo Usuario hago clear y escribo  jvazquez
    And En el campo Password hago clear y escribo  1298987
    And Tomar Captura: Login
    Then cierro la app

  @Prueba
  Scenario:Progreso
    Given Inicilizo la app en la URL https://demoqa.com/widgets
    And Cargo el DOM de la App: pruebas
    Then Espero el elemento: Progreso
    And Hago scroll hacia el elemento: Progreso
    Then Hago clic en Progreso
    And Espero el elemento: Start
    Then Hago clic en Start
    And Espero 3 segundos
    Then Hago clic en Start
    And Tomar Captura: Start
    Then cierro la app

    @Prueba
  Scenario:Autocmpletar colores
    Given Inicilizo la app en la URL https://demoqa.com/widgets
    And Cargo el DOM de la App: pruebas
    Then Espero el elemento: Autcomppletar
    And Hago scroll hacia el elemento: Autcomppletar
    Then Hago clic en Autcomppletar
    And Espero el elemento: Color
    Then Yo hago clic Color con el texto Red
    And Tomar Captura: Colores
    Then cierro la app

    
    