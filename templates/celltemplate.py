from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0r
import os
import time
import requests

def failure():
    bot_id = os.environ['slack_bot_id']
    channel_id = os.environ['slack_channel_id']
    text = "A login load test failed."
    slack_url = "https://slack.com/api/chat.postMessage"
    post_data = {'token':bot_id, 'channel':channel_id, 'text':text}
    post_response = requests.post(url=slack_url, data=post_data)

def cellTest():
	assert True

loginTest()