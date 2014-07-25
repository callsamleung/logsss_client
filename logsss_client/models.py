#coding:utf-8

import unittest
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql://root:keen@localhost/logsss')

class DB():
    session = sessionmaker(bind=engine)()

class M_Logsss(Base):
    __tablename__ = 'logsss'
    id = Column(Integer, primary_key = True)
    id_code = Column(String(50), nullable = False)
    update_at = Column(DateTime(), nullable = False)
    create_at = Column(DateTime(), nullable = False)
    tags = Column(String(100), nullable = True)
    status = Column(Integer, nullable = False)
    content = Column(Text)

def init_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()
