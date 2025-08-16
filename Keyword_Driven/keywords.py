from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def Open_browser(url):
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url=url)

def enter_username(locator,value):
    driver.find_element(By.NAME,locator).send_keys(value)

def enter_password(locator,value):
    driver.find_element(By.NAME, locator).send_keys(value)

def click_login(locator):
    driver.find_element(By.XPATH, locator).click()