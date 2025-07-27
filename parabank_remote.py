import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.options import Options


import pytest
def test_register_user():
    try:
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximised')
        options.set_capability("browserName","firefox")
        options.set_capability('platformName','Windows 11')
        command_executor = 'http://192.168.1.6:4444'
        driver = webdriver.Remote(command_executor= command_executor, options=options)
        driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
        driver.find_element(By.XPATH,'//a[text()="Register"]').click()
        driver.find_element(By.NAME,'customer.firstName').send_keys('testuser')
        driver.find_element(By.NAME, 'customer.lastName').send_keys('testuser')
        driver.find_element(By.NAME, 'customer.address.street').send_keys('430,street road')
        driver.find_element(By.NAME, 'customer.address.city').send_keys('Bangalore')
        driver.find_element(By.NAME, 'customer.address.state').send_keys('karnataka')
        driver.find_element(By.NAME, 'customer.address.zipCode').send_keys('1234238')
        driver.find_element(By.NAME, 'customer.ssn').send_keys('1234238')
        driver.find_element(By.NAME, 'customer.username').send_keys('testuser12')
        driver.find_element(By.NAME, 'customer.password').send_keys('testuser')
        driver.find_element(By.NAME, 'repeatedPassword').send_keys('testuser')
        driver.find_element(By.XPATH,'//input[@value="Register"]').click()
        actual_output = driver.find_element(By.XPATH,"//*[@id='rightPanel']//child::p").text
        expected_output = 'Your account was created successfully. You are now logged in.'
        driver.save_screenshot('image.png')
        assert  expected_output == actual_output, "Account not created due to some problem"

    except:
        raise Exception

    finally:
        driver.quit()

def test_total_balance_remaining():

    try:
        # Invoking Browser and maximising window
        options = Options()
        options.add_argument('--headless')
        options.set_capability('browserName','chrome')
        options.set_capability('platformName','Windows 11')
        # options.add_argument('--start-maximised')
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Remote(command_executor='http://192.168.1.6:4444',options=options)
        driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
        driver.maximize_window()
        # logging in to account
        driver.find_element(By.NAME,'username').send_keys('testuser123')
        driver.find_element(By.NAME,'password').send_keys('testuser')
        driver.find_element(By.XPATH, "//*[@type='submit']").click()
        time.sleep(2)

        # Navigating to 'Available Amount' by dynamically fetching its col number and storing it into var account_col_count
        account_table_headers = driver.find_elements(By.XPATH,'//table[@id="accountTable"]/thead/tr/th')
        account_col_count = 0
        account_bal = 0
        for each_account_header in account_table_headers:
            if each_account_header.text == 'Available Amount':
                account_col_count += 1
                break
            account_col_count += 1

        account_amount_locpath = "//table[@id='accountTable']/tbody/tr/td" + str([account_col_count])
        account_table_row = driver.find_elements(By.XPATH,account_amount_locpath)
        row_count = driver.find_elements(By.XPATH,"//table[@id='accountTable']/tbody/tr")
        no_of_rows = len(row_count)
        for each_account in account_table_row:
            if each_account.text is not " ":
                account_bal += float(each_account.text.split('$')[1])

        total_bal_path = "(//table[@id='accountTable']/tbody/tr" + str([no_of_rows]) + "/td)" + str([account_col_count-1])
        print(total_bal_path)
        total_bal = driver.find_element(By.XPATH,total_bal_path)
        total_bal = float(total_bal.text.split('$')[1])
        print(total_bal)
        assert account_bal == total_bal, "Mismatch in balances"
    finally:
        driver.quit()
