from environs import Env

env = Env()
env.read_env()

bucket_name = env('BUCKET_NAME')
file_name = env('FILE_NAME')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
db_path = env('DB_PATH')
db_login = env('DB_LOGIN')
db_password = env('DB_PASSWORD')