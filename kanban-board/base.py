from datetime import datetime

from sqlalchemy import create_engine, Column, String, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from rds_config import db_host, db_username, db_password, db_name

db_string = f'postgres://{db_username}:{db_password}@{db_host}:5432/{db_name}'

engine = create_engine(db_string)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Status:
    NEW = 0
    IN_PROGRESS = 1
    DONE: 2


class Task(Base):
    __tablename__ = 'tasks'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String)
    status = Column('status', Integer)
    start_date = Column('start_date', TIMESTAMP)
    end_date = Column('end_date', TIMESTAMP)

    def __init__(self, title):
        self.title = title
        self.status = Status.NEW


def add_new_task(title: str) -> int:
    """Adds a new task to the database and returns it's id"""
    new_task = Task(title)
    session = Session()
    session.add(new_task)
    session.flush()
    session.refresh(new_task)
    return new_task.id


def start_new_task(task_id: int) -> Task:
    """Starts a task and returns it"""
    session = Session()
    task: Task = session.query(Task).get(task_id)
    if not task:
        raise Exception(f'Task with id {task_id} not found')
    if task.status != Status.NEW:
        raise Exception('Task already in progress or already done')
    task.status = Status.IN_PROGRESS
    start_date = datetime.now().timestamp()
    task.start_date = start_date
    session.commit()
    return task
