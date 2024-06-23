#!/usr/bin/python3
"""
    Models states file.
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base


class City(Base):
    """
        City class in the database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey("states.id"), nullable=False)
