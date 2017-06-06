import MySQLdb as mysql

db_config = {
    'host': 'localhost',
    'user': 'funkey',
    'password': 'qwer1234',
    'db': 'cwb_test'
}

db = mysql.connect(**db_config)
cur = db.cursor()
