import re

from models import Song, Movie, App
from db import session


def add_song(data):
    song = Song(data['artist_name'], data['title'], data['year'], data['release'])
    session.add(song)


def add_movie(data):
    original_title_normalized = data['original_title']
    original_title_normalized = original_title_normalized.replace(' ', '_').lower()
    original_title_normalized = re.sub('[^A-Za-z0-9_]+', '', original_title_normalized)
    movie = Movie(data['original_title'], data['original_language'], data['budget'], data['is_adult'], data['release_date'], original_title_normalized)
    session.add(movie)


def add_app(data):
    if data['rating'] > 3:
        is_awesome = True
    else:
        is_awesome = False
    app = App(data['name'], data['genre'], data['rating'], data['version'], data['size_bytes'], is_awesome)
    session.add(app)