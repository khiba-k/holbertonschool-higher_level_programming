#!/usr/bin/python3
"""
    Models states file.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
        State class in the database.
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
