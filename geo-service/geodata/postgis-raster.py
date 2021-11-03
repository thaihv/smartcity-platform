
import psycopg2
from shapely.geometry import Point
from shapely.geometry import LineString
import geopandas as gpd
import matplotlib.pyplot as plt

connection = psycopg2.connect(database="geospatial",user="postgres", password="postgres")
cursor = connection.cursor()

# Options to RASTER
cursor.execute("SELECT * from bigi")
data=cursor.fetchall()
print(data)
cursor.execute("select ST_Summary(rast) from bigi;")
print(cursor.fetchall())
# All metadata types
cursor.execute("select ST_MetaData(rast) from bigi")
print(cursor.fetchall())
# Polygon
cursor.execute("select ST_AsText(ST_Envelope(rast)) from bigi;")
print(cursor.fetchall())
# W, H
cursor.execute("select st_height(rast), st_Width(rast) from bigi;")
print(cursor.fetchall())
# W,H in pixel
cursor.execute("select ST_PixelWidth(rast), ST_PixelHeight(rast) from bigi;")
print(cursor.fetchall())

cursor.execute("select ST_SummaryStats(rast) from bigi;")
print(cursor.fetchall())

cursor.execute("SELECT ST_Histogram(rast,1) from bigi;")
print(cursor.fetchall())
#Select polygon for a pixel 7,2
cursor.execute("select rid, ST_asText(ST_PixelAsPolygon(rast,7,2)) from bigi;")
print(cursor.fetchall())
#Select points for every pixel
cursor.execute("SELECT x, y, val, ST_AsText(geom) FROM (SELECT (ST_PixelAsCentroids(rast, 1)).* FROM bigi) as foo;")
print(cursor.fetchall())
cursor.execute("SELECT x, y, val, ST_AsText(geom) FROM (SELECT (ST_PixelAsPoints(rast, 1)).* FROM bigi) as foo;")
print(cursor.fetchall())
#Select points for 1 pixel
cursor.execute("SELECT ST_AsText(ST_PixelAsCentroid(rast,4,1)) FROM bigi;")
print(cursor.fetchall())


# Raster Values
cursor.execute("select ST_Value(rast,4,3) from bigi;")
print(cursor.fetchall())

cursor.execute("select ST_PixelOfValue(rast,1,50) from bigi;")
print(cursor.fetchall())

cursor.execute("select ST_ValueCount(rast) from bigi;")
print(cursor.fetchall())

cursor.execute("select ST_ValueCount(rast,1,True,50) from bigi;")
print(cursor.fetchall())

cursor.execute("select ST_DumpValues(rast,1) from bigi;")
print(cursor.fetchall())

# Value nearest with point
cursor.execute("select ST_NearestValue(rast,( select ST_SetSRID( ST_MakePoint(-71.629773,60.105389),4326))) from bigi;")
print(cursor.fetchall())

# Values nearest with point
cursor.execute("select ST_Neighborhood(rast,(select ST_SetSRID(ST_MakePoint(-71.629773,60.105389),4326)),1,1) from bigi;")
print(cursor.fetchall())


cursor.execute("SELECT ST_AsPNG(ST_asRaster(location,150,250,'8BUI')) from lines;")
c=cursor.fetchall()
with open('Foothills.png','wb') as f:
    f.write(c[0][0])
f.close()


connection.commit()