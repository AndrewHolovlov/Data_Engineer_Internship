from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from config import db_path, db_password, db_login


engine = create_engine(f'postgresql://{db_login}:{db_password}@{db_path}')
base = declarative_base()
base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()