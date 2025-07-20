from optparse import Option

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

def test_headless_automation():

# Setup WebDriver (Make sure to set the path to your WebDriver)
    try:
        driver_option = Options()
        # driver_option.add_argument("--headless")
        driver_option.add_argument("--incognito")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=driver_option)
        driver.get('https://the-internet.herokuapp.com/windows')
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//a[text()="Click Here"]').click()
        windows = driver.window_handle
        for each_window in windows:
            driver.switch_to.window(each_window)
            print(driver.title)
            print(driver.current_url)

    except Exception as e:
            print(e)

    finally:
        driver.quit()