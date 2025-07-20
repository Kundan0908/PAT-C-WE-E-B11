import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


def test_window_handle_automation():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://the-internet.herokuapp.com/iframe')
        driver.implicitly_wait(5)
        driver.switch_to.frame(driver.find_element(By.ID,'mce_0_ifr'))
        print(driver.find_element(By.XPATH,"//body[starts-with(@class,'mce-content')]/child::p").text)
    finally:
        driver.quit()
