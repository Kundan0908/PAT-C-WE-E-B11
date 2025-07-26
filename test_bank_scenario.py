from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_find_elements_automation():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://parabank.parasoft.com/parabank/index.htm')
        driver.maximize_windows()
        elements = driver.find_elements(By.XPATH,"//ul[@class='services']/child::li")
        for each_element in elements:
            print(each_element.text)
    except :
        raise Exception

    finally:
        driver.quit()

elements = driver.find_elements(By.XPATH,"//ul[@class='Services']/child::li")
# elements = driver.find_elements(By.XPATH,"//ul[@class='services']/child::li")