from base import Session, engine, Base
from sqlalchemy import Column, String, Integer, DateTime


def create_tasks_table(*_):
    Base.metadata.create_all(engine)
