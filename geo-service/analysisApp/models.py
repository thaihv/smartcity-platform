from . import app

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define the Arena class, which will model the Arena database table
class Arena(Base):
    __tablename__ = 'arena'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    geom = Column(Geometry(geometry_type='POINT', srid=4326))

# Define the County class
class County(Base):
    __tablename__ = 'county'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey('state.id'))
    state_ref = relationship("State",backref='county')
    geom = Column(Geometry(geometry_type='MULTIPOLYGON',srid=4326))

# Define the District class
class District(Base):
    __tablename__ = 'district'
    id = Column(Integer, primary_key=True)
    district = Column(String)
    name = Column(String)
    state_id = Column(Integer, ForeignKey('state.id'))
    state_ref = relationship("State",backref='district')
    geom = Column(Geometry(geometry_type='MULTIPOLYGON',srid=4326))

# Define the State class
class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    statefips = Column(String)
    stpostal = Column(String)
    counties = relationship('County', backref='state')
    districts = relationship('District', backref='state')
    geom = Column(Geometry(geometry_type='MULTIPOLYGON',srid=4326))