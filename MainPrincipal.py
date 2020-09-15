from selenium import webdriver
import Motor

#<?php include(...Oops aqui não rs

chromedriver_path = 'C:/Users/pc/Documents/BotInstagram/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

Motor.init(webdriver)
Motor.update(webdriver)

webdriver.close()
