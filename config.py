from environs import Env

env = Env()
env.read_env()

BUCKET_NAME = env('BUCKET_NAME')
FILE_NAME = env('FILE_NAME')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
DB_PATH = env('DB_PATH')
DB_LOGIN = env('DB_LOGIN')
DB_PASSWORD = env('DB_PASSWORD')