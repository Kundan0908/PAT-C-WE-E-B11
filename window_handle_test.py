import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


def test_window_handle_automation():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://demoqa.com/browser-windows')
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'//button[text()="New Tab"]').click()
        windows = driver.window_handles
        for windo in windows:
            driver.switch_to.window(windo)
            print(driver.title)
    finally:
        driver.quit()

