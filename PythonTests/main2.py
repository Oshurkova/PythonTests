from selenium import webdriver
from selenium.webdriver.common.by import By

with open('credit_info.txt', 'r') as file:
    for line in file:

        loanAmount, loanPeriod, lastName, firstName, middleName, dob, \
        passportSeries, passportNumber, passportIssueDate, passportIssuedBy, \
        snils, education, registrationAddress, residentialAddress, phone \
        = line.strip().split(' ')

        #часть экспорта из Selenium IDE
        driver = webdriver.Chrome()

        driver.get("http://127.0.0.1:5000/createcase")
        driver.set_window_size(834, 661)
        driver.find_element(By.ID, "creditProgram").click()
        dropdown = driver.find_element(By.ID, "creditProgram")
        dropdown.find_element(By.XPATH, "//option[. = 'Программа 2']").click()
        driver.find_element(By.ID, "loanAmount").click()
        driver.find_element(By.ID, "loanAmount").send_keys(loanAmount)
        driver.find_element(By.ID, "loanPeriod").click()
        driver.find_element(By.ID, "loanPeriod").send_keys(loanPeriod)
        driver.find_element(By.ID, "lastName").click()
        driver.find_element(By.ID, "lastName").send_keys(lastName)
        driver.find_element(By.ID, "firstName").click()
        driver.find_element(By.ID, "firstName").send_keys(firstName)
        driver.find_element(By.ID, "middleName").click()
        driver.find_element(By.ID, "middleName").send_keys(middleName)
        driver.find_element(By.ID, "dob").click()
        driver.find_element(By.ID, "dob").send_keys(dob)
        driver.find_element(By.ID, "passportSeries").click()
        driver.find_element(By.ID, "passportSeries").send_keys(passportSeries)
        driver.find_element(By.ID, "passportNumber").click()
        driver.find_element(By.ID, "passportNumber").send_keys(passportNumber)
        driver.find_element(By.ID, "passportIssueDate").click()
        driver.find_element(By.ID, "passportIssueDate").send_keys(passportIssueDate)
        driver.find_element(By.ID, "passportIssuedBy").click()
        driver.find_element(By.ID, "passportIssuedBy").send_keys(passportIssuedBy)
        driver.find_element(By.CSS_SELECTOR, "form").click()
        driver.find_element(By.ID, "snils").click()
        driver.find_element(By.ID, "snils").send_keys(snils)
        driver.find_element(By.ID, "education").click()
        driver.find_element(By.ID, "education").send_keys(education)
        driver.find_element(By.ID, "registrationAddress").click()
        driver.find_element(By.ID, "registrationAddress").send_keys(registrationAddress)
        driver.find_element(By.ID, "residentialAddress").click()
        driver.find_element(By.ID, "residentialAddress").send_keys(residentialAddress)
        driver.find_element(By.ID, "phone").click()
        driver.find_element(By.ID, "phone").send_keys(phone)
        driver.find_element(By.ID, "agreement").click()
        driver.find_element(By.CSS_SELECTOR, ".button").click()

        driver.quit()