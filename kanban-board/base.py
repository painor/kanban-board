from sqlalchemy import create_engine, Table, Column, String, MetaData, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from rds_config import db_host, db_username, db_password, db_name

db_string = f"postgres://{db_username}:{db_password}@{db_host}:5432/{db_name}"

engine = create_engine(db_string)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String)
    status = Column('status', Integer)
    start_date = Column('start_date', DateTime)
    end_date = Column('end_date', DateTime)

    def __init__(self, title):
        self.title = title
