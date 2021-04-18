from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from config import DB_PATH, DB_PASSWORD, DB_LOGIN


engine = create_engine(f'postgresql://{DB_LOGIN}:{DB_PASSWORD}@{DB_PATH}')
base = declarative_base()
base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()