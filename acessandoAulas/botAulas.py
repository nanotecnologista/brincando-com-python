from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, time
import os


#Descobrindo o dia da semana
dataHoje = datetime.today().isoweekday()

#Capturando a hora atual
hora = (datetime.today().time())
horaAtual = hora.strftime('%H:%M')

# #chamando a matéria
# def aula_Arquitetura(browser):
#     return 0.0
# def aula_Metodologia(browser):
#     return 0.0
# def aula_Laboratorio(browser):
#     return 0.0

def start():
#configurando o navegador
    options = webdriver.ChromeOptions()

    options.add_argument("--log-level=3")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument('ignore-certificate-errors')


    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 2})

    #usando dados anteriores
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "usuario")
    options.add_argument(r"user-data-dir={}".format(profile))

    #passando o caminho do navegador
    browser = webdriver.Chrome(options=options,executable_path='/home/julia/Downloads/GitHub/brincandoComPython/acessandoAulas/chromedriver')

    #passando link do site
    #Se o dia e a hora forem iguais ao horário da aula...
    if dataHoje == 2 and horaAtual >= "20:20":
        browser.get("https://conferenciaweb.rnp.br/webconf/flaviamsn")
        #aula_Arquitetura(browser)
        input("digite ok")
           
    elif dataHoje == 3 and horaAtual >= "19:30":
        browser.get("https://conferenciaweb.rnp.br/webconf/simone-amorim")
        #aula_Metodologia(browser)
        input("passou aqui")
            
    elif dataHoje == 4:
        if horaAtual >= "18:40" and horaAtual <= "20:20":
            browser.get("http://meet.google.com/wrz-zbjk-jnn")
            #aula_Laboratorio(browser)
            input("digite ok")

    input("tá aqui")

start()
            
    
    



