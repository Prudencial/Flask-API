import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    BASE_DIR = basedir
    SECRET_KEY = os.urandom(32)

   # Important parameters to use and initilize the database
    MYSQL_HOST = 'localhost' # can be any

    # Username for your mysql database
    MYSQL_USER = 'root'

    # Password for your mysql database
    MYSQL_PASSWORD = ''

    # database name
    MYSQL_DB = 'products'