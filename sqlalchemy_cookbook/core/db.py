#!coding:utf-8
"""
db.py
"""


from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric,
                        String, DateTime, ForeignKey, Boolean, create_engine)


class DataAccessLayer:
    connection = None
    engine = None
    conn_string = None
    metadata = MetaData()
    chaoses = Table('chaoses', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('name', String(50), index=True),
                    Column('fractal', Integer()),
                    Column('created_at', DateTime, default=datetime.now()),
                    Column('modifyed_at', DateTime, default=datetime.now()),
                    )

    def db_init(self, conn_string):
    	self.engine = create_engine(conn_string or self.conn_string)
    	self.metadata.create_all(self.engine)
    	self.connection = self.engine.connect()

# Singletonが望ましい
dal = DataAccessLayer()
