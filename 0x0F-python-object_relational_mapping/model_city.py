#!/usr/bin/python3
"""
Module for SQLAlchemy City model.

This module defines the City class, which is mapped to the 'cities' table
in the MySQL database.
The City class inherits from SQLAlchemy's declarative base.
"""

from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class to define each city record in the 'cities' table.

    Attributes:
        id (int): The primary key for the city record.
        name (str): The name of the city.
        state_id (int): The foreign key that references the states table.
    """
    __tablename__ = 'cities'  # Ensure table name is lowercase

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
