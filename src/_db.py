import os


db_user = os.environ.get('POSTGRES_USER', 'db_user')
db_password = os.environ.get('POSTGRES_PASSWORD', 'db_password')
db_database = os.environ.get('POSTGRES_DB', 'db_database')
test_db_database = f'test_{db_database}'
db_host = os.environ.get('DB_HOST', 'db_host')
db_port = os.environ.get('DB_PORT', 'db_port')


BASE_SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}'
SQLALCHEMY_DATABASE_URL = f'{BASE_SQLALCHEMY_DATABASE_URL}/{db_database}'
TEST_SQLALCHEMY_DATABASE_URL = f'{BASE_SQLALCHEMY_DATABASE_URL}/{test_db_database}'
