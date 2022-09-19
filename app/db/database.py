from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DB_URL = "mysql://127.0.0.1:3306/board?user=root&password=deleo123"

Base = declarative_base()
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = Session()
