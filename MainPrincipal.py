from time import sleep
from selenium import webdriver

#Vai rodar o Firefox aqui!
navegador = webdriver.Firefox()
navegador.implicitly_wait(5)

navegador.get('https://www.instagram.com/')

btnlogin = navegador.find_element_by_xpart("//a[text()='Entrar']")
btnlogin.click

sleep(5)

navegador.close()
