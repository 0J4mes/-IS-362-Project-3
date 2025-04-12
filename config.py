# Database configuration for non-SQLite databases
DB_CONFIG = {
    'postgresql': {
        'dialect': 'postgresql',
        'username': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'port': '5432',
        'database': 'chinook'
    },
    'mysql': {
        'dialect': 'mysql+pymysql',
        'username': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'database': 'chinook'
    }
}