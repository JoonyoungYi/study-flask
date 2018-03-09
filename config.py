SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}' \
    .format('root',             # mysql id
            '',                 # mysql pw
            'localhost',        # remote addr
            3306,               # remote port
            'test')             # database name

SQLALCHEMY_TRACK_MODIFICATIONS = False
USERNAME = 'yearnning'
PASSWORD = 'yearnning'
SECRET_KEY = '1234123412341234'
