from configparser import ConfigParser

config = ConfigParser()

config['DEFAULT'] = {
    "username": "standard_user",
    "password" : "secret_sauce"
}

config['LOCKEDUSER'] = {
    'username': 'locked_out_user',
    "password" : 'secret_sauce'
}
with open(file='config.ini',mode='w') as f:
    config.write(f)