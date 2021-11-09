# The pyshapefile module is used to read shapefiles and
# the pygeoif module is used to convert between geometry types
import shapefile
import pygeoif
from initdb_sqlalchemy import Arena, State, District, County
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base
# The built-in Tkinter GUI module allows for file dialogs
from tkinter import filedialog
from tkinter import Tk

#conn_string = 'postgresql://postgres:postgres@www.tamky.xyz:25432/geospatial'
conn_string = 'postgresql://postgres:postgres@localhost:5432/geospatial'
engine = create_engine(conn_string, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
# Initiate the Tkinter module and withdraw the console it generates
root = Tk()
root.withdraw()
# Navigate to the Arena shapefile using the Tkinter file dialog
#root.arenafile = filedialog.askopenfilename(initialdir = "./", title = "Select Arena Shapefile", filetypes = (("shapefiles","*.shp"), ("all files", "*.*")))
#arena_shapefile = shapefile.Reader(root.arenafile)
arena_shapefile = shapefile.Reader(r'C:\smartcity-platform\geo-service\geodata\data\Arenas_NBA.shp')
arena_shapes = arena_shapefile.shapes()
arena_records = arena_shapefile.records()

state_shapefile = shapefile.Reader(r'C:\smartcity-platform\geo-service\geodata\data\US_States.shp')
state_shapes = state_shapefile.shapes()
state_records = state_shapefile.records()

district_shapefile = shapefile.Reader(r'C:\smartcity-platform\geo-service\geodata\data\Congressional_Districts.shp')
district_shapes = district_shapefile.shapes()
district_records = district_shapefile.records()

county_shapefile = shapefile.Reader(r'C:\smartcity-platform\geo-service\geodata\data\US_County_Boundaries.shp')
county_shapes = county_shapefile.shapes()
county_records = county_shapefile.records()

# Iterate through the Arena data read from the shapefile
for count, record in enumerate(arena_records):
    arena = Arena()
    arena.name = record[6]
    print(arena.name)
    point = arena_shapes[count].points[0]
    arena.longitude = point[0]
    arena.latitude = point[1]
    arena.geom = 'SRID=4326;POINT({0} {1})'.format(point[0], point[1])
    session.add(arena)
session.commit()

# Iterate through the State data read from the shapefile
for count, record in enumerate(state_records):
    state = State()
    state.name = record[1]
    state.statefips = record[0]
    state.stpostal = record[2]
    state_geo = state_shapes[count]
    gshape = pygeoif.MultiPolygon(pygeoif.geometry.as_shape(state_geo))
    state.geom = 'SRID=4326;{0}'.format(gshape.wkt)
    session.add(state)
    if count % 10 == 0:
        session.commit()
session.commit()
# Iterate through the Districts data read from the shapefile
for count, record in enumerate(district_records):
    district = District()
    district.district = record[0]
    district.name = record[1]
    state = session.query(State).filter_by(statefips=record[4]).first()
    district.state_id = state.id
    district_geo = district_shapes[count]
    gshape = pygeoif.MultiPolygon(pygeoif.geometry.as_shape(district_geo))
    district.geom = 'SRID=4326;{0}'.format(gshape.wkt)
    session.add(district)
    if count % 50 == 0:
         session.commit
session.commit()         

# Iterate through the County data read from the shapefile
for count, record in enumerate(county_records):
    county = County()
    county.name = record[3]
    state = session.query(State).filter_by(name=record[2]).first()
    county.state_id = state.id
    county_geo = county_shapes[count]
    gshape = pygeoif.MultiPolygon(pygeoif.geometry.as_shape(county_geo))
    county.geom = 'SRID=4326;{0}'.format(gshape.wkt)
    session.add(county)
    if count % 50 == 0:
         session.commit
session.commit()        

session.close()
engine.dispose()