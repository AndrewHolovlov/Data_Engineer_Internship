from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean, Date, Float, BigInteger
from db import base
from datetime import datetime


class Song(base):
    __tablename__='songs'
    id = Column(Integer, primary_key=True)
    artist_name = Column(String)
    title = Column(String)
    year = Column(Integer)
    release = Column(String)
    ingestion_time = Column(DateTime, default=datetime.now)

    def __init__(self, artist_name, title, year, release):
        self.artist_name = artist_name
        self.title = title
        self.year = year
        self.release = release

class Movie(base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    original_title = Column(String)
    original_language = Column(String)
    budget = Column(Integer)
    is_adult = Column(Boolean)
    release_date = Column(Date)
    original_title_normalized = Column(String)

    def __init__(self, original_title, original_language, budget, is_adult, release_date, original_title_normalized):
        self.original_title = original_title
        self.original_language = original_language
        self.budget = budget
        self.is_adult = is_adult
        self.release_date = release_date
        self.original_title_normalized = original_title_normalized

class App(base):
    __tablename__ = 'apps'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    rating = Column(Float)
    version = Column(String)
    size_bytes = Column(BigInteger)
    is_awesome = Column(Boolean)

    def __init__(self, name, genre, rating, version, size_bytes, is_awesome):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.version = version
        self.size_bytes = size_bytes
        self.is_awesome = is_awesome


