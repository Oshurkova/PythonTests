import time
import logging
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#добавим логирование
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with open('users.txt', 'r') as file:
    for line in file:

        username, password = line.strip().split(' ')
        
        #добавляем ChromeOptions для ошибки CertVerifyProcBuiltin for content-autofill.googleapis.com failed
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chromeOptions)

        #часть экспорта из Selenium IDE
        driver.get("http://127.0.0.1:5000/authorization")
        driver.find_element(By.NAME, "Login").click()
        driver.find_element(By.NAME, "Login").send_keys(username)
        driver.find_element(By.NAME, "Password").click()
        driver.find_element(By.NAME, "Password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button").click()
        
        #получение данных о запросах с seleniumwire
        for request in driver.requests:
            logging.info(f"Request URL: {request.url}")
            logging.info(f"Request Body: {request.body}")
            logging.info(f"Response Status: {request.response.status_code}")
        
        time.sleep(1)
        driver.quit()

        