from sqlalchemy import Column, Integer, String, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from nitka.config import dsn

engine = create_engine(dsn)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Config(Base):
    __tablename__ = "config"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=255), unique=True)
    service_config = Column(JSON, nullable=False)
    source_tables = Column(JSON, nullable=True)
    target_tables = Column(JSON, nullable=True)
