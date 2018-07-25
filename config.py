import configparser

config = configparser.ConfigParser()

config.read('config/config.ini')

API_KEY = config['API']['api_key']
SECRET = config['API']['secret']
