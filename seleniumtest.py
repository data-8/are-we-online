from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0r
import os
import time

class LoginTest(object):
    
    def __init__(self, driver, gmailUsername, gmailPassword, calnetUsername, calnetPassword):
        self.driver = driver
        self.gmailUsername = gmailUsername
        self.gmailPassword = gmailPassword
        self.calnetUsername = calnetUsername
        self.calnetPassword = calnetPassword

    def run(self):
        driver.get("https://ds8.berkeley.edu/hub/login")
        loginButton = driver.find_element_by_class_name("btn-jupyter").click()
        try:
            # we have to wait for the page to refresh, the last thing that seems to be updated is the title
            WebDriverWait(driver, 10).until(EC.title_contains("Sign in"))
            usernameField = driver.find_element_by_id('Email')
            usernameField.send_keys(self.gmailUsername)
            try:
                passwordField = driver.find_element_by_id('Passwd')
                passwordField.send_keys(self.gmailPassword)
            except:
                pass
            
            loginButton = driver.find_element_by_id("signIn").click()

            WebDriverWait(driver, 10).until(EC.title_contains("CalNet"))

            usernameField = driver.find_element_by_id('username')
            usernameField.send_keys(self.calnetUsername)

            passwordField = driver.find_element_by_id('password')
            passwordField.send_keys(self.calnetPassword)

            loginButton = driver.find_element_by_class_name("button").click()

            WebDriverWait(driver, 10).until(EC.title_contains("Jupyter Hub"))
            return True
        except:
            return False


driver = webdriver.PhantomJS()
google_username = os.environ['google_username']
google_password = os.environ['google_password']
calnet_username = os.environ['calnet_username']
calnet_password = os.environ['calnet_password']
loginTest = LoginTest(driver, google_username, google_password, calnet_username, calnet_password)
result = loginTest.run()
if result:
    print "login test passed"
else:
    print "login test failed"
driver.quit()