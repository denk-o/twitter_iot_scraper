import configparser

config = configparser.ConfigParser()

config.read('config/config.ini')

API_KEY = config['API']['api_key']
SECRET = config['API']['secret']
ACCESS_KEY = config['API']['access_key']
ACCESS_SECRET = config['API']['access_secret']
