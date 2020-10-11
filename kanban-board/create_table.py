from base import engine, Base


def create_tasks_table(*_):
    #Base.metadata.drop_all(engine)
    s = Base.metadata.create_all(engine)
    return s

