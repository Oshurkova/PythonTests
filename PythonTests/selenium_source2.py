# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCreatecase1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createcase1(self):
    self.driver.get("http://127.0.0.1:5000/createcase")
    self.driver.set_window_size(834, 661)
    self.driver.find_element(By.ID, "creditProgram").click()
    dropdown = self.driver.find_element(By.ID, "creditProgram")
    dropdown.find_element(By.XPATH, "//option[. = 'Программа 2']").click()
    self.driver.find_element(By.ID, "loanAmount").click()
    self.driver.find_element(By.ID, "loanAmount").send_keys("2")
    self.driver.find_element(By.ID, "loanPeriod").click()
    self.driver.find_element(By.ID, "loanPeriod").send_keys("2")
    self.driver.find_element(By.ID, "lastName").click()
    self.driver.find_element(By.ID, "lastName").send_keys("2")
    self.driver.find_element(By.ID, "firstName").click()
    self.driver.find_element(By.ID, "firstName").send_keys("2")
    self.driver.find_element(By.ID, "middleName").click()
    self.driver.find_element(By.ID, "middleName").send_keys("2")
    self.driver.find_element(By.ID, "dob").click()
    self.driver.find_element(By.ID, "dob").send_keys("0002-02-02")
    self.driver.find_element(By.ID, "passportSeries").click()
    self.driver.find_element(By.ID, "passportSeries").send_keys("2")
    self.driver.find_element(By.ID, "passportNumber").click()
    self.driver.find_element(By.ID, "passportNumber").send_keys("2")
    self.driver.find_element(By.ID, "passportIssueDate").click()
    self.driver.find_element(By.ID, "passportIssueDate").send_keys("0002-02-02")
    self.driver.find_element(By.ID, "passportIssueDate").send_keys("0020-02-02")
    self.driver.find_element(By.ID, "passportIssueDate").send_keys("0200-02-02")
    self.driver.find_element(By.ID, "passportIssueDate").send_keys("2001-02-02")
    self.driver.find_element(By.ID, "passportIssuedBy").click()
    self.driver.find_element(By.ID, "passportIssuedBy").send_keys("2")
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    self.driver.find_element(By.ID, "snils").click()
    self.driver.find_element(By.ID, "snils").send_keys("2")
    self.driver.find_element(By.ID, "education").click()
    self.driver.find_element(By.ID, "education").send_keys("2")
    self.driver.find_element(By.ID, "registrationAddress").click()
    self.driver.find_element(By.ID, "registrationAddress").send_keys("2")
    self.driver.find_element(By.ID, "residentialAddress").click()
    self.driver.find_element(By.ID, "residentialAddress").send_keys("2")
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("2")
    self.driver.find_element(By.ID, "agreement").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button").click()
  
