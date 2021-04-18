import boto3
import json
import time

from db import session
from func_type import song, movie, app

from config import BUCKET_NAME, FILE_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

key_values = ['song', 'movie', 'app']
function_dict = {'song': song, 'movie': movie, 'app': app}

def get_file(bucket_name, file_name):
    try:
        obj = s3.Object(bucket_name, file_name)
        return obj.get()['Body'].read().decode("utf-8")
    except Exception as e:
        print(f'Error s3: {e}')


def new_files():
    new_files_name = get_file(BUCKET_NAME, FILE_NAME).split('\n')
    with open('files_name.json', 'r') as read:
        old_files_name = json.load(read)
    difference_files_name = list(set(new_files_name) - set(old_files_name))
    with open('files_name.json', 'w') as write:
        json.dump(old_files_name + difference_files_name, write)
    return difference_files_name


def parse():
    files_name = new_files()
    print(f'Count new files: {len(files_name)}')
    for file_name in files_name:
        json_content = json.loads(get_file(BUCKET_NAME, file_name))
        filter_json_content = list(filter(lambda d: d['type'] in key_values, json_content))
        for dict_item in filter_json_content:
            function_dict[dict_item['type']](dict_item['data'])
    session.commit()


def run_parse():
    while True:
        try:
            parse()
            time.sleep(60)
        except Exception as e:
            print(f'Error parse run: {e}')


run_parse()



























# def parse():
#     files = new_files()
#     print(f'Count new files: {len(files)}')
#     for file in files:
#         json_content = json.loads(get_file(bucket_name, file))
#         for item in json_content:
#             data = item['data']
#             if item['type'] == 'song':
#                 song = Song(data['artist_name'], data['title'], data['year'], data['release'])
#                 session.add(song)
#             elif item['type'] == 'movie':
#                 original_title_normalized = data['original_title']
#                 original_title_normalized = original_title_normalized.replace(' ', '_').lower()
#                 original_title_normalized = re.sub('[^A-Za-z0-9_]+', '', original_title_normalized)
#                 movie = Movie(data['original_title'], data['original_language'], data['budget'], data['is_adult'],
#                               data['release_date'], original_title_normalized)
#                 session.add(movie)
#             elif item['type'] == 'app':
#                 if data['rating'] > 3:
#                     is_awesome = True
#                 else:
#                     is_awesome = False
#                 app = App(data['name'], data['genre'], data['rating'], data['version'], data['size_bytes'], is_awesome)
#                 session.add(app)
#     session.commit()
