from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_explicit_wait_demo():
    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('start-maximised')
        options.set_capability('browserName','firefox')
        driver = webdriver.Remote(command_executor="http://192.168.1.6:4444",options=options)
        driver.get('https://the-internet.herokuapp.com/dynamic_loading')
        driver.find_element(By.XPATH,"//a[contains(text(),'Example 1')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'Start')]").click()
        wait = WebDriverWait(driver,20)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//h4[text()='Hello World!']")))
        print(driver.find_element(By.XPATH, "//h4[text()='Hello World!']").text)

    except:
        raise Exception

    finally:
        driver.quit()