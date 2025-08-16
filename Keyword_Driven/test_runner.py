from csv import DictReader
import keywords
# dict_ = {'Data':1,'Data2':2}
# print(dict_['Data'])

def test_execute_steps():
    with open(file='test_data.csv', mode='r') as data:
        read_data = DictReader(data) #-> [steps,Keywords,Locator,Value]
        for row in read_data:
            keyword = row['Keywords'] # in dictionary we need key value pair , keyword = 'enter_username'
            value = row['Value'] # value = 'testuser12'
            locator = row['Locator'] # locator = 'username'
            func = getattr(keywords,keyword) # func = getattr(keywords,enter_username)
            if locator and value: # False and True -> False, True and True -> True, True and True -> True
                func(locator,value) # enter_username('username','testuser12')
            elif value: #
                func(value) # Open_Browser('https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC')
            elif locator:
                func(locator)
            else:
                func()
