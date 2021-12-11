from src.data_manager.src.database import mapper_registry
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
  def __init__(self):
    conn_string = 'postgresql://postgres:root@localhost:5432/x'
    engine = create_engine(conn_string, echo=True, future=True)
    mapper_registry.metadata.create_all(engine)
    
    self.__Session = sessionmaker(bind=engine)
    self.__sync_all_tables()
  
  def build_session(self):
    return self.__Session()

  def save(self, instance):
    session = self.build_session()
    session.add(instance)
    session.commit()

  def update(self, instance):
    session = self.build_session()
    
    instance_as_dict = instance.__dict__
    instance_as_dict.pop('_sa_instance_state')

    session \
      .query(type(instance)) \
      .filter(type(instance).id == instance.id) \
      .update(instance_as_dict)
    
    session.commit()

  def get(self, id):
    pass

  def get_all(self):
    pass

  def __sync_all_tables(self):
    tables_dict = mapper_registry.metadata.tables
    table_names = tables_dict.keys()
    tables = [tables_dict[x] for x in table_names]

    for table in tables:
      self.__sync_table(table)

  def __sync_table(self, table):
    session = self.__Session()
    tablename = table.name
    
    columns_query = f'SELECT column_name, data_type ' \
      'FROM information_schema.columns ' \
        f'WHERE table_name = \'{tablename}\' AND table_schema = \'public\''

    db_columns = session.execute(columns_query).all()

    model_columns = table.columns._all_columns
    model_columns = [(x.key, x.type.compile()) for x in model_columns]

    model_columns_length = len(model_columns)
    db_columns_length = len(db_columns)

    if model_columns_length == db_columns_length:
      return
    
    alter_query = None

    if model_columns_length > db_columns_length:
      alter_query = self.__build_alter_table_add_columns_query(
        tablename,
        model_columns,
        db_columns
      )
    else:
      alter_query = self.__build_alter_table_drop_columns_query(
        tablename,
        model_columns,
        db_columns
      )

    session.execute(alter_query)
    session.commit()
  
  def __build_alter_table_add_columns_query(self, tablename, model_columns, db_columns):
    alter_query = f'ALTER TABLE {tablename} '
    add_column_statements = []

    db_column_names = [x[0] for x in db_columns]
    differences = [x for x in model_columns if x[0] not in db_column_names]

    for i in range(len(differences)):
      column = differences[i]
      statement = f'ADD COLUMN {column[0]} {column[1]}'
      add_column_statements.append(statement)
    
    add_columns_query = ', '.join(add_column_statements)
    return alter_query + add_columns_query

  def __build_alter_table_drop_columns_query(self, tablename, model_columns, db_columns):
    alter_query = f'ALTER TABLE {tablename} '
    add_column_statements = []

    model_column_names = [x[0] for x in model_columns]
    db_column_names = [x[0] for x in db_columns]
    differences = [x for x in db_column_names if x not in model_column_names]

    for i in range(len(differences)):
      column_name = differences[i]
      statement = f'DROP COLUMN {column_name}'
      add_column_statements.append(statement)
    
    add_columns_query = ', '.join(add_column_statements)
    return alter_query + add_columns_query

