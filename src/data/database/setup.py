


def setup_database():
    register_entities()
    sync_tables()


def register_entities():
    mapper_registry.metadata.create_all(engine)


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

    model_columns = list(table.columns)
    model_columns = [(x.key, x.type.compile()) for x in model_columns]
    model_column_names = [x[0] for x in model_columns]

    model_columns_length = len(model_columns)
    db_columns_length = len(db_columns)

    if model_columns_length == db_columns_length:
        return

    alter_query = 'ALTER TABLE {} '.format(tablename)
    column_statements = []

    if model_columns_length > db_columns_length:
        diffs = [x for x in model_columns if x[0] not in db_column_names]
        for diff in diffs:
            column_statements.append(
                'ADD COLUMN {} {}'.format(diff[0], diff[1]))

    if db_columns_length > model_columns_length:
        diffs = [x for x in db_columns if x[0] not in model_column_names]
        for diff in diffs:
            column_statements.append('DROP COLUMN {}'.format(diff[0]))

    alter_query += ', '.join(column_statements)

    session.execute(alter_query)
    session.commit()