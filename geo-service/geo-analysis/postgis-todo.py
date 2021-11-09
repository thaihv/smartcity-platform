
import psycopg2
from shapely.geometry import Point, LineString
import geopandas as gpd
import matplotlib.pyplot as plt

connection = psycopg2.connect(database="geospatial",user="postgres", password="postgres")
cursor = connection.cursor()
cursor.execute("SELECT id, ST_AsTexT(location) from lines")
data=cursor.fetchall()
print(data)
# Set CRS
cursor.execute("SELECT UpdateGeometrySRID('lines','location',4326)")
print(cursor.fetchall())
cursor.execute("SELECT Find_SRID('public','lines','location')")
print(cursor.fetchall())
# Display map
sql = "SELECT id, location as geom FROM lines"
gdf = gpd.GeoDataFrame.from_postgis(sql, connection, crs='epsg:4326')  
gdf.plot()
plt.show()

cursor.execute("SELECT id, ST_Length(location::geography) FROM lines ORDER BY ST_Length(location::geography)")
print(cursor.fetchall())

cursor.execute("SELECT ST_Intersects(l.location::geography,ll.location::geometry) FROM lines l, lines ll WHERE l.id=1 AND ll.id=3")
print(cursor.fetchall())

cursor.execute("SELECT ST_AsTexT(ST_Intersection(l.location::geography,ll.location::geometry)) FROM lines l, lines ll WHERE l.id=1 AND ll.id=3")
print(cursor.fetchall())

cursor.execute("SELECT id, ST_Area(location::geography) from poly")
print(cursor.fetchall())

isin=Point(-106.558743,35.318618)
cursor.execute("SELECT ST_Contains(polygon.location,ST_GeomFromText('{}')) FROM poly polygon WHERE polygon.id=1".format(isin.wkt))
print(cursor.fetchall())

cursor.execute("SELECT ST_Intersects(ST_GeomFromText('{}')::geography,polygon.location::geometry) FROM poly polygon WHERE polygon.id=1".format(isin.wkt))
print(cursor.fetchall())

isin=LineString([(-106.55,35.31),(-106.40,35.94)])
cursor.execute("SELECT ST_AsText(ST_Intersection(polygon.location,ST_GeomFromText('{}'))) FROM poly polygon WHERE polygon.id=1".format(isin.wkt))
print(cursor.fetchall())

cursor.execute("SELECT id, code,  ST_AsTexT(location) from art_pieces")
data=cursor.fetchall()
print(data)

connection.commit()