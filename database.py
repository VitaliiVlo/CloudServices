from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'

    media_id = Column(String(100), primary_key=True)
    comment_count = Column(Integer, default=0)


def get_db():
    engine = create_engine('sqlite:///production.db')
    Base.metadata.create_all(engine)
    return engine
