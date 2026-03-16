from sqlalchemy import Column, Integer, String
from database import Base


class Property(Base):

    __tablename__ = "properties"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    address = Column(String)
    price = Column(Integer)
    source = Column(String)


class Vehicle(Base):

    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    make = Column(String)
    model = Column(String)
    price = Column(Integer)
    source = Column(String)
