from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, time
from time import sleep  # lib tempo
import os


#Descobrindo o dia da semana
dataHoje = datetime.today().isoweekday()
#Capturando a hora atual
hora = (datetime.today().time())
horaAtual = hora.strftime('%H:%M')


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
        login_button = browser.find_element_by_xpath("//input[@name='commit']")
        sleep(10)
        login_button.click()
           
    elif dataHoje == 2 and horaAtual >= "19:30":
        browser.get("https://conferenciaweb.rnp.br/webconf/simone-amorim")
        login_button = browser.find_element_by_xpath("//input[@name='commit']")
        sleep(10)
        login_button.click()

       
    elif dataHoje == 3:
        if horaAtual >= "16:40" and horaAtual <= "20:20":
            browser.get("http://meet.google.com/wrz-zbjk-jnn")
            sleep(20)
            login_button = browser.find_element_by_xpath("//*[contains(text(),'Pedir para participar')]")
            login_button.click()
            input("aqui")

    input("tá aqui")
start()
            
    
    



