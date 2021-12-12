from sqlalchemy.orm import registry

mapper_registry = registry()
MetaData = mapper_registry.metadata
Base = mapper_registry.generate_base()