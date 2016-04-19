from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0r
import os
import time
import requests

def postErrorToSlack():
    bot_id = os.environ['slack_bot_id']
    channel_id = os.environ['slack_channel_id']
    text = "A login load test failed."
    slack_url = "https://slack.com/api/chat.postMessage"
    post_data = {'token':bot_id, 'channel':channel_id, 'text':text}
    post_response = requests.post(url=slack_url, data=post_data)

def loginTest():
    print "starting login test with user: " + str(test_user)
    driver = webdriver.PhantomJS()
    driver.get("https://jhubdev.westus.cloudapp.azure.com")
    try:
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        WebDriverWait(driver, 10).until(EC.title_contains("Jupyter Hub"))
            
        usernameField = driver.find_element_by_id('username_input')
        usernameField.send_keys(test_user)

        loginButton = driver.find_element_by_id("login_submit").click()

        WebDriverWait(driver, 10).until(EC.title_contains("Home"))
        assert True
    except:
        postErrorToSlack()
        assert False
    driver.quit()

loginTest()