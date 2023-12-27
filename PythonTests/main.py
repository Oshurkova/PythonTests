import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('users.txt', 'r') as file:
    for line in file:

        username, password = line.strip().split(' ')

        #часть экспорта из Selenium IDE
        driver = webdriver.Chrome()
        
        driver.get("http://127.0.0.1:5000/authorization")
        driver.find_element(By.NAME, "Login").click()
        driver.find_element(By.NAME, "Login").send_keys(username)
        driver.find_element(By.NAME, "Password").click()
        driver.find_element(By.NAME, "Password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button").click()

        time.sleep(1)
        driver.quit()