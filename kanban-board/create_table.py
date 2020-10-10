from base import engine, Base


def create_tasks_table(*_):
    Base.metadata.create_all(engine)
