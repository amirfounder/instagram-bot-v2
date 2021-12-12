from src.data_manager.database_utils import mapper_registry, engine, Session
from src.data_manager.database_entities import *


def setup():
    register_entities()
    sync_tables()


def register_entities():
    mapper_registry.metadata.create_all(engine)


def build_session():
    return Session()


def get_all():
    pass


def get():
    pass


def save(entity):
    session = build_session()
    session.add(entity)
    session.commit()


def update(entity):
    session = build_session()

    instance_as_dict = entity.__dict__
    instance_as_dict.pop('_sa_instance_state')

    session \
        .query(type(entity)) \
        .filter(type(entity).id == entity.id) \
        .update(instance_as_dict)
    
    session.commit()

def delete():
    pass


def sync_tables():
    tables_dict = mapper_registry.metadata.tables
    table_names = tables_dict.keys()
    tables = [tables_dict[x] for x in table_names]

    for table in tables:
        sync_table(table)


def sync_table(table):
    session = build_session()
    tablename = table.name

    columns_query = f'SELECT column_name, data_type ' \
        'FROM information_schema.columns ' \
        f'WHERE table_name = \'{tablename}\' AND table_schema = \'public\''

    db_columns = session.execute(columns_query).all()
    db_column_names = [x[0] for x in db_columns]

    model_columns = table.columns._all_columns
    model_columns = [(x.key, x.type.compile()) for x in model_columns]
    model_column_names = [x[0] for x in model_columns]

    model_columns_length = len(model_columns)
    db_columns_length = len(db_columns)

    if model_columns_length == db_columns_length:
        return

    alter_query = 'ALTER TABLE {} '.format(tablename)
    column_statements = []

    if model_columns_length > db_columns_length:
        differences = [x for x in model_columns if x[0] not in db_column_names]
        for diff in differences:
            column_statements.append(
                'ADD COLUMN {} {}'.format(diff[0], diff[1]))

    if db_columns_length > model_columns_length:
        differences = [x for x in db_columns if x[0] not in model_column_names]
        for diff in differences:
            column_statements.append('DROP COLUMN {}'.format(diff[0]))

    alter_query += ', '.join(column_statements)

    session.execute(alter_query)
    session.commit()
