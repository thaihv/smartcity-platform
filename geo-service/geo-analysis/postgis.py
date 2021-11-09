import psycopg2
from shapely.geometry import LineString
from shapely.geometry import MultiLineString
connection = psycopg2.connect(database="geospatial",user="postgres", password="postgres")
cursor = connection.cursor()
cursor.execute("CREATE TABLE lines (id SERIAL PRIMARY KEY, location GEOMETRY)")
thelines=[]
thelines.append(LineString([(-106.635585,35.086972), (-106.621294,35.124997)]))
thelines.append(LineString([(-106.498309,35.140108), (-106.497010,35.069488)]))
thelines.append(LineString([(-106.663878,35.106459), (-106.586506,35.103979)]))
mls=MultiLineString([((-106.635585,35.086972), (-106.621294,35.124997)),((-106.498309,35.140108), (-106.497010,35.069488)),((-106.663878,35.106459), (-106.586506,35.103979))])
for a in thelines:
    cursor.execute("INSERT INTO lines (location) VALUES(ST_GeomFromText('{}'))".format(a.wkt))
connection.commit()


import psycopg2
from shapely.geometry import Polygon
connection = psycopg2.connect(database="geospatial",user="postgres", password="postgres")
cursor = connection.cursor()
cursor.execute("CREATE TABLE poly (id SERIAL PRIMARY KEY, location GEOMETRY)")
a=Polygon([(-106.936763,35.958191),(-106.944385,35.239293), (-106.452396,35.281908),(-106.407844,35.948708)])
cursor.execute("INSERT INTO poly (location) VALUES (ST_GeomFromText('{}'))".format(a.wkt))
connection.commit()


import psycopg2
from shapely.geometry import Polygon
connection = psycopg2.connect(database="geospatial",user="postgres", password="postgres")
cursor = connection.cursor()
cursor.execute("INSERT INTO art_pieces (code, location) VALUES (101, ST_GeomFromText('Point(-106.6958 35.5545)'))")


cursor.execute("CREATE TABLE areacommand (id SERIAL PRIMARY KEY, name VARCHAR(20), geom GEOMETRY)")
cursor.execute("CREATE TABLE beats (id SERIAL PRIMARY KEY, beat VARCHAR(6), agency VARCHAR(3), areacomm VARCHAR(15),geom GEOMETRY)")
cursor.execute("CREATE TABLE incidents (id SERIAL PRIMARY KEY, address VARCHAR(72), crimetype VARCHAR(255), date DATE,geom GEOMETRY)")


connection.commit()

# to interact Raster, on Windows at \PostgreSQL\13\bin
#raster2pgsql -I -C -s 4326 C:\smartcity-platform\geo-service\BigI.tif public.bigi | psql -U postgres -d geospatial