from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest2():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_test2(self):
        self.driver.get("http://127.0.0.1:5000/authorization")
        self.driver.set_window_size(1222, 657)
        self.driver.find_element(By.NAME, "Login").click()
        self.driver.find_element(By.NAME, "Login").send_keys("user1")
        self.driver.find_element(By.NAME, "Password").click()
        self.driver.find_element(By.NAME, "Password").send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()