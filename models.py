from os import name
from posixpath import supports_unicode_filenames
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50),index=True)
    surname = Column(String(50))
    email = Column(String(50))
    physical_address = Column(String(50),index=True)


class CD(Base):
    __tablename__ = "CD"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    duration =  Column(Float,index=True)
    year_of_release = Column(Integer,index=True)
    price = Column(Float,index=True)

class VINYL(Base):
    __tablename__ = "VINYL"

    vinyl_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    duration =  Column(Float,index=True)
    rate_of_speed = Column(Float, index=True)    
    year_of_release = Column(Integer,index=True)
    price = Column(Float,index=True)
