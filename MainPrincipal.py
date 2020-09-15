from time import sleep
from selenium import webdriver

#Vai rodar o Firefox aqui!
browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')

sleep(5)

browser.close()
