import time
from optparse import Option

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.mark.register_account
def test_register_user():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
        driver.find_element(By.XPATH,'//a[text()="Register"]').click()
        driver.find_element(By.NAME,'customer.firstName').send_keys('testuser')
        driver.find_element(By.NAME, 'customer.lastName').send_keys('testuser')
        driver.find_element(By.NAME, 'customer.address.street').send_keys('430,street road')
        driver.find_element(By.NAME, 'customer.address.city').send_keys('Bangalore')
        driver.find_element(By.NAME, 'customer.address.state').send_keys('karnataka')
        driver.find_element(By.NAME, 'customer.address.zipCode').send_keys('1234238')
        driver.find_element(By.NAME, 'customer.ssn').send_keys('1234238')
        driver.find_element(By.NAME, 'customer.username').send_keys('testuser123')
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


def test_check_popups():
    try:
        # Invoking Browser and maximising window
        chrome_options = Options()
        chrome_options.add_argument("--disable-features=SafetyTip,PasswordCheck")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
        driver.maximize_window()

        # logging in to account
        driver.find_element(By.NAME,'username').send_keys('testuser123')
        driver.find_element(By.NAME,'password').send_keys('testuser')
        driver.find_element(By.XPATH, "//*[@type='submit']").click()
        time.sleep(2)
        # alert = driver.switch_to.alert
        # alert.accept()
    finally:
        driver.quit()

@pytest.mark.balance_check
def test_total_balance_remaining():
    try:
        # Invoking Browser and maximising window
        chrome_options = Options()
        chrome_options.add_argument("--disable-features=SafetyTip,PasswordCheck")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
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
        print(f"total acount balance {total_bal} is matching with actual account balance {account_bal}")
        driver.save_screenshot('account_statement.png')
        assert account_bal == total_bal, "Mismatch in balances"
    finally:
        driver.quit()


@pytest.mark.sanity
def test_get_headerpanel_data():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
        headerpanel = driver.find_elements(By.XPATH,"//ul[@class='leftmenu']//child::li")
        for eachitem in headerpanel:
            print(eachitem.text)
            if eachitem.text == 'Products':
                eachitem.click()
                print(driver.current_url)
                driver.save_screenshot('Products_page.png')
                break
    except:
        raise Exception

    finally:
        driver.quit()


@pytest.mark.e2e
def test_money_transfer():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
        driver.find_element(By.NAME,'username').send_keys('abc')
        driver.find_element(By.NAME, 'password').send_keys('abc')
        driver.find_element(By.XPATH, '//*[@value="Log In"]').submit()
        check_for_login = driver.find_element(By.XPATH,"//*[@id='showOverview']//child::h1").text
        assert check_for_login == 'Accounts Overview'.strip(), "Not logged in"
        get_elements = driver.find_elements(By.XPATH,"//*[@id = 'accountTable']/child::thead/tr/th")
        count,account_count = 1,0
        cal_amount = 0
        for each_element in get_elements:
            if each_element.text == 'Available Amount':
                break
            count +=1
        path_ = "//*[@id = 'accountTable']/child::tbody/tr/td" + str([count])
        time.sleep(4)
        amount_ele = driver.find_elements(By.XPATH,path_)
        for each_amount in amount_ele:
            if each_amount.text is not " ":
                each_amount = each_amount.text.split('$')[1]
                cal_amount += float(each_amount)
            account_count += 1
        total_amt_path = "(//*[@id = 'accountTable']/child::tbody/tr/td" + str([count-1]) +")" + str([account_count])
        actual_amount_text = driver.find_element(By.XPATH,total_amt_path)
        actual_amount = float(actual_amount_text.text.split('$')[1])
        assert cal_amount == actual_amount, "Data mismatch"
    except:
        raise Exception

    finally:
        driver.quit()
