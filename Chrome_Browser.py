
# selenium is basically used for web-scraping and web-automation
# in easy words basically used to extract data from websites


# WEBDRIVER: allow us to interact with web-browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

executable_path="Your chromedriver_path "
# This creates a service object that tells Selenium where the ChromeDriver is located.
chrome_service=Service(executable_path)


# This is like opening a new Chrome browser window that you can control with your code.
driver=webdriver.Chrome(service=chrome_service)

# .get() method opens the specified URL in the browser.
driver.get("https://www.bing.com/?mkt=en-EN")

time.sleep(4)
