#!/usr/bin/python3
'''Module provide a class that map to State table'''
# Module for Connecting To MySQL database
import sys
from model_state import State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''Class mapping table Sate'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey(State.id))
