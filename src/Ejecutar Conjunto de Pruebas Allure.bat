echo. ##################### PRUEBAS #####################
cd C:\pycharm\src
rd /s /q allure-report
rd /s /q allure-results
cd C:\pycharm\src\tests
python -m pytest test_050.py --alluredir ..\allure-results
python -m pytest tui.py --alluredir ..\allure-results
cd.. 
allure generate C:\pycharm\src\allure-results --output C:\pycharm\src\allure-report --clean && allure open --port 5000	
pause