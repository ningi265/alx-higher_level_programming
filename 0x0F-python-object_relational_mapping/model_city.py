#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py
"""
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """ inherits from Base imported from model_state """
    __tablename__ = "Cities"

    id = Column(Integer, Primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
