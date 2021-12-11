from sqlalchemy.orm.session import Session
from src.data_manager.src.database import mapper_registry
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
  def __init__(self):
    conn_string = 'postgresql://postgres:root@localhost:5432/x'
    engine = create_engine(conn_string, echo=True, future=True)
    mapper_registry.metadata.create_all(engine)

    self.__Session = sessionmaker(bind=engine)

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
