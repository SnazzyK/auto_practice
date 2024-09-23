import time
from os import times
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('C:\\Users\\valeriy.kaurov\\PycharmProjects\\auto_practice\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
link = "https://www.wildberries.ru/"


driver.get(link)
driver.maximize_window()
time.sleep(2)
main_field = driver.find_element(By.XPATH,"//input[@placeholder='Найти на Wildberries']")
main_field.send_keys("Ноутбук для Hello World")
time.sleep(2)
main_field = driver.find_element(By.XPATH,"//button[@id='applySearchBtn']")
main_field.click()
time.sleep(5)
driver.close()