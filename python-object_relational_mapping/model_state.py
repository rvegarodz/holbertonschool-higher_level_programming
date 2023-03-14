#!/usr/bin/python3
'''DOCUMENTATION'''
# Module for Connecting To MySQL database
import sys
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    ''' DOCUMENTATION '''
    __tablename__ = 'State'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
