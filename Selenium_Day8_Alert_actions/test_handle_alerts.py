import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

def test_action_demo():
    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('start-maximised')
        options.set_capability('browserName','firefox')
        driver = webdriver.Remote(command_executor="http://192.168.1.6:4444",options=options)
        driver.get('https://testautomationpractice.blogspot.com/#')
        alert = Alert(driver)

        # Simple Alert
        simple_alert_ele = driver.find_element(By.ID,'alertBtn')
        simple_alert_ele.click()
        time.sleep(1)
        alert.accept()

        # Confirmation Alert
        conf_alert_ele = driver.find_element(By.ID, 'confirmBtn')
        conf_alert_ele.click()
        time.sleep(1)
        alert.dismiss()

        # Prompt Alert
        promt_alert_ele = driver.find_element(By.ID, 'promptBtn')
        promt_alert_ele.click()
        alert.send_keys('Testing_Alert')
        time.sleep(4)
        alert.accept()
        msg_ = driver.find_element(By.ID,'demo').text
        print(msg_)
        # driver.save_screenshot('simple_alert.png')

    finally:
        driver.quit()
