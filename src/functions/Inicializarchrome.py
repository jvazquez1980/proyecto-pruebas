# -*- coding: utf-8 -*-
import os

class Inicializarchrome():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + u"/pages"

    Environment = 'Dev'

    # BROWSER DE PRUEBAS
    NAVEGADOR = u'Chrome'

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'/data/DataTest.xlsx'

    if Environment == 'Dev':
        URL = 'https://www.iberostar.com/es/'

    if Environment == 'Test':
        URL = 'https://demoqa.com/'
