# -*- coding: utf-8 -*-
import os

class Inicializar():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + u"/pages"

    Environment = 'Test'

    # BROWSER DE PRUEBAS
    NAVEGADOR = u'CHROME'


    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'/data/DataTest.xlsx'

    if Environment == 'Dev':
        URL = 'https://the-internet.herokuapp.com/'


    if Environment == 'Test':
        URL = 'https://demoqa.com/'

