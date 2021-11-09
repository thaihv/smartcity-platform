from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base

conn_string = 'postgresql://postgres:postgres@localhost:5432/geospatial'
engine = create_engine(conn_string, echo=True)
# Uncomment the line below if you need to recreate the database.
#drop_database(engine.url)

# Check to ensure that the database doesn't exist
# If it doesn't, create it and generate the PostGIS extention and tables
if not database_exists(engine.url):
    create_database(engine.url)

# Create a direct connection to the database using the engine.
# This will allow the new database to use the PostGIS extension.
conn = engine.connect()
conn.execute("commit")
try:
    conn.execute("CREATE EXTENSION postgis")
except Exception as e:
    print(e)
    print("extension postgis already exists")
conn.close()

# Define the model Base
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

# Create all tables using Base class
try:
    Base.metadata.create_all(engine)   
except:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine) 

# Or generate the State table from the State class.
# If it already exists, drop it and regenerate it
# try:
#     State.__table__.create(engine)
# except:
#     State.__table__.drop(engine)
#     State.__table__.create(engine)