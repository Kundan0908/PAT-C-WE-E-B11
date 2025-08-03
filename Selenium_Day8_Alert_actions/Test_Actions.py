import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_action_demo():
    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('start-maximised')
        options.set_capability('browserName','chrome')
        driver = webdriver.Remote(command_executor="http://192.168.1.6:4444",options=options)
        actions = ActionChains(driver)
        driver.get('https://testautomationpractice.blogspot.com/#')
        dropdown_element = driver.find_element(By.XPATH, "//button[text()='Point Me']")
        select_element = driver.find_element(By.XPATH, "//a[text()='Laptops']")
        time.sleep(3)
        actions.move_to_element(dropdown_element).move_to_element(select_element).perform()
        driver.save_screenshot("mousehover.png")
        actions.move_to_element(dropdown_element).click(select_element).perform()
        driver.save_screenshot("click.png")

    finally:
        driver.quit()


def test_doubleclick():
    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('start-maximised')
        options.set_capability('browserName','chrome')
        driver = webdriver.Remote(command_executor="http://192.168.1.6:4444",options=options)
        actions = ActionChains(driver)
        driver.get('https://testautomationpractice.blogspot.com/#')
        double_click_element = driver.find_element(By.XPATH,'//button[text()="Copy Text"]')
        actions.move_to_element(double_click_element).perform()
        input_box_field2_before = driver.find_element(By.ID,'field2').get_attribute('value')
        print(input_box_field2_before)
        actions.double_click(double_click_element).perform()
        input_box_field2_after = driver.find_element(By.ID,'field2').get_attribute('value')
        print(input_box_field2_after)

    finally:
        driver.quit()


def test_dragndrop():

    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('start-maximised')
        options.set_capability('browserName','chrome')
        driver = webdriver.Remote(command_executor="http://192.168.1.6:4444",options=options)
        actions = ActionChains(driver)
        driver.get('https://testautomationpractice.blogspot.com/#')
        drage_ = driver.find_element(By.XPATH,'//p[text()="Drag me to my target"]')
        actions.move_to_element(drage_)
        drop_ = driver.find_element(By.XPATH,'//div[@id="droppable"]/p')
        actions.drag_and_drop(source=drage_, target=drop_).perform()
        time.sleep(5)
    finally:
        driver.quit()


